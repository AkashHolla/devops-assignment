from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set")


@app.route('/')
def home():
    return jsonify({"status": "ok", "service": "service-a", "message": "Hello from Service A!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/data')
def data():
    return jsonify({"records": [1, 2, 3, 4, 5], "source": "service-a"})

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error occurred: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
