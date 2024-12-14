str1 = '  hubballi   jamkhandi  \t  '
print(str1.strip().capitalize(), '***')
print('Count of a =',str1.count('a'))
print('Count of a =',str1.count('a',12))
print('Count of a =',str1.count('a',11,15))

print('Index of h=',str1.index('h'))
print('Index of j=',str1.find('j'))
print('Index of a=',str1.index('j',10))
print('Index of m=',str1.index('m',11,23))
