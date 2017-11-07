from flask import Flask
from flask_login import LoginManager, login_required

app = Flask(__name__)

@app.route("/")
def home():
    return "Under construction"

if __name__ == '__main__':
    app.run(port=5000, debug=True)