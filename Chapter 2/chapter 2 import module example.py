#this commented out program is included as an example focused on for loops
#I'm not sure why the third line writes + str(i) + , but when '+' isn't included it has syntax errors
#I noticed chapter 1.py has + str(int(myAge) + 1) + so it might be a required condition

# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

#another program that would print out 5 random integers
#the range would be from 1 to 10

import random
for i in range(5):
    print(random.randint(1, 10))