Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
L = [10, 20, 30 40]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
L = [10, 20, 30, 40]
for X in L:
    print(X)

    
10
20
30
40
D = {'a' : 10, 'b' : 20, 'c':30, 'd':40}
for key in D:
    print(key, D[key])

    
a 10
b 20
c 30
d 40

= RESTART: C:/Users/Aditya Chavhan/Documents/PYTHON-50/REPEATITHON/SESSION-036/for-loop.py
10
20
30
40
A 100
B 1.1
abc xyz
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
L = [10, 20 30, 40]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
L = [10, 20, 30, 40]
10 in L1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    10 in L1
NameError: name 'L1' is not defined. Did you mean: 'L'?
10 in L
True
20 in L
True
30 in L
True
40 in L
True
30 in L
True
50 in L
False
L2  = ['xyz', 'pqr', 'lmn']
'xyz' in L2
True
'pqr' in L2
True
'lmn' in L2
True
'dhiraj' in L2
False
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'__iter__' in dir(list)
True
'__iter__' in dir(str)
True
'__iter__' in dist(touple)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    '__iter__' in dist(touple)
NameError: name 'dist' is not defined. Did you mean: 'dict'?
'__iter__' in dir(touple)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    '__iter__' in dir(touple)
NameError: name 'touple' is not defined. Did you mean: 'tuple'?
'__iter__' in dir(tuple)
True
'__iter__' in dir(dict)
True
'__iter__' in dir(set)
True
'__iter__' in dir(int)
False
'__iter__' in dir(bool)
False
'__iter__' in dir(float)
False
b  = True
type(b)
<class 'bool'>
n = 10
type(n)
<class 'int'>
f = 3.4
type(f)
<class 'float'>
s = 'Hello'
type(s)
<class 'str'>
L = [10, 20 , 30 , 40]
type(L)
<class 'list'>
T = (10, 20 ,30, 40)
type(T)
<class 'tuple'>
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd':40}
type(D)
<class 'dict'>
s = {10, 20, 30 , 40}
type(s)
<class 'set'>
for x in b:
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for x in b:
TypeError: 'bool' object is not iterable
for x in n:
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    for x in n:
TypeError: 'int' object is not iterable
for x in f:
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    for x in f:
TypeError: 'float' object is not iterable
for x in s:
    print(x)

    
40
10
20
30
str = 'Hello'
for x in str:
    print(x)

    
H
e
l
l
o
for x in L:
    print(x)

    
10
20
30
40
for x in T:
    print(x)

    
10
20
30
40
>>> for x in D:
...     print(x)
... 
...     
a
b
c
d
>>> for x in D:
...     print(x, D[x])
... 
...     
a 10
b 20
c 30
d 40
>>> #VERY ADVANCED
>>> L = [10, 20, 30, 40]
>>> for x in L:
...     print(x)
... 
...     
10
20
30
40
>>> I = L.__iter__()
>>> while True:
...     try:
...         x = I.__next__()
...         print(x)
...     except StopIteration:
...         break
... 
...     
10
20
30
40
