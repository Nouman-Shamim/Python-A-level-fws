sample = int(input("Enter choice"))
 
match sample:
    case (1|2|3|4):
        print("It is a boolean value")
    case _ :
        print("Not a boolean value")
