# обрабатывает запросы

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bill
from .serializers import Bill_serializer
from django.http import Http404

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


@api_view(['GET'])
def withdraw_cash(request): pass


@api_view(['POST'])
def add_cash(request):
    if request.method == 'POST':
        for i in request.data:
            try:
                bill = Bill.objects.get(bill_name=i)
                bill.bill_count += int(request.data[i])
            except Bill.DoesNotExist:
                bill = Bill(bill_name=i, bill_count=request.data[i])
            bill.save()
        return Response(request.data)


@api_view(['GET'])
def status(request):
    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = Bill_serializer(bills, many=True)
        data = {}
        for i in serializer.data:
            bill_with_count = list(i.values())
            data.update({bill_with_count[0]: bill_with_count[1]})
        return Response(data=data)
