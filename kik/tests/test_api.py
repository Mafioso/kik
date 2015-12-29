import json
import urllib

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import RequestFactory


def prepare_urls(path_name, query={}, *args, **kwargs):
        url = reverse(path_name, *args, **kwargs)
        url += '?' + urllib.urlencode(query)
        return url

class RequestTests(APITestCase):
    def setUp(self):
        pass

    def test_receive_request(self):
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
                    'contact_data': {},
                    'job_data': {},
                    'family_data': {},
                    'income_data': {},
                    'expenses_data': {}
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
                        'contact_data': {},
                        'job_data': {},
                        'family_data': {},
                        'income_data': {},
                        'expenses_data': {}
                    }
                },
            ],
            'msap': '10',
            'lpk': {},
        }
        data = json.dumps(data)

        url = prepare_urls('request-receive', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_approved(self):
        r = RequestFactory()

        url = prepare_urls('request-approved', kwargs={'pk': r.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_declined(self):
        r = RequestFactory()

        url = prepare_urls('request-declined', kwargs={'pk': r.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_problem(self):
        r = RequestFactory()

        url = prepare_urls('request-problem', kwargs={'pk': r.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_find_request(self):
        r = RequestFactory()

        url = prepare_urls('request-find', query={'iin': r.renter.personal_data['iin']})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = prepare_urls('request-find', query={'iin': '123'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = prepare_urls('request-find', query={'iin': ''})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = prepare_urls('request-find')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_lawyer(self):
        r = RequestFactory()
        data = {
            'document_id': r.document_id,
            'lawyer_conclusion': {
                'key': 'value',
            }
        }
        data = json.dumps(data)

        url = prepare_urls('request-lawyer', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_risk(self):
        r = RequestFactory()
        data = {
            'document_id': r.document_id,
            'risk_conclusion': {
                'key': 'value',
            }
        }
        data = json.dumps(data)

        url = prepare_urls('request-risk', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_security(self):
        r = RequestFactory()
        data = {
            'document_id': r.document_id,
            'security_conclusion': {
                'key': 'value',
            }
        }
        data = json.dumps(data)

        url = prepare_urls('request-security', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_credit_manager(self):
        r = RequestFactory()
        data = {
            'document_id': r.document_id,
            'credit_manager_conclusion': {
                'key': 'value',
            }
        }
        data = json.dumps(data)

        url = prepare_urls('request-credit-manager', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_committee(self):
        r = RequestFactory()
        data = {
            'document_id': r.document_id,
            'decision': True
        }
        data = json.dumps(data)

        url = prepare_urls('request-committee', query={'data': data})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)