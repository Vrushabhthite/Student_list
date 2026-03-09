from rest_framework import serializers
from .models import Student



# Serializer Convert model data to JSON

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

        