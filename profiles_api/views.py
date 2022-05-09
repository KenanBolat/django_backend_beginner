from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from profiles_api import serializers
from rest_framework import viewsets
from . import models


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = ['Uses HTTP methods as function (get, post, patch, put, delete)',
                       'Is similar to a traditional Django View',
                       'Gets input from the URL',
                       'Gets input from the body']
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
