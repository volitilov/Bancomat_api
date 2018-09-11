# - обрабатывает POST-запросы на снятие, и добавления налички
# - обрабатывает GET-запрос на проверку общего баланса банка

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import copy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bill
from .serializers import Bill_serializer
from django.http import Http404

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


@api_view(['POST'])
def withdraw_cash(request):
    '''Реализует снятие наличных'''
    if request.method == 'POST':
        amount = int(request.data['amount'])
        bills = Bill.objects.all()
        all_balans = 0
        cash = []
        
        # сумму всех денег в банкомате
        for i in bills: 
            all_balans += i.balans
    
        if all_balans < amount:
            return Response(
                data={'message': 'В банкомате не достаточно денег, доступная сумма: {}'.format(all_balans)}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        if amount == 0:
            return Response(
                data={'message': 'Нельзя снять 0'}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        # формирую список банкнот с их кол-вом для удобной обработки
        for bill in bills: 
            cash.append([int(bill.name), bill.count])
        
        cash = sorted(cash)[::-1]
        resp = {}
        for i in cash:
            bill_name = i[0]
            bill_count = i[1]
            min_bill = cash[-1][0]

            # проверяю остаток
            if amount % min_bill > 0:
                return Response(
                    data={'message': 'Минимальная купюра: {}'.format(min_bill)},
                    status=status.HTTP_400_BAD_REQUEST)

            # реализует снятие наличных
            for x in range(bill_count):
                if amount < bill_name and amount != 0: 
                    break
                amount -= bill_name
                if amount < 0:
                    break
                bill_count -= 1
                bill = Bill.objects.get(name=bill_name)
                bill.count = bill_count
                
                # формирует ответ
                if resp.get(bill_name):
                    resp[bill_name] += 1
                else:
                    resp.update({bill_name: 1})  
            
            bill.set_balans()
            bill.save()
        
        return Response(
            data=resp, 
            status=status.HTTP_200_OK)



@api_view(['POST'])
def add_cash(request):
    '''Реализует добавление кеша в банкомат'''
    if request.method == 'POST':
        for i in request.data:
            try:
                bill = Bill.objects.get(name=i)
                bill.count += int(request.data[i])
                bill.save()
                bill.set_balans()
            except Bill.DoesNotExist:
                bill = Bill(name=i, count=request.data[i])
                bill.save()
                bill.set_balans()
            bill.save()
        return Response(
            data={'message': 'Банкомат заправлен'}, 
            status=status.HTTP_201_CREATED)



@api_view(['GET'])
def banc_status(request):
    '''Отдаёт ответ о наминале в банкомате'''
    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = Bill_serializer(bills, many=True)
        data = {}
        for i in serializer.data:
            bill_with_count = list(i.values())
            data.update({bill_with_count[0]: bill_with_count[1]})
        return Response(data=data)
