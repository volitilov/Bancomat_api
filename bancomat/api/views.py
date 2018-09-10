# обрабатывает запросы

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Bill
from .serializers import Bill_serializer

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class Bancomat(APIView):
    '''api банкомата'''

    def get(self, request): pass

    def set(self, request): pass

    def status(self, request): pass
