from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend JS to talk to Flask

@app.route("/order", methods=["POST"])
def receive_order():
    data = request.get_json()
    if not data or "items" not in data:
        return jsonify({"error": "Invalid order"}), 400

    # Print order in terminal
    print("\n=== Nouvelle commande reçue ===")
    print(f"Nom: {data.get('name')}")
    print(f"Téléphone: {data.get('phone')}")
    print(f"Adresse: {data.get('address')}")
    print(f"Remarques: {data.get('notes')}")
    print("Items:")
    for item in data["items"]:
        print(f" - {item['qty']} × {item['name']} (€{item['price']})")
    print(f"Total: €{data.get('total')}")
    print("============================\n")

    return jsonify({"message": "Commande reçue avec succès!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)

