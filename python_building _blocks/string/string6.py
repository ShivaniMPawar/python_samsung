'''Read as many strings as you wish from command line.Each string has 2 parts which are separated by space.The 1st part is name of the state and the 2nd part is its capital.Now create 2 lists named states and capitals.And store the states from the command line Args into states and similarily the capitals.Print the states and capitals data in a table format.Apply proper formatting to the o/p'''
import sys
print(sys.version)
import string
states = []
capitals = []

for i in range(1,len(sys.argv)):

    index_of_space = sys.argv[i].find(' ')
    states.append(sys.argv[i][:index_of_space])
    capitals.append(sys.argv[i][index_of_space+1:])
print('%-15s | %-15s|'%('States','Captial'))
print('-'* 34)
for i in range (len(sys.argv)-1):
    print('%-15s | %-15s |'%(states[i].capitalise(),capitals[i].capitalise))