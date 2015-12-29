from rest_framework import serializers
from .models import Person, Form, Request

class PersonSerializer(serializers.ModelSerializer):
    personal_data = serializers.DictField()
    form = serializers.SerializerMethodField()

    class Meta:
        model = Person

    def get_form(self, instance):
        request_id = self.context.get('request_id', None)
        if not request_id:
            return None
        try:
            form = instance.forms.get(request_id=request_id)
            return FormSerializer(form).data
        except Form.DoesNotExist:
            return None


class RequestSerializer(serializers.ModelSerializer):
    renter = serializers.SerializerMethodField()
    guarants = serializers.SerializerMethodField()
    conditions_data = serializers.DictField()

    class Meta:
        model = Request
        exclude = ('id', 'stage', 'status', 'date_created', 'date_edited', 'lawyer_conclusion', 'risk_conclusion', 'security_conclusion', 'credit_manager_conclusion',)

    def get_renter(self, instance):
        renter = instance.renter
        return PersonSerializer(renter, context={'request_id': instance.id}).data

    def get_guarants(self, instance):
        guarants = instance.guarants
        return PersonSerializer(guarants, many=True, context={'request_id': instance.id}).data


class FormSerializer(serializers.ModelSerializer):
    family_data = serializers.DictField()
    address_data = serializers.DictField()
    contact_data = serializers.DictField()
    expenses_data = serializers.DictField()
    income_data = serializers.DictField()
    job_data = serializers.DictField()

    class Meta:
        model = Form

