import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def api_config():
    config = {
        'api_url': os.getenv("API_URL"),
        'page_code': os.getenv("PAGE_CODE"), 
        'user_id': os.getenv("USER_ID")
    }
    
    missing_vars = [key for key, value in config.items() if not value]
    if missing_vars:
        pytest.fail(f"Missing required environment variables: {missing_vars}")
    
    return config