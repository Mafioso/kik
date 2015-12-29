from django.test import TestCase

from ..models import Person, Form, Request
from ..factories import RequestFactory


class RequestTests(TestCase):
    
    def test_receive_request(self):
    	'''
    		we can receive request
    	'''
        data = {
            'document_id': '123',
            'conditions_data': {},
            'stage':'secondary',
            'renter':{
                'personal_data': {
                    'family_name': 'Smith',
                    'given_name': 'Nigel',
                    'middle_name': 'Patrick',
                    'iin': 123123123123,
                },
                'form':{
                    'contact_data': '',
                    'job_data': '',
                    'family_data': '',
                    'income_data': '',
                    'expenses_data': ''
                }
            },
            'guarants': [
                {
                    'personal_data': {
                        'family_name': 'Gordon',
                        'given_name': 'Michael',
                        'middle_name': 'Bruce',
                        'iin': 456456456456,
                    },
                    'form':{
                        'contact_data': '',
                        'job_data': '',
                        'family_data': '',
                        'income_data': '',
                        'expenses_data': ''
                    }
                },
            ],
            'msap': '10',
            'lpk': {},
            'gcvp':'##',
        }

        request = Request.receive_request(data=data)

        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Form.objects.count(), 2)
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(request.guarants.count(), 1)
        self.assertEqual(request.gcvp, '##')
        self.assertEqual(request.stage, 'secondary')
        self.assertEqual(request.document_id, '123')

    def test_receive_request_same_person(self):
    	'''
    		we do not save same person again
    	'''
        data = {
            'document_id': '123',
            'conditions_data': {},
            'stage':'secondary',
            'renter':{
                'personal_data': {
                    'family_name': 'Smith',
                    'given_name': 'Nigel',
                    'middle_name': 'Patrick',
                    'iin': 123123123123,
                },
                'form':{
                    'contact_data': '',
                    'job_data': '',
                    'family_data': '',
                    'income_data': '',
                    'expenses_data': ''
                }
            },
            'guarants': [
                {
                    'personal_data': {
                        'family_name': 'Gordon',
                        'given_name': 'Michael',
                        'middle_name': 'Bruce',
                        'iin': 456456456456,
                    },
                    'form':{
                        'contact_data': '',
                        'job_data': '',
                        'family_data': '',
                        'income_data': '',
                        'expenses_data': ''
                    }
                },
            ],
            'msap': '10',
            'lpk': {},
        }

        request = Request.receive_request(data=data)

        data = {
            'document_id': '123',
            'conditions_data': {},
            'stage':'secondary',
            'renter':{
                'personal_data': {
                    'family_name': 'Smith',
                    'given_name': 'Nigel',
                    'middle_name': 'Patrick',
                    'iin': 123123123123,
                },
                'form':{
                    'contact_data': '',
                    'job_data': '',
                    'family_data': '',
                    'income_data': '',
                    'expenses_data': ''
                }
            },
            'guarants': [],
            'msap': '10',
            'lpk': {},
        }

        request = Request.receive_request(data=data)

        self.assertEqual(Person.objects.count(), 2)

    def test_set_approved(self):
        r = RequestFactory()
        r.set_status('approved')
        self.assertEqual(r.status, 'approved')

    def test_set_declined(self):
        r = RequestFactory()
        r.set_status('declined')
        self.assertEqual(r.status, 'declined')

    def test_set_problem(self):
        r = RequestFactory()
        r.set_status('problem')
        self.assertEqual(r.status, 'problem')

    def test_get_last_by_person_iin(self):
        r1 = RequestFactory()
        renter = r1.renter
        r2 = RequestFactory(renter=renter)
        r = Request.get_last_by_person_iin(renter.personal_data['iin'])
        self.assertEqual(r.id, r2.id)

    def test_set_lawyer_conclusion(self):
        r = RequestFactory()
        r.set_lawyer_conclusion({'key': 'value'})
        self.assertEqual(r.lawyer_conclusion, {'key': 'value'})

    def test_set_risk_conclusion(self):
        r = RequestFactory()
        r.set_risk_conclusion({'key': 'value'})
        self.assertEqual(r.risk_conclusion, {'key': 'value'})

    def test_set_security_conclusion(self):
        r = RequestFactory()
        r.set_security_conclusion({'key': 'value'})
        self.assertEqual(r.security_conclusion, {'key': 'value'})

    def test_set_credit_manager_conclusion(self):
        r = RequestFactory()
        r.set_credit_manager_conclusion({'key': 'value'})
        self.assertEqual(r.credit_manager_conclusion, {'key': 'value'})

    def test_set_committee_decision(self):
        r = RequestFactory()
        r.set_committee_decision(True)
        self.assertEqual(r.status, 'approved_by_rc')

        r.set_committee_decision(False)
        self.assertEqual(r.status, 'declined_by_rc')