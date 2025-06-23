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
