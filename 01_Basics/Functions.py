def sumOfTwoNum(a,b):
    print("sum of two numberrs: " + str(a+b))

def calculateBill(billAmount, tip_percent):
    tip = billAmount * (tip_percent / 100)
    totalBill = billAmount + tip   
    return totalBill

def biggerNumber(a, b):
    if a > b:
        print(f"a ({a}) is greater than b ({b})")
    elif a < b:
        print(f"b ({b}) is greater than a ({a})")
    else:
        print(f"Both numbers are equal! Both are {a}")

# Test the new condition
biggerNumber(10, 10)


sumOfTwoNum(2,3)
sumOfTwoNum(5,9)
myBill = calculateBill(100,5)

print("Total Bill amount to be charged is: " + str(myBill))

biggerNumber(12,12)

