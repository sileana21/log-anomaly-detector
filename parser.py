def parse_log(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) < 5:
                continue

            log_entry = {
                "timestamp": parts[0] + " " + parts[1],
                "user": parts[2],
                "status": parts[3],
                "ip": parts[4],
            }

            logs.append(log_entry)

    return logs