from django.db import models
from django.contrib.postgres.fields import JSONField


class Person(models.Model):
    personal_data = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_edited = models.DateTimeField(auto_now=True, blank=True)

    @classmethod
    def build_agenda(cls, cnt):
        assert cnt > 0, "cnt should be at list 1"
        return Person.objects.all().select_related().order_by(
            '-date_edited', '-date_created')[:cnt]


class Form(models.Model):
    family_data = JSONField(null=True)
    address_data = JSONField(null=True)
    contact_data = JSONField(null=True)
    expenses_data = JSONField(null=True)
    income_data = JSONField(null=True)
    job_data = JSONField(null=True)
    person = models.ForeignKey(
        'Person', related_name='forms',
        on_delete=models.SET_NULL,
        null=True, blank=True)
    request = models.ForeignKey(
        'Request', related_name='forms',
        on_delete=models.SET_NULL,
        null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_edited = models.DateTimeField(auto_now=True, blank=True)


class Request(models.Model):
    STAGE_CHOICES = (
        ('initial', 'Initial'),
        ('secondary', 'Secondary'),
        )
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('problem', 'Problem'),
        ('pending', 'Pending'),
        ('approved_by_rc', 'Approved by rent committee'),
        ('declined_by_rc', 'Declined by rent committee'),
    )
    conditions_data = JSONField(null=True)
    renter = models.ForeignKey(
        'Person', related_name='requests',
        null=True, blank=True)
    document_id = models.CharField(max_length=50, null=True, blank=True)
    guarants = models.ManyToManyField('Person')
    msap = models.CharField(max_length=100, null=True, blank=True)
    lpk = JSONField(null=True)
    gcvp = models.CharField(max_length=100, null=True, blank=True)

    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='initial')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_edited = models.DateTimeField(auto_now=True, blank=True)
    lawyer_conclusion = JSONField(null=True)
    risk_conclusion = JSONField(null=True)
    security_conclusion = JSONField(null=True)
    credit_manager_conclusion = JSONField(null=True)

    @classmethod
    def receive_request(cls, data):
        renter_data = data.pop('renter')
        personal_data = renter_data.pop('personal_data')
        try:
            person = Person.objects.get(personal_data__iin=personal_data['iin'])
            person.personal_data = personal_data
            person.save()
        except Person.DoesNotExist:
            person = Person(personal_data=personal_data)
            person.save()

        guarants = data.pop('guarants')
        request = Request(renter=person, **data)
        request.save()
        form_data = renter_data.pop('form')
        renter_form = Form(person=person, request=request, **form_data)
        renter_form.save()

        for raw_guarant in guarants:
            personal_data = raw_guarant.pop('personal_data')
            try:
                guarant = Person.objects.get(personal_data__iin=personal_data['iin'])
                guarant.personal_data = personal_data
                guarant.save()
            except Person.DoesNotExist:
                guarant = Person(personal_data=personal_data)
                guarant.save()
            request.guarants.add(guarant)
            form_data = raw_guarant.pop('form')
            guarant_form = Form(person=guarant, request=request, **form_data)
            guarant_form.save()

        # mocking scoring calculation
        from .integrations.scoring import mock_scoring_result
        mock_scoring_result(request)

        return request

    @classmethod
    def get_last_by_person_iin(cls, iin):
        if not iin:
            return None
        try:
            person = Person.objects.get(personal_data__iin=iin)
            return person.requests.order_by('-date_edited').first()
        except Person.DoesNotExist:
            return None

    def set_status(self, status):
        self.status = status
        self.save()

    def set_lawyer_conclusion(self, lawyer_conclusion):
        self.lawyer_conclusion = lawyer_conclusion
        self.save()

    def set_risk_conclusion(self, risk_conclusion):
        self.risk_conclusion = risk_conclusion
        self.save()

    def set_security_conclusion(self, security_conclusion):
        self.security_conclusion = security_conclusion
        self.save()

    def set_credit_manager_conclusion(self, credit_manager_conclusion):
        self.credit_manager_conclusion = credit_manager_conclusion
        self.save()

    def set_committee_decision(self, decision):
        self.status = 'approved_by_rc' if decision else 'declined_by_rc'
        self.save()


class MVDPerson(models.Model):
    name_year = models.CharField(max_length=200)
