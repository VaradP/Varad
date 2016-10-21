a=input('Enter username: ')
print('The total number of characters in the username is',len(a))
if 'a' in a:
    print('The character A exists in the username')
else:
    print('Character A does not exist in the userame')
print('The reverse of the string is ')
z=0
while z <=(len(a)):
    print(a[len(a)-z:len(a)-z+1])
    z=z+1





