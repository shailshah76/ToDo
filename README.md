# ToDo List

## About

Create CRUD API enpoints using Flask framework for different operation of tasks. Below are the enpoints with the proper curl command to test the endpoints

### <b>Integration with FrontEnd:</b>

The APIs provide data to interact and manipulate the tasks, which can be adapted in the frontend with the help of buttons and events. For e.g An Edit/Delete Button can interact with the specific endpoint to edit/delete the data.
</br></br>

### To run the application:

1. Clone the Repository from https://github.com/shailshah76/ToDo.git
2. cd Todo/
3. Run the command: 
```console
$ FLASK_APP=run.py flask run
```  

### <b>POST Request:</b>

```bash 
$ curl -X POST http://127.0.0.1:5000/item/new -d '{"item": "Implement POST endpoint"}' -H 'Content-Type: application/json'

{"Implement POST endpoint": "Not Started"}
```

### <b>GET Request:</b>

```bash 
$ curl -X GET http://127.0.0.1:5000/item/all

{"count": 2, "items": [["Setting up Flask", "Not Started"], [Implement POST endpoint", "Not Started"]]}
```

### <b>PUT Request:</b> 

#### <i>Status Update<i>

```bash 
$ curl -X PUT http://127.0.0.1:5000/item/update -d '{"item": "Setting up Flask", "status": "Completed"}' -H 'Content-Type: application/json'

{"Setting up Flask": "Completed"}
```
#### <i>Task Update<i>

```bash 
$ curl -X PUT http://127.0.0.1:5000/item/edit -d '{"sr": "1", "item": "Setting up Flask API"}' -H 'Content-Type: application/json'

{"1": "Setting up Flask API"}
```

### <b>DELETE Request:</b>

```bash 
$ curl -X DELETE http://127.0.0.1:5000/item/remove/1 -H 'Content-Type: application/json'
```

Bug report:

Updating task which is not present



