# tests.py

from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceAPITestCase(APITestCase):
    def test_create_invoice(self):
        data = {
            'date': '2024-02-17',
            'customer_name': 'Test Customer',
            'invoice_details': [
                {'description': 'Item 1', 'quantity': 1, 'unit_price': '10.00', 'price': '10.00'},
                {'description': 'Item 2', 'quantity': 2, 'unit_price': '20.00', 'price': '40.00'}
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
