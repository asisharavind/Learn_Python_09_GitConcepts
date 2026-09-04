#A List [] is a mutable, changeable collection of items.
#A Tuple () is an immutable, unchangeable collection of items.
# enumerate() is not a collection storage container. It is a built-in Python tool (a function) that takes a list or tuple 
# and automatically numbers each item as you loop through it.
#

fruits = ["apple", "banana", "mango"]
for index1, item1 in enumerate(fruits): # 'index' is the number (0, 1, 2...) and # 'item' is the actual value from the list
    print(f"{index1}: {item1}")

