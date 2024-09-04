def calc(n1,n2,op):
    result=0
    if op=="+":
        result=n1+n2
    elif op=="-":
        result=n1-n2
    elif op=="*":
        result=n1*n2
    return result
a=int(input("enter first number"))
b=int(input("enter second number"))
c=input("Enter Operator")
print(calc(a,b,c))

    
        
