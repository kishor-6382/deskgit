number=int(input("enter the number"))
if number%2==0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
string=input("enter name")
if string[::]==string[::-1]:
    print("yes it is palindrome")