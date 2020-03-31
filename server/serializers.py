from rest_framework import serializers
from .models import *


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = [ 'number_photo']
