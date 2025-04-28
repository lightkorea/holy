from flask import Flask, request
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

@app.route('/', methods=['GET'])
def home():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return f"<pre>{json.dumps(data, indent=4)}</pre>"
    else:
        return "No data received yet."

@app.route('/receive_info', methods=['POST'])
def receive_info():
    data = request.get_json()
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    return "Data received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
