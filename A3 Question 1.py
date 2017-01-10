'''Part A: This code will yield all numbers between 100 and 200 (inclusive)
are divisible by 25.'''

#******************* Part A *******************
for i in range (100,201):
    if i%25==0:
        print (i,"Running loop Part A")

#******************* Part B *******************
''' Part B: This code will print a rectangle made of stars if the number of
rows is between 1 and 30 and the number of columns is between 1 and 20.'''

col = int(input("How many columns? "))
row = int(input("How many rows? "))
while (col < 0 or col> 30) or (row < 0 or row > 20):
	col = int(input("How many columns? "))
	row = int(input("How many rows? "))

#Print the square and make sure to end the function with ''
for i in range(row): 
	print("\n")
	for j in range(col):
		print('*',end=" ")

#******************* Part C *******************
'''Part C: This code will ask the user to enter a number greater than 10 and
print the sum of all of the numbers, until a user enters a number less than 10.'''
numberInput = 11
while numberInput > 10:
    numberInput = int(input("The sum of the values from 10 to the number entered will be printed.Enter a number greater than 10."))
    total = 0
    for i in range (10,numberInput):
        total += i
    if total != 0:
        print (total)


