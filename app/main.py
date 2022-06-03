from flask import Flask, jsonify, request
from flask_cors import CORS
from pytube import YouTube

app = Flask(__name__)
CORS(app)

@app.route("/f/<string:isim>",methods=['POST','GET'])
def fullrez(isim: str):
        link = "https://www.youtube.com/watch?v="+isim
        yt = YouTube(link)
        source_link = yt.streams.filter(file_extension='mp4', resolution='1080p').order_by('resolution').desc().first().url
        return jsonify(url = source_link),200

@app.route("/m/<string:isim>",methods=['POST','GET'])
def lowrez(isim: str):
        link = "https://www.youtube.com/watch?v="+isim
        yt = YouTube(link)
        source_link = yt.streams.filter(file_extension='mp4', resolution='720p').order_by('resolution').desc().first().url
        return jsonify(url = source_link),200

if __name__ == "__main__":
    app.run()
