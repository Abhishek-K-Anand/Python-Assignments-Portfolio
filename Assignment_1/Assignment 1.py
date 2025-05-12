#Basic Mathematical Operations

a  = int(input("Enter the first no. = "))
b  = int(input("Enter the second no. = "))

addition = a + b
subtraction = a - b
multiplication = a * b

if b != 0:
    division = a / b
else :
    division = "can't divide by zero"


print(f'Addition Results :{a} + {b} = {addition}')
print(f'subtraction Results :{a} - {b} = {subtraction}')
print(f'multiplication Results :{a} * {b} = {multiplication}')
print(f'division Results :{a} / {b} = {division}')

print("=====================================================================================")

# Create a Personalized Greeting

first_name = input("Enter first name : ")
last_name = input("Enter last name : ")

print(f'Hello,{first_name} {last_name}! Good morning,Welcome to my group.')