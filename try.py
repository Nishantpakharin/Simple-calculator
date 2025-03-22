# Raw idea

def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multipication(x,y):
    return x * y
def division(x,y):
    return x / y

x = int(input("Enter the first number: "))
y = int(input('Enter the second number: '))

a = addition(x,y)
s = subtraction(x,y)
m = multipication(x,y)
d = division(x,y)

print(f'The Addition of {x} and {y} is {a}')
print(f'The Subtraction of {x} and {y} is {s}')
print(f'The Multiplication of {x} and {y} is {m}')
print(f'The Division of {x} and {y} is {d}')