import pytest
import requests
import uuid
from requests.exceptions import RequestException

BASE_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = "указать токен"
REQUEST_TIMEOUT = 10


@pytest.fixture
def auth_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def create_test_project(auth_headers):

    unique_id = uuid.uuid4().hex[:8]
    project_data = {
        "title": f"Test Project {unique_id}"
    }
    try:
        response = requests.post(
            f"{BASE_URL}/projects",
            json=project_data,
            headers=auth_headers,
            timeout=REQUEST_TIMEOUT
        )
        if response.status_code == 201 and "id" in response.json():
            return response.json()["id"]
        pytest.skip(f"Failed to create test project: {response.text}")
    except RequestException as e:
        pytest.skip(f"API request failed: {str(e)}")
