#accept 3 distinct numbers from the user and find biggest number
input_number1 = int(input("Enter 1st number:"))
input_number2 = int(input("Enter 2nd number:"))
input_number3 = int(input("Enter 3rd number:"))

if input_number1 > input_number2 and input_number1 > input_number3:
    print(f"{input_number1} is biggest number amoung other two")

elif input_number2 > input_number3:
    print(f"{input_number2} is biggest number amoung other two")

else:
    print(f"{input_number3} is biggest number amoung other two")
    
    