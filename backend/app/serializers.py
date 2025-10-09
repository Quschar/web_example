from rest_framework import serializers

from .models import *

class ItemSerialier(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('create_date', 'update_date')