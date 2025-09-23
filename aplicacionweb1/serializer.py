from rest_framework import serializers
from .models import consulta1
from .models import DetalleVulnerabilidad
from .models import GraficaVulnerabilidades

class consulta1Serializer(serializers.ModelSerializer):
    class Meta:
        model = consulta1
        fields = '__all__'

class DetalleVulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVulnerabilidad
        fields = '__all__'

class GraficaVulnerabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraficaVulnerabilidades
        fields = '__all__'
