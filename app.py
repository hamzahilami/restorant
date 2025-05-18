from flask import Flask, request, jsonify, render_template
from menu_item import MenuItem
from menu_manager import MenuManager

app = Flask(__name__)

@app.route('/')
def index():
    items = MenuManager.all_items()
    return render_template('index.html', items=items)

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(MenuManager.all_items())

@app.route('/api/item/<string:name>', methods=['GET'])
def get_item(name):
    item = MenuManager.get_by_name(name)
    if item:
        return jsonify({"item_name": item[1], "item_price": item[2]})
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/item', methods=['POST'])
def add_item():
    data = request.get_json()
    item = MenuItem(data['name'], data['price'])
    item.save()
    return jsonify({"message": "Item added"}), 201

@app.route('/api/item/<string:name>', methods=['PUT'])
def update_item(name):
    data = request.get_json()
    item = MenuItem(name, 0)
    item.update(data['new_name'], data['new_price'])
    return jsonify({"message": "Item updated"})

@app.route('/api/item/<string:name>', methods=['DELETE'])
def delete_item(name):
    item = MenuItem(name, 0)
    item.delete()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
