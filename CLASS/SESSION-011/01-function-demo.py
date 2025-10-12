def TestFunction():
    print('This is a TestFunction() which does nothing apart from printing this msg')

print('Function with zero parameter')
print('-----------------------------------------------')
TestFunction()
TestFunction()
print('-----------------------------------------------')
# -------------------------------------------------------------
# Function with 1 formal parameter
def TestFunction1(param_1):
    print('Value of param_1:', param_1)
    print('Type of param_1:', type(param_1))
    print('Id of param_1:', id(param_1))

print('Function With one param')
print('-----------------------------------------------')
TestFunction1(1500)
TestFunction1(1.1)
TestFunction1('Dhiraj')
print('-----------------------------------------------')

# --------------------------------------------------------------
def TestFunction2(x, y):
    print('value of x:', x)
    print('Type of x', type(x))
    print('Id of x:', id(x))
    print('Value of y:', y)
    print('Type of x:', type(y))
    print('Id of y', id(y))

print('Function with two parameter')
print('-----------------------------------------------')
TestFunction2(100, 200)
TestFunction2(100, 1.1)
TestFunction2(100, 'Hello')
print('-----------------------------------------------')