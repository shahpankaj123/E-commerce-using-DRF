from rest_framework import serializers
from .models import *



class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class ProductLineserializer(serializers.ModelSerializer):
    class Meta:
        model=ProductLine
        fields='__all__'

class Brandserializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'        


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'