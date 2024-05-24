
# Q.4.Write a python program and iterate the given tuples
#     Input: employee1 = ("John Doe", 101, "Human Resources", 60000) 
#            employee2 = ("Alice Smith", 102, "Marketing", 55000) 
#            employee3 = ("Bob Johnson", 103, "Engineering", 75000)



# Define the employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Create a list of employee tuples for easy iteration
employees = [employee1, employee2, employee3]

# Iterate through each employee tuple
for employee in employees:
    # Unpack the tuple into individual variables for clarity
    name, id, department, salary = employee
    
    # Print the employee details
    print(f"Name: {name}, ID: {id}, Department: {department}, Salary: ${salary}")

# Alternatively, you could use the tuple index to access and print the elements
for employee in employees:
    print(f"Name: {employee[0]}, ID: {employee[1]}, Department: {employee[2]}, Salary: ${employee[3]}")
