
---

```markdown
# 🔥 HECC-IVR

## Hackers Eye Cyber Community — Interactive Voice Response (IVR) System

HECC-IVR is a hacker-themed, research-grade IVR platform built with **Flask + Twilio** for cybersecurity labs, telecom testing, authorized red-team simulations, and training environments.  
It supports multi-level voice menus, DTMF + speech input, call recording, outbound calling, real-time logging, and a live admin dashboard.

> ⚠️ For **authorized and legal use only**. Misuse may violate telecom and privacy laws.

---

## 🚀 Use Cases

- 📞 Telecom & VoIP research  
- 🧪 Cybersecurity lab simulations  
- 🎓 Training demos for IVR systems  
- 🛡️ Blue-team call flow testing  
- 📊 Call analytics experiments  

---

## ✨ Key Features

- ☎️ Multi-level IVR menu routing  
- 🧠 DTMF + speech recognition capture  
- 📞 Outbound call trigger API  
- 🗂 SQLite persistent call logs  
- 🖥️ Live hacker-style admin dashboard  
- 📊 Runtime statistics & menu analytics  
- 📡 Telegram alert integration  
- 🔥 ASCII hacker branding in backend logs  
- ⚡ Lightweight Flask deployment  

---

## 📁 Repository Structure

```

HECC-IVR/
│
├── app.py                 # Main Flask + Twilio IVR server
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── templates/
└── admin.html         # Admin dashboard UI

````

---

## ⚙️ Tech Stack

| Layer      | Technology |
|------------|------------|
| Backend    | Flask (Python) |
| Voice API  | Twilio Programmable Voice |
| Database   | SQLite |
| Frontend   | HTML + JS (Admin Panel) |
| Alerts     | Telegram Bot API |

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Hackers-Eye/HECC-IVR.git
cd HECC-IVR
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Recommended: use virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Environment Configuration

Create a `.env` file in project root:

```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxx
TWILIO_NUMBER=+1xxxxxxxxxx
PUBLIC_BASE_URL=https://your-ngrok-url.ngrok.app

TELEGRAM_BOT_TOKEN=xxxxxxxx
ADMIN_CHAT_ID=xxxxxxxx
```

⚠️ Never commit `.env` to GitHub.

### 4️⃣ Run Server

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🌍 Public URL for Twilio

Twilio requires **public HTTPS endpoints**.

Use **ngrok**:

```bash
ngrok http 5000
```

Update in `.env`:

```
PUBLIC_BASE_URL=https://xxxx.ngrok.app
```

Restart server after change.

---

## ☎️ Twilio Webhook Setup

In **Twilio Console → Phone Number → Voice Configuration**:

```
POST https://your-ngrok-url/voice
```

Content Type: `application/x-www-form-urlencoded`

---

## 🖥️ Admin Dashboard

Open in browser:

```
http://localhost:5000/admin
```

### Capabilities

* View live call logs
* Monitor menu flow
* See caller numbers and timestamps
* Future versions: playback + charts

---

## 📡 API Endpoints

| Endpoint         | Method | Description           |
| ---------------- | ------ | --------------------- |
| `/voice`         | POST   | IVR entry webhook     |
| `/menu`          | POST   | Menu routing          |
| `/record/<menu>` | POST   | Save user input       |
| `/call_user`     | POST   | Trigger outbound call |
| `/api/logs`      | GET    | Fetch call logs       |
| `/api/stats`     | GET    | Runtime statistics    |
| `/health`        | GET    | Health check          |

---

## 📞 Outbound Call API

### Endpoint

```
POST /call_user
```

### Body

```json
{
  "to": "+919xxxxxxxxx"
}
```

### Use Cases

* Automated alerts
* Training call flows
* Incident response drills

---

## 🔐 Security & Compliance

This project is built for:

* ✅ Authorized testing
* ✅ Training environments
* ✅ Legal research

Not allowed:

* ❌ Harassment
* ❌ Unauthorized recording
* ❌ Phishing
* ❌ Robocalling campaigns

Always comply with:

* Local telecom regulations
* * Data protection laws
* Twilio Acceptable Use Policy

---

## 🛠 Configuration Tips

* Use strong Twilio API tokens
* Restrict admin access behind VPN or authentication
* Do not expose admin panel publicly
* Rotate API credentials regularly

---

## 🧩 Roadmap

* 🎙️ Call playback in dashboard
* 📈 Graph-based analytics
* 📁 CSV / JSON log export
* 🔐 Admin authentication system
* 🤖 AI-based intent detection
* 🐳 Docker deployment support
* ☁️ Cloud hosting templates

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Submit Pull Request

All contributions are reviewed.

---

## 📜 License

Licensed under the **MIT License**
Free to use, modify, and distribute with attribution.

---

## 🔥 Hackers Eye Cyber Community

* Cybersecurity labs
* Red-team learning projects
* IoT security research
* Community CTF events

GitHub: [https://github.com/Hackers-Eye](https://github.com/Hackers-Eye)

---

```
```
