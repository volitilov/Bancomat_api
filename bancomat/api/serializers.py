# преобразует данные для api

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from rest_framework import serializers
from .models import Bill

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Bill_serializer(serializers.ModelSerializer):
    '''Сериализация банкнот'''
    class Meta:
        model = Bill
        fields = ('bill_name', 'bill_count')