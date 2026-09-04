#A tuple is essentially an immutable list. Once you create a tuple, you cannot add, remove, or change its elements.
# You define a tuple using parentheses () instead of square brackets [].


# A tuple of strings
coordinates = (40.7128, -74.0060)

# A tuple with mixed data types
user_profile = ("Asish", 25, True)

print(coordinates[0])  # Output: 40.7128 (Indexing works exactly like lists)
print(user_profile[1])

# A tuple representing a 3D point
point = (10, 20, 30)

# Unpacking into individual variables
x, y, z = point

print(x)  # Output: 10
print(y)  # Output: 20


#When to Choose a Tuple over a ListSince lists and tuples look so similar, here is the golden rule for choosing between them:
# Use a List when your data is a collection of the same item types that will grow, shrink, or change over time 
# (e.g., a list of users, shopping cart items, todo tasks).Use a Tuple when your data represents a single record with a fixed structure 
# where the position of each item has a specific meaning (e.g., an (x, y) coordinate, an (ip_address, port) pairing, a (year, month, day) date).

print("another example***")


# 1. DEFINE the function first
def full_emails(people):
    # This creates a new formatted string for every pair it loops through
    return [f"{name} <{email}>" for email, name in people]


# 2. CREATE your input data (a list containing tuples)
student_list = [
    ("alex@example.com", "Alex Diego"),
    ("shay@example.com", "Shay Brandt"),
    ("asish@example.com", "Asish Kumar")
]


# 3. CALL the function and store the result in a variable
formatted_emails = full_emails(student_list)


# 4. PRINT the result to see the output
print(formatted_emails)

# This will crash! because you cannot modify a tuple after created
#fruits_tuple = ("apple", "banana")
#fruits_tuple[0] = "kiwi"  # TypeError: 'tuple' object does not support item assignment

#If you want to create a tuple with only one item, you must include a trailing comma. Otherwise, Python just thinks it is a normal math parenthesis.
not_a_tuple = ("apple")   # Python sees this as just a string
is_a_tuple = ("apple",)   # The comma tells Python it's a tuple
