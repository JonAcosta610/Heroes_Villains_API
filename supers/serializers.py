from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'type']
        depth = 1