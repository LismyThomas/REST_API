from rest_framework import serializers
from . models import Person

class person_serializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields ='__all__'