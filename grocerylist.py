import sys
import math

# The problem given uses an input of a shopping list, and asks for the cost


#at the end of the day, what this code essientially does is takes items in a list, then places all items and their costs into a dictionarythe 

n = int(input())
Item_and_Price = {}
MyList = []
final =0
for i in range(n):
    _list = input()
    MyList.append(_list)
c = int(input())
for i in range(c):
    inputs = input().split()
    item = inputs[0]
    cost = int(inputs[1])
    Item_and_Price[item] = cost

for z in MyList: #for each item in the grocery list (MyList)
    if z in Item_and_Price: #if the item is in the dictionary of items and their prices
        final += Item_and_Price[z] #add item's cost aka value  to final total

print(final)
