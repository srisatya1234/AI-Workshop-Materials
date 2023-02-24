from flask import Flask, request, jsonify
from module import search, update

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api_alive = 'Im alive'


@app.route('/api/search_books', methods=['GET', 'POST'])
def extract_names():
    """
        input to api 
        {
            "title": "booktitle",
            "author": "",
        }
        output to api
        {
            "id": "",
            "available": "yes/no",
            "borrower": "",
            "borrowed_date": ""
        }
    """
    
    if request.method == 'GET':
        return api_alive
    else:
        input_json = request.json
        title = input_json.get('title', None) # api input should have city key
        author = input_json.get('author', None) # api input should have email key
        result = search(title, author)
        return jsonify(result)
    

@app.route('/api/update_status', methods=['GET', 'POST'])
def update_status():
    """
        update the status to 1 if borrowed, else 0 if returned
        input to api 
        {
            "id": "",
            "borrower": "",
            "status": 1
        }
        output to api
        {
            "status": "",
        }
    """
    
    if request.method == 'GET':
        return api_alive
    else:
        input_json = request.json
        id = input_json.get('id', None) # api input should have city key
        borrower = input_json.get('borrower', None) # api input should have email key
        status = input_json.get('status', 0)
        result = update(id, borrower, status)
        return jsonify(result)
    

if __name__ == '__main__':
    # use any port number between 1001 to 9999
    # if the same port is being used it will throw error mentioning port already in use.
    app.run("0.0.0.0", port=8000)
