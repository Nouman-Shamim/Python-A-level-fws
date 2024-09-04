number1=input("Enter First Number:")
number2=input("Enter Second Number:")
number3=input("Enter Third Number:")
if number1>number2:
  largest=number1
else:
    largest=number2
    if number2>number3:
      largest=number2
    else:
        largest=number3
        if number1>number3:
            largest=number1
        else:
            largest=number3
print("The largest number is:", largest)
