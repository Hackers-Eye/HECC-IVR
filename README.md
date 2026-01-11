🛡️ Hacker's-Eye IVR Control Node

Cybersecurity-focused Interactive Voice Response (IVR) system built for telecom labs, OSINT research, and authorized security simulations.

Hackerseye IVR Control Node is a hacker-themed, lab-grade IVR platform built with Flask + Twilio that enables controlled call flows, speech and DTMF capture, real-time monitoring, and outbound call triggering — designed strictly for ethical and legal testing environments.

🚀 Features

☎️ Twilio-powered IVR engine

🧭 Multi-level menu system (Support / Training / Message)

🔢 DTMF + 🎤 Speech recognition

📞 Call recording enabled

🗃️ SQLite logging backend

🖥️ Hacker-style real-time admin dashboard

🔔 Telegram alerts on new inputs

📊 Runtime statistics API

⚡ Single-file Flask backend (easy to deploy)

📁 Project Structure (Minimal & Clean)
hackerseye-ivr/
│
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── admin.html


No complex modules. No microservices. Everything runs from one main file.

⚙️ Requirements

Python 3.9+

Twilio account (trial or paid)

Public HTTPS URL for webhook (ngrok / cloud server)

📦 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/hackerseye-ivr.git
cd hackerseye-ivr

2️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Configuration

Create a .env file in project root:

TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxx
TWILIO_NUMBER=+1xxxxxxxxxx
PUBLIC_BASE_URL=https://xxxx.ngrok-free.app

TELEGRAM_BOT_TOKEN=xxxxxxxx
ADMIN_CHAT_ID=xxxxxxxx


PUBLIC_BASE_URL must be a public HTTPS URL pointing to your Flask server.

▶️ Run the Server
python app.py


You should see the Hackerseye ASCII banner in terminal.

Default server:

http://localhost:5000

🌐 Expose Public URL (Required for Twilio)

Twilio must reach your server via HTTPS.

Option — Using ngrok
ngrok http 5000


Update .env:

PUBLIC_BASE_URL=https://xxxx.ngrok-free.app


Restart the server after updating.

☎️ Twilio Webhook Setup

In Twilio Console:

Phone Numbers → Your Number → Voice Configuration

Set:

When a call comes in:
Webhook
POST
https://xxxx.ngrok-free.app/voice


Save settings.

🧑‍💻 Admin Dashboard

Open in browser:

http://localhost:5000/admin


Dashboard shows:

Caller number

Menu selected

Speech transcript

Digits pressed

IP address

Timestamp

Auto-refreshes every 5 seconds.

📊 API Endpoints
✅ Health Check
GET /health


Returns uptime and call count.

📈 Stats
GET /api/stats


Returns:

Total calls

Menu distribution

Server uptime

📄 Logs
GET /api/logs?search=keyword


Returns latest IVR entries (open access for lab usage).

📞 Outbound Call Trigger

Start IVR call programmatically:

POST /call_user


Payload:

{ "to": "+919XXXXXXXXX" }


Server will call the number and route to IVR.

🔒 Security Notes

Twilio webhook signature validation is enabled

Admin dashboard is intentionally open for lab environments

For public deployments, add authentication and firewall rules

⚠️ Legal & Ethical Use

This project is intended only for:

Cybersecurity training labs

Telecom research

IVR testing environments

Awareness simulations

❌ Do NOT use for:

Surveillance

Phishing

Scam calls

Recording without consent

Always comply with:

Local telecom laws

Twilio Acceptable Use Policy

Data protection regulations

🧠 Future Roadmap

Planned or possible upgrades:

▶️ Call recording playback in dashboard

📊 Analytics charts and heatmaps

📁 Export logs to CSV/JSON

🧠 Speech intent classification

📞 Agent forwarding & call queues

🐳 Docker production deployment

👨‍💻 Community

Hackerseye Cyber Community
