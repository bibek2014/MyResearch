import base64
import requests


filepath = "audio.mp3"
with open(filepath, 'rb') as f:
    audio_encoded = base64.b64encode(f.read())  # read file into RAM and encode it

audio_endcoded_string=audio_encoded.decode("utf-8")

data = {
    "audioData": audio_endcoded_string,  # base64 string    
}




url = 'http://192.168.83.12:5000/api/add_message/1234'
r = requests.post(url, json=data)  
if r.ok:
    print(r.json())