Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
L1 = []
print(L1)
[]
id(L1)
1430807663168
type(L1)
<class 'list'>
len(L1)
0
#Create a list with some data
L2 = [10, 20, 30 , 40, 50]
print(L2)
[10, 20, 30, 40, 50]
type(L2)
<class 'list'>
id(L2)
1430763184256
len(L2)
5
#Creating list with diffrernt data elemt at each index
L3 = [True, 10, 3.14, "Hello"]
print(L3)
[True, 10, 3.14, 'Hello']
type(L3)
<class 'list'>
id(L3)
1430807762240
len(L3)
4
L3[0]
True
type(L3[0])
<class 'bool'>
L3[1]
10
type(L3[1])
<class 'int'>
L3[2]
3.14
type(L3[2])
<class 'float'>
\
L3[3]
'Hello'
type(L3[3])
<class 'str'>
# How to insert nw data into the list object
#create an empty list
L = []
print(L)
[]
len(L)
0
L.append(10) # Function applied to the objet must be defined in the class of theobject
>>> print(L)
[10]
>>> # Problem: Let L be the followig list
>>> # L = [True, 10, False, 20]
>>> L.append(10) # Function applied to the objet must be defined in the class of theobject
>>> print(L)
[10, 10]
>>> # object on whcih function is applied is passed as the first actual parameter
>>> #L.append(10) == list.append(L, 10)
>>> 
>>> #Problem: let L be the follwing list
>>> # L = [True, 10, False, 20]
>>> # visit list L element by element and print them using while loop
>>> i = 0
>>> while i< len(L):
...     print(i, L[i])
...     i = i+1
... 
...     
0 10
1 10
>>> #We did not initialize L to [True, 10, False, 20]> the vaiable L was naming list object contains [10, 10]
>>> # That explains the above output
>>> # Let solve the problem again, This time we will start with initializing the list
>>> L = [True, 10, False, 20]
>>> i = 0
>>> while i< len(L):
...     print(i, L[i])
...     i = i + 1
... 
...     
0 True
1 10
2 False
3 20
