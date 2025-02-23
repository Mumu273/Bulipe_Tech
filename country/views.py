from django.shortcuts import render

# Create your views here.

from drf_spectacular.utils import extend_schema

from external.swagger.swagger_query_params import set_query_params
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Country
from .serializers import CountrySerializer


@extend_schema(tags=['Country'])
class CountryAPIView(ReadOnlyModelViewSet):
    model_class = Country
    queryset = model_class.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_queryset(self):
        return self.model_class.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_class

    @extend_schema(parameters=set_query_params('list', [
        {"name": 'country_full_name', 'type': 'string'},
        {"name": 'country_code', 'type': 'string'}

    ]))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'country_full_name' in request.query_params.keys() and request.query_params.get('country_full_name') not in ['', "", None]:
            queryset = queryset.filter(full_name=request.query_params.get('country_full_name'))
        if 'country_code' in request.query_params.keys() and request.query_params.get('country_code') not in ['', "", None]:
            queryset = queryset.filter(country_code=request.query_params.get('country_code'))
        serializer_class = self.get_serializer_class()
        return Response(serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)


    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj = queryset.filter(id=kwargs['id']).first()
        if not obj:
            return Response("No object found", status=status.HTTP_400_BAD_REQUEST)
        serializer_class = self.get_serializer_class()
        return Response(serializer_class(obj, many=False).data, status=status.HTTP_200_OK)



