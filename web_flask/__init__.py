from flask import Flask
from web_flask import routes

app = Flask(__name__)
routes.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
