n1 = int(input('Enter numer1:'))
n2 = int(input('Enter numer2:'))
operation = int(input("Press 1 for add, 2 for substraction:"))

if operation == 1:
    result = n1 + n2
    print('Addition Result:',result)
elif operation  == 2:
    result = n1 - n2
    print('Substractio Result:', result)
else:
    print('Wrong Operation code:')
