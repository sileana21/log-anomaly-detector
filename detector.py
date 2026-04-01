from collections import defaultdict


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