s1 = 'Jamkhandi'
s2 = 'Dubai'
print(f'Before Swap : \n s1 = {s1} , s2 = {s2}')
s1, s2 = s2 , s1
#Implicitly a tuple is created and the RHS values is stored in it.And then the values from the tuple are copied one by one to the LHS variables 
print(f'After Swap : \n s1 = {s1} , s2 = {s2}')
