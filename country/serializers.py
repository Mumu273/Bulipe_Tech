from rest_framework import serializers
from .models import Country
from external.exclude import exclude_list

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = exclude_list
