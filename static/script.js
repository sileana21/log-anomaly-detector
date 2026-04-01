fetch("/alerts")
.then(response => response.json())
.then(data => {

    const list = document.getElementById("alerts");

    data.forEach(alert => {

        const item = document.createElement("li");

        item.textContent =
            alert.type + " | User: " +
            alert.user + " | Severity: " +
            alert.severity;

        // severity styling
        if (alert.severity === "MEDIUM") {
            item.style.color = "orange";
        }

        if (alert.severity === "HIGH") {
            item.style.color = "red";
        }

        if (alert.severity === "CRITICAL") {
            item.style.color = "darkred";
            item.style.fontWeight = "bold";
        }

        list.appendChild(item);

    });

});