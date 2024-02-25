from flask import Flask, request
from flask_cors import CORS
from db import Database
import json

app = Flask(__name__)
CORS(app)

db_handler = Database("login_details")

data_file_path = 'received_data.json'

all_login_data = []


def write_data_to_file(data):
    with open(data_file_path, 'w') as file:
        json.dump(data, file)

def read_data_from_file():
    try:
        with open(data_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

@app.route('/', methods=['POST'])
def receive_login_data():
    login_data = request.json

    all_login_data.append(login_data)

    db_handler.insert(login_data)

    write_data_to_file(all_login_data)
    return "-Data sent successfully"

@app.route('/', methods=['GET'])
def get_received_data():
    received_data = read_data_from_file()

    if received_data is None:
        return 'No data received yet'
    else:
        return received_data


if __name__ == '__main__':
    app.run(debug=True)


