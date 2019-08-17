from flask import Flask

from Utils import api_utils

app = Flask(__name__)


@app.route('/getDetails', methods=['POST'])
def getDetails():
    """
    check Duration and return Date verification
    """
    # response = api_utils.getUserDetails()
    response = api_utils.getFriends()
    response.pop('_id')  # remove object id
    return response


if __name__ == '__main__':
    app.run(debug=True)
