from django.conf import settings

from suds.client import Client
from suds.sax.text import Raw


def get_authenticated_client():
    client = Client(settings.PKB_SERVICE_URL)
    CigWsHeader = client.factory.create('CigWsHeader')
    CigWsHeader.UserName = settings.PKB_SERVICE_USERNAME
    CigWsHeader.Password = settings.PKB_SERVICE_PASSWORD
    CigWsHeader.Culture = 'ru-RU'
    client.set_options(soapheaders=CigWsHeader)

    return client

def get_report(iin):
    client = get_authenticated_client()
    xml = Raw("""
                 <keyValue>
                   <idNumber>"""+str(iin)+"""</idNumber>
                   <idNumberType>14</idNumberType>
                   <reportImportCode>6</reportImportCode>
                </keyValue>
        """)
    result = client.service.GetReport(200004, xml)

    root = result['CigResult']['Result']['Root']
    existing_credits = root['ExistingContracts']['Contract'] if hasattr(root['ExistingContracts'], 'Contract') else []
    terminated_credits = root['TerminatedContracts']['Contract'] if hasattr(root['TerminatedContracts'], 'Contract') else []

    if not hasattr(existing_credits, 'count'):
        existing_credits = [existing_credits]

    if not hasattr(terminated_credits, 'count'):
        terminated_credits = [terminated_credits]

    overdue_for_existing = map(
        lambda x: {
            'non_used': x['OutstandingAmount']['_value'] or None,
            'overdue_days': x['NumberOfOverdueInstalments']['_value'], 
        },
        existing_credits
    )
    overdue_for_terminated = map(lambda x: {
            'credit_amount': x['TotalAmount']['_value'] or None,
            'overdue_days': x['NumberOfOverdueInstalments']['_value'], 
            'close_date_with_overdue': x['DateOfCreditEnd']['_value'] if x['NumberOfOverdueInstalments']['_value'] != '0' else None
        },
        terminated_credits
    )

    mvd_criminal = root['PublicSources']['MvdCriminalInvestigations']['Status']['_id']
    mvd_missing = root['PublicSources']['MvdMissingInvestigations']['Status']['_id']

    return {
        'existing_credits': overdue_for_existing, 
        'terminated_credits': overdue_for_terminated,
        'mvd_criminal': mvd_criminal != '2',  # 2 - means not found
        'mvd_missing': mvd_missing != '2',  # 2 - means not found
    }