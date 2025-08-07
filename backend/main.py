from flask import Flask, send_from_directory
from flask_cors import CORS
from app.routes import api

app = Flask(__name__, static_folder="static")
CORS(app)

# Register other API routes
app.register_blueprint(api)

# Serve static files like HTML
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/")
def home():
    return "✅ BabyCare API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
