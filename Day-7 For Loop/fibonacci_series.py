# Q. 4. Python program to get the Fibonacci series between 0 to 50 

# // Code

# Function to generate Fibonacci series up to n using a for loop
def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[i-1] + fib_series[i-2]
        if next_num < n:
            fib_series.append(next_num)
        else:
            break
    return fib_series

# Generate Fibonacci series up to 50
fib_series_50 = fibonacci_series(50)

# Print the Fibonacci series
print("Fibonacci series up to 50:")
print(fib_series_50)