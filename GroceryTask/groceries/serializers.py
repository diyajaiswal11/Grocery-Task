from rest_framework import serializers
from .models import *

class GroceryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model= GroceryItem
        fields = '__all__'