# -*- coding: utf-8 -*-
from xml.sax.saxutils import escape
from django.conf import settings

from suds.client import Client


def get_authenticated_client(url):
    client = Client(url=url,
                    username=settings.DOCUMENTOLOG_WSDL_USERNAME,
                    password=settings.DOCUMENTOLOG_WSDL_PASSWORD)
    return client

def move_document(doc_id):
    client = get_authenticated_client(url=settings.DOCUMENTOLOG_MOVE_WSDL)
    xml = escape(u"""<?xml version="1.0" encoding="UTF-8"?><root><item doctype_id='"""+settings.DOCUMENTOLOG_DOCTYPE_ID+"""' document_id='"""+unicode(doc_id)+"""'>Title</item></root>""")
    result = client.service.move(xml, 1)
    # print result

def edit_document(doc_id, **data):
    client = get_authenticated_client(url=settings.DOCUMENTOLOG_EDIT_WSDL)
    xml = escape(str(u"""<?xml version="1.0" encoding="UTF-8"?><root><item doctype_id='"""+settings.DOCUMENTOLOG_DOCTYPE_ID+"""' document_id='"""+unicode(doc_id)+"""'>Title</item></root>""".encode('utf-8')))
    result = getattr(client.service, str(u'Заявка_на_арендное_жилье'.encode('utf-8')))(xml, **data)
    # print result