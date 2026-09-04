for i in range(20):
    print(f"number {i}")

print("--- For Loop Countdown ---")
# This counts from 1 up to (but not including) 6
for number in range(1, 6):
    print(f"Counting: {number}")

print("--- While Loop Countdown ---")
countdown = 5

# This keeps running as long as countdown is greater than 0
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown = countdown - 1  # Reduces the count by 1 each time

print("Blast off! 🚀")

for number in range(1, 6+1, 2): #x = Start - Starting index position of the range,y = Stop - Ending index position of range,z = Step - Incremental value
    print(number * 3)

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = []
for x in range(7):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)