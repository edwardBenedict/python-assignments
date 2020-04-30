print("WELCOME TO FIBONACCI SERIES GENERATOR")

fibonacci_series = []
for i in range(1, 11):
    if i == 1:
        fibonacci_series.append(i)
    elif i == 2:
        fibonacci_series.append(i-1)
    else:
        next = fibonacci_series[i-2]+fibonacci_series[i-3]
        fibonacci_series.append(next)

print("fibonacci → ", fibonacci_series)



# Desired Output => fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]