from fastapi import FastAPI
from parser import parse_log
from detector import detect_failed_logins

app = FastAPI()


@app.get("/alerts")
def get_alerts():
    logs = parse_log("logs/auth.log")
    alerts = detect_failed_logins(logs)
    return alerts