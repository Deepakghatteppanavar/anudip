import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine full-time and part-time employee data
all_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

print("Comprehensive Employee Dataset:")
for employee in all_employees:
    print(f"Employee ID: {employee[0]}, Name: {employee[1]}, Type: {employee[2]}, Salary: {employee[3]}")
