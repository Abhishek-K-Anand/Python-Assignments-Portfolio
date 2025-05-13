def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

num = int(input("Enter a number : "))
factorial = fact(num)
print(f'factorial of {num} is : {factorial}')

print("=====================================================================")

import math

n = int(input("enter a number : "))

if n < 0:
    print("Square root  and logarithmic of negative value is not possible")

else:
    square_root = math.sqrt(n)
    log_value = math.log(n)
    print(f'Square root of {n} is : {square_root}')
    print(f'logarithmic of {n} : {log_value}')


sine_value = math.sin(n)
print(f'sine_value of {n} is : {sine_value} ')

