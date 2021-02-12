'''
Created on 12 Feb 2021

@author: clayb
'''

def addTwoValues(a, b):
    return a + b


def addFixedValue(a):
    y = 5
    return y + a


print("Did this make it to GitHub?...")

ansTwoVal = addTwoValues(1, 2)
print (ansTwoVal)

ansFixedVal = addFixedValue(7)
print(ansFixedVal)