#Initializing list
x = ["my", "name", "is", "Asish"] #elements in a list 
print(x[3])

print(len(x)) #length of a list


print("*******************************************")
print("list")
print("*******************************************")

fruits = ["banana", "grapes", "watermelon","apple","pear"]
print(fruits)
fruits.append("mango")
print(fruits)
fruits.insert(1,"kiwi")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits)

print("*******************************************")
print("iterating over list")
print("*******************************************")

y = ["my", "name", "is", "dwayne johnson"] #elements in a list 
for a in y: # iterating elements in a list
    print(a)

for a in y[1:3]: # printing specific elements in a list
    print(a)

# Loops through exactly index 1 and index 3
for a in [y[1], y[3]]:
    print(a)

animals = ["lion", "zebra", "dolphin", "monkey", "tiger"]
chars = 0
for animal in animals:
    chars+= len(animal)


print(f"total characters in animal list is {str(chars)} and average length is : {str(chars/len(animals))}")

print("*******************************************")

multiples = []
for x in range(1,10):
    multiples.append(x*7)
print(multiples)

print("*****List comprehension**************************************")
multiples = [x*7 for x in range(1,10)]
print(multiples)

languages = ["python", "pearl", "java", "csharp"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(1,100) if x%3==0]
print(z)

#for loops are for doing something. They tell Python a series of steps to take.
#List comprehensions are for making something. They describe what the final list should look like.