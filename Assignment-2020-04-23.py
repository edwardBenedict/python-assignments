name = input('Enter your name?: ').title()

if name == "Joseph" :
    message = "Hello, {userName}! The password id : @12".format(userName=name)
else:
    message = "Hello, {userName}! See you later.".format(userName=name)

print(message)