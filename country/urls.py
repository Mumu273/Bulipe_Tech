from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryAPIView

router = DefaultRouter()

router.register('', CountryAPIView, basename='country')

urlpatterns = [

] + router.urls