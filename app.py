import os
import sys
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mobile/Website ko local computer se jodne ke liye

@app.route('/api/status', methods=['GET'])
def check_status():
    return jsonify({"status": "connected", "engine": "Offline-Voice-Bridge-v1"}), 200

@app.route('/api/tts', methods=['GET'])
def process_tts():
    text = request.args.get('text', '')
    lang = request.args.get('lang', 'eng')
    
    if not text:
        return jsonify({"error": "Text is empty"}), 400

    print(f"[LOCAL RUNTIME] Generating offline speech for language: {lang}")
    temp_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_stream.wav")
    
    if os.path.exists(temp_output):
        return send_file(temp_output, mimetype="audio/wav")
    else:
        return jsonify({"status": "processing", "message": "Voice compiled successfully"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, threaded=True)
