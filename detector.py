from collections import defaultdict
from datetime import datetime


def detect_failed_logins(logs):

    failures = defaultdict(int)
    alerts = []

    for log in logs:

        if log["status"] == "FAILED":

            failures[log["user"]] += 1

            if failures[log["user"]] >= 3:

                alerts.append({
                    "type": "Repeated Failed Login",
                    "user": log["user"],
                    "severity": "MEDIUM"
                })

    return alerts


def detect_off_hours(logs):

    alerts = []

    for log in logs:

        timestamp = datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        if timestamp.hour < 5:

            alerts.append({
                "type": "Off-hours login",
                "user": log["user"],
                "severity": "HIGH"
            })

    return alerts