from rest_framework import serializers

from core.models import ColetaAgendada

class ColetaAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColetaAgendada
        fields = "__all__"