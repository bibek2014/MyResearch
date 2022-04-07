from flask import Flask, request, jsonify
import base64
app = Flask(__name__)


@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print(content)

    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host="192.168.83.12")