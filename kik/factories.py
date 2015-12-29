import factory

from .models import Person, Form, Request


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    personal_data = {
                'family_name': factory.Faker('last_name').evaluate(None, None, False),
                'given_name': factory.Faker('first_name').evaluate(None, None, False),
                'middle_name': factory.Faker('suffix_male').evaluate(None, None, False),
                'iin': str(factory.Faker('random_number', digits=12).evaluate(None, None, False)),
            }
    

class FormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Form


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Request

    conditions_data = {}
    document_id = factory.Faker('uuid4')
    renter = factory.SubFactory(PersonFactory)