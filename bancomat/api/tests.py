# тестирует приложение

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from .views import Bill, Bill_serializer
from rest_framework.test import APITestCase, APIClient

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Bill_tests(TestCase):
    def test_create_proporties(self):
        '''Тестирую работу с атрибутами модели'''
        bill = Bill(name='100', count=500)
        bill.save()
        bill = Bill.objects.filter(name='100').first()
        self.assertFalse(bill == None)
        self.assertTrue(bill.count == 500)
        bill.set_balans()
        bill.save()
        self.assertTrue(bill.balans == 50000)


    def test_delete_model(self):
        bill = Bill(name='100', count=500)
        bill.save()
        bill = Bill.objects.filter(name='100').first()
        self.assertTrue(bill != None)
        bill.delete()
        bill = Bill.objects.filter(name='100').first()
        self.assertTrue(bill == None)



class BillSerializer_tests(TestCase):
    def test_BillSerializer(self):
        bill = Bill(name='100', count=500)
        bill.save()
        bill = Bill.objects.filter(name='100').first()
        self.assertFalse(bill == None)
        serializer = Bill_serializer(bill)
        self.assertTrue(type(serializer).__name__, 'Bill_serializer')
        self.assertTrue(type(serializer).__class__.__name__, 'SerializerMetaclass')
        self.assertTrue(serializer.data['name'] == '100')
        self.assertTrue(serializer.data['count'] == 500)



class appAPI_tests(APITestCase):
    def test_statusBank(self):
        response = self.client.get('/api/bank/status')
        self.assertEqual(response.data, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
