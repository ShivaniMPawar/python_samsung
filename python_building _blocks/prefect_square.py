#Accept a number and check if it is Prefect square
import math
n = int(input("Enter a number to check whether it is a prefect square : "))
# step 1
root = math.sqrt(n)
print("root in step 1:",root)
print(type(root))

#step 2  
root = math.floor(root)
print("root in step 2:",root)
print(type(root))

if root * root == n:
    print(f"{n} is a prefect square")

else:
    print(f"{n} is not a prefect square")
