# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.

n = int(input())
i = 0

letter_sum = 0

while i < n:
    letter_sum = letter_sum + ord(input())
    i += 1

print("The sum equals: " + str(letter_sum))
