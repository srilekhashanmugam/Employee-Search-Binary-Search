def binary_search(employees, target_id):
    low = 0
    high = len(employees) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = employees[mid][0]

        if mid_id == target_id:
            return employees[mid]

        elif mid_id < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# Sorted employee records
employees = [
    (101, "Anita"),
    (104, "Kumar"),
    (108, "Sneha"),
    (112, "Vikram"),
    (116, "Rahul"),
    (120, "Priya"),
    (125, "Arjun")
]

print("================================")
print("     EMPLOYEE SEARCH SYSTEM")
print("     Using Binary Search")
print("================================")

try:
    emp_id = int(input("Enter Employee ID: "))

    result = binary_search(employees, emp_id)

    if result:
        print("\nEmployee Found")
        print("Employee ID   :", result[0])
        print("Employee Name :", result[1])
    else:
        print("\nEmployee Not Found")

except ValueError:
    print("\nPlease enter a valid numeric Employee ID.")