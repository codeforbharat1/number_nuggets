from flask import (Flask,jsonify)
import http.client
import json
# import requests

# Function that create the app 
def create_app(test_config=None ):
    # create and configure the app
    app = Flask(__name__)

    # Simple route
    @app.route('/')
    def hello_world(): 
        return jsonify({
           "status": "success",
            "message": "Hello World!"
        }) 
    
    # Simple route
    @app.route('/numberapi')
    def get_number_fact(): 
        conn = http.client.HTTPConnection("numbersapi.com")
        payload = "32"
        headers = {'Content-type': 'application/json'}
        conn.request("GET", "http://numbersapi.com/42/trivia",payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        print(data)
        return data
     
    return app # do not foget to return the app

APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=True)