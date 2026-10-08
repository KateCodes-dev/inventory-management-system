from unittest.mock import patch

from services.openfoodfacts import get_product_by_barcode


@patch("services.openfoodfacts.requests.get")
def test_get_product_by_barcode(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Cereal",
            "categories": "Breakfast"
        }
    }

    result = get_product_by_barcode("123456789")

    assert result["product_name"] == "Test Cereal"
    assert result["categories"] == "Breakfast"