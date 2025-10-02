n1 = int(input('Enter number 1:'))
n2 = int(input('Enter number 2:'))
operation = int(input('Press 1 for addition, 2 for substraction:'))


if operation == 1:
    result = n1 + n2
    print('Result of additon is:',result)
elif operation == 2:
    result = n1 - n2
    print('Result of subtraction is:', result)
else:
    print('Invalid operation code')
