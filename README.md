

It is professional, clear, and structured for maximum visibility and understanding by developers and collaborators.

---

```markdown
# HECC-IVR

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Twilio](https://img.shields.io/badge/twilio-supported-red)](https://www.twilio.com/)

**Hackers Eye Cyber Community — Interactive Voice Response (IVR) System**

A powerful, hacker-themed IVR platform built with Flask and Twilio for cybersecurity labs, telecom research, and authorized simulations. It features multi-level voice menus, DTMF + speech capture, call recording, real-time logging, and an aggressive hacker-style admin dashboard.

---

## 📌 Features

- ☎️ Multi-level IVR with menu routing
- 🧠 DTMF and speech input capture
- 📞 Outbound call trigger API
- 🗂 SQLite call logging
- 🖥️ Live admin dashboard
- 📊 Runtime and menu analytics
- 📡 Telegram alerts
- 🔥 Hacker-style ASCII branding

---

## 📁 Repository Structure

```

HECC-IVR/
│
├── app.py                       # Main IVR + admin server
├── requirements.txt             # Dependencies
├── README.md                   # Project documentation
└── templates/
└── admin.html               # Admin dashboard UI

````

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/Hackers-Eye/HECC-IVR.git
cd HECC-IVR
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

Create a file `.env` with:

```
TWILIO_ACCOUNT_SID=ACXXXXXX
TWILIO_AUTH_TOKEN=XXXXXX
TWILIO_NUMBER=+1XXXXXXX
PUBLIC_BASE_URL=https://yourpublicurl.ngrok.app

TELEGRAM_BOT_TOKEN=XXXXXX
ADMIN_CHAT_ID=XXXXXX
```

---

## 🧠 Run Server

```bash
python app.py
```

By default, the server listens on:

```
http://localhost:5000
```

---

## 🌍 Public URL

Twilio requires a public HTTPS endpoint. Use ngrok:

```bash
ngrok http 5000
```

Update `PUBLIC_BASE_URL` in `.env` accordingly.

---

## ☎️ Twilio Webhook Setup

In the Twilio Console, set your number’s Voice webhook:

```
POST        https://your-ngrok-url/voice
```

---

## 🖥️ Admin Dashboard

Open:

```
http://localhost:5000/admin
```

Search and monitor calls in real time.

---

## 📊 API Endpoints

| Route            | Purpose                    |
| ---------------- | -------------------------- |
| `/voice`         | IVR entry webhook (Twilio) |
| `/menu`          | IVR menu routing           |
| `/record/<menu>` | Save input                 |
| `/call_user`     | Trigger outbound call      |
| `/api/logs`      | Fetch call logs            |
| `/api/stats`     | Runtime stats              |
| `/health`        | Server health              |

---

## 📞 Outbound Call API

Invoke IVR on any number:

```
POST /call_user
```

Body (form or JSON):

```json
{ "to": "+919xxxxxxxxx" }
```

---

## 📌 Notes

* Designed for research, labs, training, and authorized use.
* Do **not** use for harassment, unauthorized recording, or illegal activities.
* Always adhere to local laws and Twilio terms.

---

## 🛠️ Roadmap

* 🎙️ Call playback in admin panel
* 📈 Dashboard analytics and charts
* 📁 Log export (CSV/JSON)
* 🤖 AI speech intent tagging
* 🚀 Docker deployment

---

## 📜 License

Distributed under the **MIT License**
See `LICENSE` for details.

---

## 📣 Contributing

We welcome contributions!
Please open issues and pull requests to improve features, security, and UX.

---

## 🔥 Join Hackers Eye

Connect with our cybersecurity community for labs, challenges, and collaborative projects.

```

---

If you’d like, I can also generate:

- A **LICENSE file** (MIT, Apache, GPL etc.)
- A **GitHub Actions CI workflow**
- A **project badge set**
- A **contributing template**
- A **demo GIF/hero image section**

Just let me know what you want next!
```
