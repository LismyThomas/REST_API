from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from . models import Person
from . serializers import person_serializer

# Create your views here.
class PersonListCreateView(ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=person_serializer
    
class PersonDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=person_serializer