print('Start of program')

num = 100
result  = num
a = int(input('Enter an interger:'))

if a>0:
    print('Entered number is gretaer than 0')
    result = (num + 1) * a
elif a < 0:
    print('Entered number is less than 0')
    result  = (num-1) * a
else:
    print('Entered number is Zero')
    result = num * a
print('Result :', result)
print('End of program')
