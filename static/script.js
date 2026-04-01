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

        list.appendChild(item);

    });

});