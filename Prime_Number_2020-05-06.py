print("WELCOME TO PRIME NUMBER CREATERS")
limit = int(input("What is your limit to create prime number? "))
prime_numbers = []

for num in range(2,limit):
    if all(num%i!=0 for i in range(2,num)):
       prime_numbers.append(num)


print("Prime Numbers until ", limit, "=>", prime_numbers)

# Desired output : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
