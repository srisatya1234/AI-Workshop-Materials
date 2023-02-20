from flask import Flask, request, jsonify
from module import search

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api_alive = 'Im alive'


@app.route('/api/extract_names', methods=['GET', 'POST'])
def extract_names():
    """
        input to api 
        {
            "city": "mycityname",
            "email": "email@gmail.com",
            "starting_letter": "s",
            "search_type": "city" 
        }
        output to api
        {
            "names": []
        }
    """
    
    if request.method == 'GET':
        return api_alive
    else:
        input_json = request.json
        city_name = input_json.get('city', None) # api input should have city key
        email = input_json.get('email', None) # api input should have email key
        starting_letter = input_json.get('starting_letter', None)
        search_type = input_json.get('search_type', 'city')
        result = search(city_name, email, starting_letter, search_type)
        return jsonify(result)
    

if __name__ == '__main__':
    # use any port number between 1001 to 9999
    # if the same port is being used it will throw error mentioning port already in use.
    app.run("0.0.0.0", port=8000)
