from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is TKD!!! I just discovered deployment pull policy"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

