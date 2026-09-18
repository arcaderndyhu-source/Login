"""Local/RDP launcher for the Flask app.

Environment variables:
  HOST=0.0.0.0
  PORT=5000
  SELF_URL=https://your-app.example.com/health
  SELF_PING_INTERVAL=45

For Render, the recommended start command is: gunicorn app:app
"""
import os
import threading
import time
import requests
from app import app


def _self_ping_loop():
    self_url = os.getenv("SELF_URL", "").strip()
    if not self_url:
        return

    try:
        interval = max(15, int(os.getenv("SELF_PING_INTERVAL", "45")))
    except ValueError:
        interval = 45

    while True:
        try:
            response = requests.get(self_url, timeout=15)
            print(f"SELF PING: {response.status_code} | {self_url}", flush=True)
        except Exception as exc:
            print(f"SELF PING FAILED: {exc}", flush=True)
        time.sleep(interval)


def _start_self_ping():
    if os.getenv("SELF_URL", "").strip():
        thread = threading.Thread(target=_self_ping_loop, daemon=True)
        thread.start()


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    _start_self_ping()
    app.run(host=host, port=port, debug=False)
