from rest_framework import serializers
from web.models import Cvs


class CvsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cvs
        fields = '__all__'