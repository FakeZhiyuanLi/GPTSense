from flask import Flask, request, render_template
import os

import sys
sys.path.insert(0, '/Users/zhiyuan/Desktop/Hackathon/GPTSense/src/main/model')

from classifier import predict

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        text_input = request.form['input']
        return render_template('index.html', text=int((predict(text_input)*100)))
    else:
        return render_template('index.html', text="[placeholder]")


if __name__ == '__main__':
    app.run()