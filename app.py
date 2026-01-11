import os
import sqlite3
import requests
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, abort
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv

# ================= HACKER BANNER =================
BANNER = r"""
 █████   █████   █████████     █████████  █████   ████ ██████████ ███████████    ██  █████████             ██████████ █████ █████ ██████████
▒▒███   ▒▒███   ███▒▒▒▒▒███   ███▒▒▒▒▒███▒▒███   ███▒ ▒▒███▒▒▒▒▒█▒▒███▒▒▒▒▒███  ███ ███▒▒▒▒▒███           ▒▒███▒▒▒▒▒█▒▒███ ▒▒███ ▒▒███▒▒▒▒▒█
 ▒███    ▒███  ▒███    ▒███  ███     ▒▒▒  ▒███  ███    ▒███  █ ▒  ▒███    ▒███ ▒▒▒ ▒███    ▒▒▒             ▒███  █ ▒  ▒▒███ ███   ▒███  █ ▒ 
 ▒███████████  ▒███████████ ▒███          ▒███████     ▒██████    ▒██████████      ▒▒█████████  ██████████ ▒██████     ▒▒█████    ▒██████   
 ▒███▒▒▒▒▒███  ▒███▒▒▒▒▒███ ▒███          ▒███▒▒███    ▒███▒▒█    ▒███▒▒▒▒▒███      ▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒  ▒███▒▒█      ▒▒███     ▒███▒▒█   
 ▒███    ▒███  ▒███    ▒███ ▒▒███     ███ ▒███ ▒▒███   ▒███ ▒   █ ▒███    ▒███      ███    ▒███            ▒███ ▒   █    ▒███     ▒███ ▒   █
 █████   █████ █████   █████ ▒▒█████████  █████ ▒▒████ ██████████ █████   █████    ▒▒█████████             ██████████    █████    ██████████
▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒             ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒ 
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                   █████ █████   █████ ███████████                                          
                                                                  ▒▒███ ▒▒███   ▒▒███ ▒▒███▒▒▒▒▒███                                         
                                                                   ▒███  ▒███    ▒███  ▒███    ▒███                                         
                                                                   ▒███  ▒███    ▒███  ▒██████████                                          
                                                                   ▒███  ▒▒███   ███   ▒███▒▒▒▒▒███                                         
                                                                   ▒███   ▒▒▒█████▒    ▒███    ▒███                                         
                                                                   █████    ▒▒███      █████   █████                                        
                                                                  ▒▒▒▒▒      ▒▒▒      ▒▒▒▒▒   ▒▒▒▒▒                                         
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            

        >>> HACKERSEYE IVR CONTROL NODE <<<
        Cybersecurity | Telecom | Research Lab
        Authorized Access Only
"""

# ================= LOAD ENV =================
load_dotenv()

app = Flask(__name__)

# ================= CONFIG =================
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

DB_FILE = "hackerseye_ivr.db"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
validator = RequestValidator(TWILIO_AUTH_TOKEN)

# ================= RUNTIME STATS =================
START_TIME = time.time()
CALL_COUNT = 0
MENU_STATS = {"support": 0, "training": 0, "message": 0}

# ================= DATABASE =================
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS ivr_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caller TEXT,
            receiver TEXT,
            menu TEXT,
            digits TEXT,
            speech TEXT,
            confidence REAL,
            call_sid TEXT,
            ip TEXT,
            timestamp TEXT
        )
        """)
    print("[+] Database online")

def log_call(data):
    global CALL_COUNT
    CALL_COUNT += 1

    with sqlite3.connect(DB_FILE, check_same_thread=False) as conn:
        conn.execute("""
        INSERT INTO ivr_logs
        (caller, receiver, menu, digits, speech, confidence, call_sid, ip, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["caller"], data["receiver"], data["menu"], data["digits"],
            data["speech"], data["confidence"], data["call_sid"], data["ip"],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    print(f"[LOG] {data['menu']} | {data['caller']} | {data['speech'][:50]}")

# ================= SECURITY =================
def validate_twilio():
    sig = request.headers.get("X-Twilio-Signature", "")
    url = PUBLIC_BASE_URL + request.path
    if not validator.validate(url, request.form, sig):
        print("[!] BLOCKED: Invalid Twilio Signature")
        abort(403)

# ================= TELEGRAM =================
def send_telegram(msg):
    if not TELEGRAM_BOT_TOKEN:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": ADMIN_CHAT_ID, "text": msg}, timeout=5)
    except:
        print("[!] Telegram alert failed")

# ================= HEALTH =================
@app.route("/health")
def health():
    uptime = int(time.time() - START_TIME)
    return jsonify({
        "status": "online",
        "uptime_sec": uptime,
        "calls_logged": CALL_COUNT
    })

# ================= STATS =================
@app.route("/api/stats")
def stats():
    uptime = int(time.time() - START_TIME)
    return jsonify({
        "uptime_sec": uptime,
        "total_calls": CALL_COUNT,
        "menu": MENU_STATS
    })

# ================= OUTBOUND CALL =================
@app.route("/call_user", methods=["POST"])
def call_user():
    data = request.get_json(silent=True) or request.form
    to = data.get("to")

    if not to:
        return {"error": "missing number"}, 400

    call = client.calls.create(
        to=to,
        from_=TWILIO_NUMBER,
        url=f"{PUBLIC_BASE_URL}/voice",
        record=True
    )

    print(f"[+] Outbound call launched → {to}")
    return {"success": True, "sid": call.sid}

# ================= IVR =================
@app.route("/voice", methods=["POST"])
def voice():
    validate_twilio()
    print("[IVR] Entry point triggered")

    resp = VoiceResponse()
    gather = Gather(input="dtmf speech", finishOnKey="#", action="/menu", method="POST")
    gather.say(
        "Welcome to Hackerseye secure voice gateway. "
        "Press 1 for support. Press 2 for cyber training. "
        "Press 3 to leave a message. Then press pound.",
        voice="alice"
    )
    resp.append(gather)
    resp.say("No input detected. Disconnecting.", voice="alice")
    return Response(str(resp), mimetype="text/xml")

@app.route("/menu", methods=["POST"])
def menu():
    validate_twilio()
    choice = request.form.get("Digits", "")
    print(f"[IVR] Menu selection → {choice}")

    resp = VoiceResponse()

    if choice == "1":
        MENU_STATS["support"] += 1
        resp.say("Describe your support issue and press pound.", voice="alice")
        resp.append(Gather(input="speech dtmf", finishOnKey="#", action="/record/support", method="POST"))

    elif choice == "2":
        MENU_STATS["training"] += 1
        resp.say("Training division notified. Goodbye.", voice="alice")
        resp.hangup()

    elif choice == "3":
        MENU_STATS["message"] += 1
        resp.say("Leave your message after the tone and press pound.", voice="alice")
        resp.append(Gather(input="speech dtmf", finishOnKey="#", action="/record/message", method="POST"))

    else:
        resp.say("Invalid command. Session terminated.", voice="alice")
        resp.hangup()

    return Response(str(resp), mimetype="text/xml")

@app.route("/record/<menu>", methods=["POST"])
def record(menu):
    validate_twilio()

    data = {
        "caller": request.form.get("From", ""),
        "receiver": request.form.get("To", ""),
        "menu": menu,
        "digits": request.form.get("Digits", ""),
        "speech": request.form.get("SpeechResult", ""),
        "confidence": request.form.get("Confidence", ""),
        "call_sid": request.form.get("CallSid", ""),
        "ip": request.headers.get("X-Forwarded-For", request.remote_addr)
    }

    log_call(data)

    send_telegram(
        f"HACKERSEYE IVR\nMenu: {menu}\nCaller: {data['caller']}\nSpeech: {data['speech']}"
    )

    resp = VoiceResponse()
    resp.say("Payload received. Disconnecting.", voice="alice")
    resp.hangup()
    return Response(str(resp), mimetype="text/xml")

# ================= ADMIN =================
@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/api/logs")
def api_logs():
    search = request.args.get("search", "")
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute("""
        SELECT * FROM ivr_logs
        WHERE caller LIKE ? OR speech LIKE ? OR digits LIKE ?
        ORDER BY id DESC LIMIT 300
        """, (f"%{search}%", f"%{search}%", f"%{search}%"))
        logs = [dict(row) for row in cur.fetchall()]
    return jsonify(logs)

# ================= MAIN =================
if __name__ == "__main__":
    print(BANNER)
    print("[*] Booting Hackerseye IVR Core...")
    init_db()
    print("[*] Awaiting connections...\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
