# Calculate how many courses will be needed to elevate n persons by using an 
# elevator of capacity of p persons. 
# The input holds two lines:the number of people n and the capacity p of the elevator.
# (I find the use of the divmod useful here)

n = int(input())
p = int(input())

courses = divmod(n,p)

if courses[1] != 0: # last trip wont be at full capacity
    print(courses[0] + 1)  # the number of full courses + one thats not full
else:
    print(courses[0])      # the number of courses at full capacity, no remaining persons
