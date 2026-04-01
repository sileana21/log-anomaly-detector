from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from parser import parse_log
from detector import detect_failed_logins

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/alerts")
def get_alerts():
    logs = parse_log("logs/auth.log")
    alerts = detect_failed_logins(logs)
    return alerts

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )