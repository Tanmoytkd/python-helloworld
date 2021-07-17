from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is TKD!!! I just discovered deployment pull policy"

@app.route("/test")
def test():
    return "Hello World! This is a test to check ArgoCD"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

