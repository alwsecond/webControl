from flask import Flask, render_template, request
import pyautogui
import socket
import os

def getname():
    return socket.gethostname()
def localip():
    return socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', hostname=getname())

@app.route('/off', methods=['POST'])
def off_func():
    if request.method == "POST":
        if (request.form.get('time') == 'undefined'):
            os.system("shutdown /s /t 0")
        else:
            os.system(f"shutdown /s /t {request.form.get('time')}")
        return '', 204

@app.route('/screen', methods=['POST'])
def screen_func():
    if request.method == "POST":
        if (request.form.get('status') != 'undefined'):
            pyautogui.screenshot('static/img.png')
        return '', 204

@app.route('/cmd', methods=['POST'])
def cmd_func():
    if request.method == "POST":
        if (request.form.get('command') != 'undefined'):
            os.system(f"{request.form.get('command')}")
        return '', 204

if __name__ == '__main__':
    app.run(
        host=f"{localip()}",
        port="8080",
        debug=False
    )