from People.models import Person
from People.serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework import permissions

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]