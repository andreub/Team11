from flask import Flask, jsonify, render_template
from gtts import gTTS
import requests
import uuid

app = Flask(__name__)

MP3 = dict()

def generate_mp3(quote):
   url = uuid.uuid5(uuid.NAMESPACE_DNS,quote)
   if not url in MP3:
       tts = gTTS(text=quote, lang='en')
       tts.save("/tmp/{}".format(url))
       MP3[url]=True
   return "/mp3/{}".format(url)

@app.route('/mp3/<file>')
def roi_mp3(file):
   return open("/tmp/{}".format(file),"rb").read()     

@app.route('/')
def roi_speak():
   try:
        r = requests.get("http://localhost:8078/proxy/?vip=team12&path=/api/quote/random")
        q = r.json()["quote"]
        #q = "Winter is coming"
        return render_template('index.html', quote=q, mp3_url=generate_mp3(q))
   except Exception as error:
        return not_found('Quote service error. {}'.format(error))

@app.route('/healthcheck')
def healthcheck():
    data = {
        'status': 'ok'
    }
    resp = jsonify(data)
    resp.status_code = 200
    return resp
    
@app.route('/Status')
def status():
    return 'Eureka!'
    
@app.errorhandler(404)
def not_found(error='Error'):
    message = {
            'status': 404,
            'message': error
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp    

if __name__ == '__main__':
    app.run(host='0.0.0.0')

