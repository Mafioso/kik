from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from kik.models import Person
from kik.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    @list_route(methods=['get'], url='build_agenda')
    def build_agenda(self, request, *a, **kw):
        projects = Person.build_agenda(request.query_params.get('limit', 5))
        serializer = self.get_serializer(projects, many=True)
        return response.Response(serializer.data)

