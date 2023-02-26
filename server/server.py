from flask import Flask, send_from_directory, request
import random
import os
import logging
from .. import videotoframe
from PIL import Image, PngImagePlugin
from ..webuiAPI import client
import time

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='../client/public')

class Video(object):
    defaultUploadOptions = {
        "filename": "file",
        "validation": {
            "allowedExtensions": ["mp4", "webm", "ogg"],
            "sizeLimit": 10485760
        },
    }
    @staticmethod
    def upload(request, options = None):
        if options is None:
            options = Video.defaultUploadOptions
        print(str(request))
        return File.upload(request, options)
        
@app.route("/")
def base():
    app.logger.debug('Debug message')
    app.logger.info('Info message')
    app.logger.warning('Warning message')
    app.logger.error('Error message')
    app.logger.critical('Critical message')
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def home(path):
    return send_from_directory(app.static_folder, path)

@app.route("/rand")
def hello():
    app.logger.info("HERE in RAND")
    return str(random.randint(0, 100))

@app.route("/upv", methods=["POST"])
def upload_video():
    app.logger.info("HERE in UPLOAD VIDEO")
    file = request.files['video']
    fps = request.form['fps']
    prompt = request.form['prompt']
    model = request.form['model']
    samplingMethod = request.form['samplingMethod']
    filename = file.filename
    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    fname = filename[:-4]
    fps = request.args.get('fps')
    videotoframe.video2frame(os.path.join(app.config['UPLOAD_FOLDER'], fname), fps)
    dirpath = os.path.join(app.config['UPLOAD_FOLDER'], fname + "-opencv")
    files = os.listdir(dirpath)
    for file in files:
        frame = os.path.join(dirpath, file)
        fimg = Image.open(frame)
        oimg = client.controlNetImg2img(fimg)
        client.saveimg("outputs/" + fname + "-outimg", oimg)
        time.sleep(1)
    return "ok"

@app.route("/dlv", methods=["GET"])
def download_video():
    fname = request.args.get('dfn')
    app.logger.info("HERE in DOWNLOAD VIDEO")
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], f"{fname}.mp4")

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['DOWNLOAD_FOLDER'] = 'downloads'
    app.run(debug=True)