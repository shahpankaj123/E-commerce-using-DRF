from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response



class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing 
    """
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = Brandserializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing 
    """
    def list(self, request):
        queryset = Product.objects.all()
        serializer = Productserializer(queryset, many=True)
        return Response(serializer.data)
    
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing 
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = Categoryserializer(queryset, many=True)
        return Response(serializer.data)    

# Create your views here.
