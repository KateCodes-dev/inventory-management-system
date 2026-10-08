import requests


BASE_URL = "https://world.openfoodfacts.org"


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/api/v3/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    return data.get("product")