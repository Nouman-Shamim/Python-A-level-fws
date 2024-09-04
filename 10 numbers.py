postive=0
negative=0
choice="y"
while choice=="y":
    num=int(input("Enter Number"))
    if num>=0:
        postive=postive+1
    else:
        negative=negative+1
    choice=input("Do you want to enter another number.y or N")
print("Postive Numbers are",postive)
print("Negative Numbers are",negative)
                               
