import pytest

from app import app
from inventory import inventory


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_single_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert response.json["id"] == 1


def test_get_missing_item(client):
    response = client.get("/inventory/9999")

    assert response.status_code == 404


def test_create_item(client):

    data = {
        "name": "Test Product",
        "barcode": "111111",
        "category": "Test",
        "price": 100,
        "quantity": 5
    }

    response = client.post(
        "/inventory",
        json=data
    )

    assert response.status_code == 201
    assert response.json["name"] == "Test Product"


def test_update_item(client):

    response = client.patch(
        "/inventory/1",
        json={
            "price": 200
        }
    )

    assert response.status_code == 200
    assert response.json["price"] == 200


def test_delete_item(client):

    response = client.delete("/inventory/1")

    assert response.status_code == 200