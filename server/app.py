from flask import Flask, request, jsonify
import sqlite3
import os
from flask_cors import CORS
from flask import send_from_directory


DB_PATH = os.path.join(os.path.dirname(__file__), "events.db")

app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project TEXT,
                metric TEXT,
                value REAL,
                step INTEGER,
                ts REAL
            )
        """)


@app.route('/ingest', methods=['POST'])
def ingest():
    api_key = request.headers.get('X-API-KEY')
    if not api_key:
        return "missing api key", 401

    data = request.get_json() or []
    if not isinstance(data, list):
        return "expected list", 400

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        for ev in data:
            c.execute("INSERT INTO events (project, metric, value, step, ts) VALUES (?, ?, ?, ?, ?)",
                      (ev.get('project'), ev.get('metric'), ev.get('value'), ev.get('step'), ev.get('timestamp')))
        conn.commit()

    return jsonify({"ok": True, "count": len(data)})


@app.route('/runs/<path:project>/metrics')
def get_metrics(project):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT metric, value, step, ts FROM events WHERE project=? ORDER BY ts DESC LIMIT 500", (project,))
        rows = c.fetchall()

    out = [ {"metric": r[0], "value": r[1], "step": r[2], "timestamp": r[3]} for r in rows ]
    return jsonify(out)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=3000, debug=True)