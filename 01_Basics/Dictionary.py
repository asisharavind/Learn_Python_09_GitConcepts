file_counts = {"csv":10, "jpg":12, "py":15, "shr":20}
print(file_counts)

print(file_counts["shr"])

print("py" in file_counts)

print("txt" in file_counts)

file_counts["txt"] = 8

print(file_counts)

file_counts["jpg"] = 25 #will update the value for the existing key.

print(file_counts)

del file_counts["py"]
print(file_counts)

print("******iteration in dictionaries**********************")

for extnsion in file_counts:
    print(extnsion)#this would print keys only

for keys in file_counts.keys():
    print(keys)#this would also print keys only

for values in file_counts.values():
    print(values)#this would print values only

for ext,amount in file_counts.items():
    print(f"key is : {ext} and value is {amount}")#this would print keys and values

print("******another example**********************")

key = 'banana'
if key in file_counts:
	print(f"The value of {key} is {file_counts[key]}")
else:
	print(f"{key} is not found in the dictionary")

##DIDNT UNDERSTAND THE BELOW
key = 'csv'
if key in file_counts:
	print(f"The value of {key} is {file_counts[key]}")
else:
	print(f"{key} is not found in the dictionary")


keys_to_check = ['csv', 'png', 'txt']  # A list of keys to look up

# Loop through each key in the list
for key in keys_to_check:
    if key in file_counts:
        print(f"The value of {key} is {file_counts[key]}")
    else:
        print(f"{key} is not found in the dictionary")
file_counts = {'csv': 5, 'txt': 2}
keys_to_check = ['csv', 'png', 'txt']  # A list of keys to look up

# Loop keeps running as long as there are items left in the list
while len(keys_to_check) > 0:
    key = keys_to_check.pop(0)  # Get and remove the first key from the list
    
    if key in file_counts:
        print(f"The value of {key} is {file_counts[key]}")
    else:
        print(f"{key} is not found in the dictionary")
