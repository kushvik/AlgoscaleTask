from flask import Flask, request, make_response
from src.Utils import api_utils
import json

app = Flask(__name__)

@app.route('/getDetails', methods=['POST'])
def getDetails():
        """
        check Duration and return Date verification
        """
        # response = api_utils.getUserDetails()
        response = api_utils.getFriends()
        response.pop('_id')#remove object id
        return response

if __name__ == '__main__':
    app.run(debug=True)
       
        