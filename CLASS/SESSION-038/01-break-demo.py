print('start of the program')
L = [10, 15, 20, 25, 42, 45, 70, 75, 77, 100]

print('For loop without break statement-START')
for x in L:
    print('Current Value of x :',x)
print('For loop without break statement-END')

print('For loop with break statement-START')
for x in L:
    if x%7 == 0:
        break;
    print('Current Value of x:', x)
print('For loop with break statement-END')

print(' end of program')
