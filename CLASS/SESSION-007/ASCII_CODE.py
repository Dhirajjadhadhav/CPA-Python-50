#The ord() function in Python is a built-in function that takes a single Unicode character as input and returns its corresponding integer Unicode code point. 
ord('A')

z = 500
print(z)

print('z')

# code the print all the printtable char ans ascii value
print('print all the printtable char ans ascii value')
s = "   ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()-_=+{[]};\'\"/?.>,<"

for c in s:
    print(c, ord(c), sep='\t')

# code the print all the printtable char ans ascii value and binary 
print("print all the printtable char ans ascii value and binary ")

for c in s:
    print(c, ord(c), bin(ord(c))[2:], sep='\t')


#  bin() function in Python is a built-in function used to convert an integer into its binary representation. It returns a string prefixed with 0b to indicate that the string represents a binary number.

# [2:] gives the binary from the 2 nd  bit as first 2 bit gives s the first (ob) represent the number is in binary number system