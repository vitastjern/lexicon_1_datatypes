# Write a program to read an integer n and print all triples of the first n small 
# Latin letters, ordered alphabetically

n = int(input())

for i in range(0, n):
    for j in range (0, n):
        for k in range(0, n):
            print(chr(i+97) + chr(j+97) + chr(k+97))
