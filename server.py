import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from threading import Lock

async_mode = None
app = Flask(__name__, static_folder='HyeonRista_client/build')
thread_lock = Lock()
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)