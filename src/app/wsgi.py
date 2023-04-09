from flask import Flask, request, render_template, jsonify
import os
import sys

modelPath = os.path.abspath(os.path.join(__file__, "..", "..", "main", "model"))
sys.path.insert(0, modelPath)

from classifier import predict

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        text_input = request.get_json()['value']
        return jsonify({"result": predict(text_input).tolist()})
    else:
        return render_template('index.html', text="[placeholder]")


if __name__ == '__main__':
    app.run()