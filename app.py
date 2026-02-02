"""
Простое Flask-приложение для тестирования Docker-контейнера.
"""
from flask import Flask, jsonify
import os
import socket
import platform

app = Flask(__name__)


@app.route("/")
def index():
    """Главная страница — приветствие и информация о контейнере."""
    hostname = socket.gethostname()
    return {
        "message": "Flask приложение работает в Docker!",
        "hostname": hostname,
        "status": "ok",
    }


@app.route("/health")
def health():
    """Эндпоинт для проверки здоровья приложения (healthcheck)."""
    return {"status": "healthy"}, 200


@app.route("/info")
def info():
    """Эндпоинт для получения информации о системе."""
    return {
        "system": {
            "platform": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "node": platform.node(),
        },
        "environment": {
            "python_version": platform.python_version(),
            "hostname": socket.gethostname(),
            "working_directory": os.getcwd(),
            "environment_vars_count": len(os.environ),
        },
        "status": "ok"
    }


@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    """Умножение двух чисел"""
    return jsonify({
        'result': a * b
    }), 200

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        return jsonify({
            'error': 'Division by zero'
        }), 400
    return jsonify({
        'result': a / b
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
