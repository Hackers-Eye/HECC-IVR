🛡️ Hacker'S-Eye IVR Control Node

Aggressive-style, lab-grade Interactive Voice Response (IVR) system built with Flask + Twilio, designed for cybersecurity training, telecom research, and authorized simulations.

This project provides a hacker-themed control panel, call logging, speech + DTMF capture, real-time monitoring, and outbound call triggering — all in a minimal single-file backend.

🚀 Features

☎️ Twilio-based IVR system

🎯 Multi-level menu (Support / Training / Message)

🔢 DTMF + 🎤 Speech input

📞 Call recording enabled

🗃️ SQLite call logging

📊 Runtime stats API

🔔 Telegram alerts

🧠 Menu analytics counters

🖥️ Hacker-style Admin Dashboard

🔥 Aggressive ASCII branding

📁 Project Structure (Minimal)
hackerseye-ivr/
│
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── admin.html


No extra services, no blueprints — fast to deploy and easy to modify.

⚙️ Requirements

Python 3.9+

Twilio account (trial or paid)

Internet access (for Twilio webhooks)

📦 Installation
1️⃣ Clone or Download
git clone https://github.com/yourname/hackerseye-ivr.git
cd hackerseye-ivr

2️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Configuration

Create a file named .env in project root:

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

Server runs on:

http://localhost:5000

🌐 Expose Public URL (Required for Twilio)

Twilio must reach your server over HTTPS.

Option A — Using ngrok
ngrok http 5000


Copy HTTPS URL and update:

PUBLIC_BASE_URL=https://xxxx.ngrok-free.app


Restart server after updating .env.

☎️ Twilio Webhook Setup

In Twilio Console:

Voice → Phone Numbers → Your Number

Set:

When a call comes in:
Webhook
POST
https://xxxx.ngrok-free.app/voice


Save configuration.

🧑‍💻 Admin Dashboard

Open in browser:

http://localhost:5000/admin


Dashboard shows:

Caller number

Menu selected

Speech text

Digits pressed

IP address

Timestamp

Auto refresh every 5 seconds.

📊 APIs
🔹 Health Check
GET /health


Returns uptime and call count.

🔹 Stats
GET /api/stats


Returns menu usage counters.

🔹 Logs
GET /api/logs?search=keyword


Returns recent call logs (open access for lab use).

📞 Outbound Call API

Trigger IVR call to any number:

POST /call_user


Form or JSON body:

{ "to": "+919xxxxxxxxx" }


Server will place a call and route to IVR.

⚠️ Legal & Ethical Use

This project is intended for:

Cybersecurity labs

Telecom research

IVR testing

Awareness training simulations

❌ Do NOT use for:

Harassment

Surveillance

Phishing

Scam calls

Recording without consent

Always comply with:

Local telecom laws

Twilio Terms of Service

Consent requirements

🧠 Roadmap (Optional Upgrades)

Future expansions you can add:

▶️ Play call recordings in dashboard

📈 Call analytics graphs

📁 Export logs to CSV

🧠 Speech keyword classification

📞 Agent forwarding system

🐳 Docker deployment

👨‍💻 Author

Hackerseye Cyber Community
KRISH GHOSH
