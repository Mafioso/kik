import json
import urllib

from django.http import HttpResponse

from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework import viewsets, status

from kik.models import Request
from kik.serializers import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    @list_route(methods=['get'], url_path='receive')
    def receive(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        obj = Request.receive_request(data=data)

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_path='approved')
    def approved(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.set_status('approved')

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_path='declined')
    def declined(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.set_status('declined')

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_path='problem')
    def problem(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.set_status('problem')

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @list_route(methods=['get'], url_path='find')
    def find(self, request, *args, **kwargs):
        callback = request.query_params.get('callback', None)
        iin = request.query_params.get('iin', None)
        obj = Request.get_last_by_person_iin(iin=iin)
        if not obj:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(obj)
        return HttpResponse('{0}({1});'.format(callback, json.dumps(serializer.data)), content_type='text/javascript')

    @list_route(methods=['get'], url_path='lawyer')
    def lawyer(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        try:
            obj = Request.objects.get(document_id=data['document_id'])
        except Request.DoesNotExist:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND) 

        obj.set_lawyer_conclusion(data['lawyer_conclusion'])
        return Response('OK')

    @list_route(methods=['get'], url_path='risk')
    def risk(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        try:
            obj = Request.objects.get(document_id=data['document_id'])
        except Request.DoesNotExist:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND) 

        obj.set_risk_conclusion(data['risk_conclusion'])
        return Response('OK')

    @list_route(methods=['get'], url_path='security')
    def security(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        try:
            obj = Request.objects.get(document_id=data['document_id'])
        except Request.DoesNotExist:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND) 

        obj.set_security_conclusion(data['security_conclusion'])
        return Response('OK')

    @list_route(methods=['get'], url_path='credit_manager')
    def credit_manager(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        try:
            obj = Request.objects.get(document_id=data['document_id'])
        except Request.DoesNotExist:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND) 

        obj.set_credit_manager_conclusion(data['credit_manager_conclusion'])
        return Response('OK')

    @list_route(methods=['get'], url_path='committee')
    def committee(self, request, *args, **kwargs):
        data = json.loads(urllib.unquote(request.query_params.get('data', {})))
        try:
            obj = Request.objects.get(document_id=data['document_id'])
        except Request.DoesNotExist:
            return Response('Document not found', status=status.HTTP_404_NOT_FOUND) 

        obj.set_committee_decision(data['decision'])
        return Response('OK')
