from flask import Flask, request, jsonify
import base64
from datetime import datetime





app = Flask(__name__)

audio_encoded = base64.b64encode
@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print(content['audioData'])
    print(content['uid']) 	
	
    ans = base64.b64decode(bytes(content["audioData"], 'utf-8'))

    print(type(ans)) #This is type bytes

    now = datetime.now() # current date and time
    today = now.strftime("%d-%m-%Y")
    flname ="Data/"+content['uid']+"_"+today

    with open(flname+".wav", "wb") as fh:
        fh.write(ans)

    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host="192.168.83.12")