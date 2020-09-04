from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    stream = os.popen('hostname --short')
    hostname = stream.read()
    return "Hello World from {} !!".format(hostname)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
