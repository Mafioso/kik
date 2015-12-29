from rest_framework import viewsets

from kik.models import Form
from kik.serializers import FormSerializer

class FormViewSet(viewsets.ModelViewSet):
	serializer_class = FormSerializer
	queryset = Form.objects.all()