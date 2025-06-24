# PART I
# ----1
s = int(input("Start of the range? > "))
e = int(input("End of the range? > "))

for i in range (s, e+1):
	if i % 7 == 0:
		print(i)

# ----2
s = int(input("Start of the range? > "))
e = int(input("End of the range? > "))

print("All numbers in the range: ")
for i in range(s, e + 1):
	print(i, end='')
	print(" ", end='')

print("\nAll numbers in the decreasing order in the range: ")
for i in range(e, s - 1, -1):
	print(i, end='')
	print(" ", end='')

print("\nAll numbers that can be divided by 7: ")
n = 0
for i in range(s, e + 1):
	if i % 7 == 0:
		print(i, end='')
		print(" ", end='')
	if i % 5 == 0:
		n += 1
print(f"There are also {n} numbers that are divisible by 5 in this range.")

# ----3
s = int(input("Start of the range? > "))
e = int(input("End of the range? > "))

for i in range(s, e + 1):
	if i % 3 == 0 and i % 5 != 0:
		print("Fizz")
	elif i % 3 != 0 and i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0 and i % 5 == 0:
		print("Fizz Buzz")
	else:
		print(i)

# ----4
b = int(input("Start of the range? > "))
e = int(input("End of the range? > "))
s = int(input("Step? > "))
w = int(input("How should the range be presented? 1 for regular way, 2 to print backwards."))

if w == 1:
	for i in range(b, e+1, s):
		print(i)
elif w == 2:
	for i in range(e, b-1, s):
		print(i)
    
# ----5
s = int(input("Start of the range? > "))
e = int(input("End of the range? > "))
p = 1
f = False

if s>e:
	for i in range(s, e+1):
		if i%4==0 and i%6!=0:
			p *= i
			f = True
elif e<s:
	for i in range(s, e+1):
		if i%4==0 and i%6!=0:
			p *= i
			f = True
if not f:
	print("There are no numbers that are divisible by 4 and not divisible by 6.")
  
# ----6
n = int(input("Enter the number > "))
e = int(input("Enter the exponent > "))
p = 1

for i in range(e):
	p*=n
print(p)

# PART II
# ----1
s = int(input("Enter the starting number > "))
e = int(input("Enter the end number > "))
sumeven, sumodd, sumc9 = 0, 0, 0
numev, numodd, numc9 = 0, 0, 0

for i in range(s, e+1):
	if i % 2 == 0:
		sumeven+=i
		numev+=1
	elif i % 2 != 0:
		sumodd+=i
		numodd += 1
	if i % 9 == 0:
		sumc9 += i
		numc9 += 1

print(f"Sum of even numbers in range from {s} to {e} is {sumeven}.")
print(f"Average of these is {sumeven//numev}")
print()
print(f"Sum of odd numbers in range from {s} to {e} is {sumodd}.")
print(f"Average of these is {sumodd//numodd}")
print()
print(f"Sum of numbers divisible by 9 in range from {s} to {e} is {sumc9}.")
print(f"Average of these is {sumc9//numc9}")

# ----2
l = int(input("Enter the column height > "))
s = input("What's the symbol you would like to use to build the column? > ")

for i in range(l):
	print(s)
# ----3
while True:
	n = int(input("Enter any number (enter 7 to stop) > "))
	if n==7:
		print("Good bye!")
		break
	elif n>0:
		print("Number is positive")
	elif n<0:
		print("Number is negative")
	elif n==0:
		print("Number is equal to zero")
# ----4
numbers = [ ]
n = None

while not n == 7:
	n = input("Enter number - \"s\" to stop and count, 7 to quit the program. > ")
	if not n.lower().startswith("s"):
		if int(n) == 7:
			print("Good bye!")
			break
		numbers.append(int(n))
	elif n.lower().startswith("s"):
		print(f"Sum of numbers you entered is {sum(numbers)}.")
		print(f"Biggest of numbers you entered is {max(numbers)}.")
		print(f"Smallest of numbers you entered is {min(numbers)}.")

# ----5
n = int(input("Enter the number > "))
divisibility_cases_number = 0

if n <= 1:
	print("Number must be larger than 1.")
	exit()

for i in range(1, n + 1):
	if n % i == 0:
		divisibility_cases_number += 1

if divisibility_cases_number == 2:
	print("The number you typed is prime!")
else:
	print("The number you typed is NOT prime!")

# !!! я іду легшими шляхами відомими для мене, лол !!! #
# ----6
n = int(input("Enter the number > "))
a, b = 0, 1

while not b>n:
	if n == a or n == b:
		print("Your number is present in fibonacci order!")
		exit()
	else:
		a, b = b, a + b
		
print("Your number is NOT present in fibonacci order!")
