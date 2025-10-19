from flask import Flask, request, jsonify, send_file
import sqlite3
import os

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            value REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    device_id = data.get('device_id')
    value = data.get('value')

    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO sensor_data (device_id, value) VALUES (?, ?)", (device_id, value))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/sqlite_file', methods=['GET'])
def get_sqlite_file():
    return send_file('iot_data.db', as_attachment=True)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute("SELECT timestamp, value FROM sensor_data ORDER BY timestamp DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()

    html = "<h2>IoT Sensor Data</h2><table border='1'><tr><th>Time</th><th>Value</th></tr>"
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
    html += "</table>"
    return html

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
