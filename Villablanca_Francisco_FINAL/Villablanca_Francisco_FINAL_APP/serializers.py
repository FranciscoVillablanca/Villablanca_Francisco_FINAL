from rest_framework import serializers
from .models import Institucion, Inscrito

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'