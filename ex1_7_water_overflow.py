# You have a watertankwith capacity of 255 liters. On the next n lines, you will receive 
# liters of water, which you have to pour in your tank. If the capacity is not enough, 
# print "Insufficient capacity!" and continue reading the next line. On the last line, 
# print the liters in the tank.

capacity = 255
quantity = 0
n = int(input())

for i in range(0, n):
    amount = int(input())
    if quantity + amount <= capacity:
        quantity = quantity + amount
    else:
        print("Insufficient capacity!")

print(quantity)
