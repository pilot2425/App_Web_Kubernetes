from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    "host": os.getenv("MYSQL_HOST", "mysql-service"),
    "user": os.getenv("MYSQL_USER", "appuser"),
    "password": os.getenv("MYSQL_PASSWORD", "apppassword"),
    "database": os.getenv("MYSQL_DATABASE", "test_db"),
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM message LIMIT 1;")
        message = cursor.fetchone()[0]
        conn.close()
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
