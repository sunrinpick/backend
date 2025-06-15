from rest_framework import serializers
from .models import FleaItem


class FleaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleaItem
        fields = '__all__'