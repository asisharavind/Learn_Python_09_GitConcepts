def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

replace_domain("aaravind@cognizant.com","cognizant.com","costco.com")
#Strings can be initialized within single or double quotes
firstName = "Asish" #double quotes
lastName = 'Aravind' #single quotes
print(f"first name is {firstName} and last name is {lastName}")

#string multiplier
print("example" * 3)

#length function
print(f"length of my first name is : {str(len(firstName))}")

#get Index of a letter in a string
print("4th index in my first name is : " + firstName[4])

#get last index of a string
randomString = "random string with lot of characters"
print("last position of given string " +  randomString[-1])
print("second last position of given string " +  randomString[-2])

#substring or slice of string
fruit = "pineapple"
print(fruit[0:6])
print(fruit[:4])
print(fruit[4:])

#.index of
message = "cats & dogs"
print(f"index of & in {message} is : " + str(message.index('&')))

# - in - 
print("dragons" in message)
print("cats" in message)
print("dog" in message)

#upper and lower case handling
text = " Mountains "
print(text.upper())
print(text.lower())
print(text.lower().strip())
print(text.lower().lstrip())
print(text.lower().rstrip())

#count
print("number of times n occur in Mountains is : " + str(text.count("n")))
#ends with
print(text.endswith("ain"))
print(text.endswith("ains "))

#isNuumeric()
print(text.isnumeric())
print(text.isalpha())
print(" ".isspace())
print(" ".join(["This","is","a","sentence","  now"]) )

car_make = "Lamborghini"
print(car_make[3:-5])#bor
print(car_make[-4:])#hini
print(car_make[:7])#Lamborg