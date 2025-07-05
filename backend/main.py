# main.py
from flask import Flask
from app.routes import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")  # 👈 optional test route
def home():
    return "✅ BabyCare API is running!"

if __name__ == "__main__":
    app.run(debug=True)
