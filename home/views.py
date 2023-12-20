from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from . serializers import person_serializer

@api_view(['GET', 'POST'])
def PersonListCreateView(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = person_serializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = person_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'PUT', 'DELETE'])
def PersonDetailView(request, pk):

    person = Person.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = person_serializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = person_serializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
