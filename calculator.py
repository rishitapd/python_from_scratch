first =int( input("Enter your first no.:"))
operator = input("enter the operator(+,-,*,%,/):")

second=int(input("enter"))

if operator=='+':
    print(first+second)
elif operator=='-':
    print(first-second)
elif operator=='*':
    print(first*second)
elif operator=='/':
    print(first/second)
elif operator=='%':
    print(first%second)
else:
    print("undefined")