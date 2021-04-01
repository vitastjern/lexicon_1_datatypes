# Write a program that prints part of the ASCII tableof characters on the console.  
# On the first line of input you will receive the char index you should start with and 
# on the second line - the index of the last character you should print.

first = int(input())
last = int(input())

letters = ""

for i in range(first, last+1):
    letters = letters + chr(i) + " "

print(letters)