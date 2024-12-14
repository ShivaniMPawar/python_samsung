str1 = 'Karnataka'
print(str1.islower())
print(str1.isupper())
chars= [ char for char in str1]  # convert string to list
print(chars)

str2 = ''.join(chars)  #convert list to string
print(str2)