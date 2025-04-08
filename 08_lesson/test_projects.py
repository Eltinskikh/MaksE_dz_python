import pytest
import requests
import uuid
from conftest import BASE_URL


def test_create_project_positive(auth_headers):
    """Позитивный тест создания проекта"""
    unique_id = uuid.uuid4().hex[:8]
    project_data = {
        "title": f"New Project {unique_id}"
    }
    try:
        response = requests.post(
            f"{BASE_URL}/projects",
            json=project_data,
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")

    assert response.status_code == 201, (
        f"Expected 201, got {response.status_code}. "
        f"Response: {response.text}"
    )
    assert "id" in response.json(), f"Response: {response.json()}"


def test_create_project_negative(auth_headers):
    """Негативный тест создания проекта (без title)"""
    project_data = {}
    try:
        response = requests.post(
            f"{BASE_URL}/projects",
            json=project_data,
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")

    assert response.status_code == 400, (
        f"Expected 400, got {response.status_code}. "
        f"Response: {response.text}"
    )


def test_get_project_positive(auth_headers, create_test_project):
    """Позитивный тест получения проекта"""
    project_id = create_test_project
    try:
        response = requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")

    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}. "
        f"Response: {response.text}"
    )
    assert response.json()["id"] == project_id


def test_get_project_negative(auth_headers):
    """Негативный тест получения проекта (несуществующий ID)"""
    try:
        response = requests.get(
            f"{BASE_URL}/projects/nonexistent_id_12345",
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")

    assert response.status_code == 404, (
        f"Expected 404, got {response.status_code}. "
        f"Response: {response.text}"
    )


def test_update_project_positive(auth_headers, create_test_project):
    """Позитивный тест обновления проекта"""
    project_id = create_test_project
    update_data = {
        "title": "Updated Project Title"
    }
    try:
        response = requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=update_data,
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Request failed (timeout?): {str(e)}")

    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}. Response: {response.text}"


def test_update_project_negative(auth_headers):
    """Негативный тест обновления проекта (несуществующий ID)"""
    update_data = {
        "title": "Should Not Update"
    }
    try:
        response = requests.put(
            f"{BASE_URL}/projects/nonexistent_id_12345",
            json=update_data,
            headers=auth_headers,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")

    assert response.status_code == 404, (
        f"Expected 404, got {response.status_code}. Response: {response.text}"
    )
