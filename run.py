from flask import Flask, request, Response
import json

import modules.createDb as createDb
import modules.addItem as addItem
import modules.getItem as getItem
import modules.updateItem as updateItem
import modules.deleteItem as deleteItem

app = Flask(__name__)

createDb.create_db()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/item/new', methods=['POST'])
def add_to_list():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Add item to the list
    res_data = addItem.add_to_list(item)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/item/all', methods=['GET'])
def get_items():
    # Get items from the helper
    res_data = getItem.get_all_items()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/item/<sr>', methods=['GET'])
def get_item_by_id(sr):
    res_data = getItem.get_item_by_id(sr)

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/item/update', methods=['PUT'])
def update_status():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    # Update item in the list
    res_data = updateItem.update_status(item, status)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/item/edit', methods=['PUT'])
def update_task():
    # Get item from the POST body
    req_data = request.get_json()
    print(req_data)
    sr = req_data['sr']
    item = req_data['item']

    # Update item in the list
    res_data = updateItem.update_task(sr,item)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item , status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/item/remove/<sr>', methods=['DELETE'])
def delete_item(sr):
    # Delete item from the list
    res_data = deleteItem.delete_item(sr)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + sr +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response