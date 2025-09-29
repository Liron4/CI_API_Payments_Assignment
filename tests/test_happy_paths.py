import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
PAGE_CODE = os.getenv("PAGE_CODE")
USER_ID = os.getenv("USER_ID")

def test_successful_payment_creation():
    form_data = {
        'pageCode': PAGE_CODE,
        'userId': USER_ID,
        'sum': '100',
        'paymentNum': '1',
        'description': 'Test Order 123',
        'pageField[fullName]': 'Test User',
        'pageField[phone]': '0501234567',
        'pageField[email]': 'test@example.com'
    }
    
    response = requests.post(API_URL, data=form_data)
    
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get('status') == 1
    assert 'data' in response_json
    data = response_json['data']
    assert 'url' in data
    payment_url = data['url']
    assert payment_url.startswith('https://')