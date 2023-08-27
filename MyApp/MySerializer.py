from rest_framework import serializers
from .models import Product
#this class will serialize the information
#in JSON format
class ProductSerializers (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields  = "__all__" 
        
