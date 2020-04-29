number = input("Please enter a positive integer number _  ")
results = { 
    0: f'{number} is not an Armstrong number',
    1: f'{number} is an Armstrong number',
    2: 'Please enter a positive number',
    3: 'Please enter an integer number',
    4: 'Please enter numeric values'
    }
if number[0] == '-':
    print(results[2])
elif number.count(',') + number.count('.') != 0:
    print(results[3])
elif not number.isnumeric():
    print(results[4])
else:
    is_Armstrong = 0
    for i in number:
        is_Armstrong += int(i) ** len(number)
    print(results[is_Armstrong == int(number)])