from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_info', methods=['POST'])
def receive_info():
    data = request.get_json()
    print("Received Data:", data)
    # 원하는대로 저장하거나 가공
    with open('collected_data.json', 'a') as f:
        f.write(json.dumps(data, indent=4))
    return "Data received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
