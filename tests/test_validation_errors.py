import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
PAGE_CODE = os.getenv("PAGE_CODE")
USER_ID = os.getenv("USER_ID")

def test_payment_creation_with_invalid_email():
    form_data = {
        'pageCode': PAGE_CODE,
        'userId': USER_ID,
        'sum': '100',
        'paymentNum': '1',
        'description': 'Invalid Email Test',
        'pageField[fullName]': 'Test User',
        'pageField[phone]': '0501234567',
        'pageField[email]': 'invalid-email-format'
    }
    
    response = requests.post(API_URL, data=form_data)
    assert response.status_code == 422

def test_payment_creation_with_negative_sum():
    form_data = {
        'pageCode': PAGE_CODE,
        'userId': USER_ID,
        'sum': '-10',
        'paymentNum': '1',
        'description': 'Negative Sum Test',
        'pageField[fullName]': 'Test User',
        'pageField[phone]': '0501234567',
        'pageField[email]': 'test@example.com'
    }
    
    response = requests.post(API_URL, data=form_data)
    assert response.status_code == 422