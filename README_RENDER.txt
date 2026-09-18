SCAR DEC - Render/local layout

ROOT
- app.py            Fixed Flask application
- run.py            Local/RDP launcher
- start.bat         Windows launcher for run.py
- requirements.txt  Python dependencies
- db.json            Local database file
- .env.example       Example environment variables (no secrets)

FOLDERS
- templates/         login.html, index.html, dashboard.html
- static/            web assets

RENDER
Build command: pip install -r requirements.txt
Start command: gunicorn app:app

Do not upload a real .env file containing passwords/session credentials to GitHub.
Put required environment variables in Render's Environment settings.

LOCAL/RDP
Run start.bat, or:
python run.py

Session note
The fixed app keeps the requests cookie jar authoritative and refreshes the CSRF header from the current cookie. This can reduce problems caused by stale local cookies/CSRF values. It cannot prevent server-side session invalidation.
