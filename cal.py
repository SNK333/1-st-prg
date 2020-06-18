o=input("Enter the option :")
x,y=input("Enter 2 numbers :").split()
x=int(x)
y=int(y)
if o=="+" :
    print(x+y)
elif o=="-" :
    print(x-y)
elif o=="*" :
    print(x*y)
elif o=="/" :
    if y!=0 :
        print(x/y)
    else :
        print("Division not possible")
else :
   print("invalid input")
