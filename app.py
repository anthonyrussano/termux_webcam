from flask import Flask, send_file, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_image')
def get_image():
    subprocess.run("termux-camera-photo camera.jpg", shell=True)
    return send_file("camera.jpg", mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
