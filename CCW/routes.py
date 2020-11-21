from flask import render_template, url_for, request
from CCW import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweetsInfo')
def tweetsInfo():
    return render_template('tweetsInfo.html')

@app.route('/visualmap')
def visualMap():
    return render_template('visualMap.html')
