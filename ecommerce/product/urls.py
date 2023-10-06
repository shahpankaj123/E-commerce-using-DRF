
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Brand', BrandViewSet, basename='Brand')
router.register(r'Category', CategoryViewSet, basename='Category')
router.register(r'Product', ProductViewSet, basename='Product')

urlpatterns = [
    path('',include(router.urls)),
]