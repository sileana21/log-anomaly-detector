from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from parser import parse_log
from detector import detect_failed_logins, detect_off_hours
from database import insert_alert, get_all_alerts


app = FastAPI()

# Enable static file serving
app.mount("/static", StaticFiles(directory="static"), name="static")

# Enable template rendering
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


@app.get("/alerts")
def get_alerts():

    logs = parse_log("logs/auth.log")

    detected_alerts = []

    # Run anomaly detection rules
    detected_alerts.extend(detect_failed_logins(logs))
    detected_alerts.extend(detect_off_hours(logs))

    # Store alerts in database
    for alert in detected_alerts:
        insert_alert(alert)

    # Return alerts from database
    return get_all_alerts()