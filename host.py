#!flask/bin/python
from flask import  Flask
from flask import request, jsonify
from flask_cors import CORS

def convert_and_save(b64_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

app =Flask(__name__)
cors = CORS(app)
# @app.route('/')
# def index():
#     return "Hello, World!"

@app.route('/api/end', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    print(request.json.image)
    convert_and_save(request.json.image)
    return jsonify(request.json), 201

if __name__ == '__main__':
    app.run(debug=True)