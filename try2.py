#  using if else

print('==== calculator ====')

print('In build operations -\n'
    '1.Addition\n'
    '2.Subtraction\n'
    '3.Multiplication\n'
    '4.Division\n'
)

choice = int(input('Enter your choice: '))

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

if choice == 1:
    print(f'The addition of {x} and {y} is {x+y}')

elif choice == 2:
    print(f'The subtraction of {x} and {y} is {x-y}')

elif choice == 3:
    print(f'The multiplication of {x} and {y} is {x*y}')

elif choice == 4:
    print(f'The division of {x} and {y} is {x/y}')

else:
    print('Invalid number')    
    
