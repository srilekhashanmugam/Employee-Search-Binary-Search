const employees = [
    { id: 101, name: "Anita" },
    { id: 104, name: "Kumar" },
    { id: 108, name: "Sneha" },
    { id: 112, name: "Vikram" },
    { id: 116, name: "Rahul" },
    { id: 120, name: "Priya" },
    { id: 125, name: "Arjun" }
];

function searchEmployee() {

    const target = Number(
        document.getElementById("empId").value
    );

    let low = 0;
    let high = employees.length - 1;

    while (low <= high) {

        const mid = Math.floor((low + high) / 2);

        if (employees[mid].id === target) {

            document.getElementById("result").innerHTML =
                "Employee Found<br><br>" +
                "Employee ID: " + employees[mid].id +
                "<br>" +
                "Employee Name: " + employees[mid].name;

            return;
        }

        if (employees[mid].id < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    document.getElementById("result").innerHTML =
        "Employee Not Found";
}