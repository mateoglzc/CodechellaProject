from flask import render_template, url_for, request
from Naked.toolshed.shell import execute_js, muterun_js
from CCW import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweetsInfo')
def tweetsInfo():
    return render_template('tweetsInfo.html')

@app.route('/visualmap')
def visualMap():
    # result = execute_js('CCW/static/JS/getTweetLocations.js')
    return render_template('visualMap.html')
