from flask import Flask, jsonify, request
from inventory import inventory
from services.openfoodfacts import get_product_by_barcode

app = Flask(__name__)


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):

    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200

@app.route("/inventory", methods=["POST"])
def create_item():

    data = request.get_json()

    required_fields = [
        "name",
        "barcode",
        "category",
        "price",
        "quantity"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    new_id = max([item["id"] for item in inventory], default=0) + 1

    new_item = {
        "id": new_id,
        "name": data["name"],
        "barcode": data["barcode"],
        "category": data["category"],
        "price": data["price"],
        "quantity": data["quantity"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()

    allowed_fields = [
        "name",
        "barcode",
        "category",
        "price",
        "quantity"
    ]

    for field in allowed_fields:
        if field in data:
            item[field] = data[field]

    return jsonify(item), 200

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({
        "message": "Item deleted successfully"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)