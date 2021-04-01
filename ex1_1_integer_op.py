# Read four integer numbers. Add first to the second, divide (integer) the sum by the 
# third number and multiply the result by the fourth number. Print the result.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = ((a + b) // c) * d

print(result)
