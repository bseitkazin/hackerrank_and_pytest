s = input()
up = []
low = []
num1 = []
num0 = []
for i in s:
	if i.isdigit():
		if int(i) % 2:
			num1.append(i)
		else:
			num0.append(i)
	elif i.isupper():
		up.append(i)
	else:
		low.append(i)
up.sort()
low.sort()
num1.sort()
num0.sort()
print(*low, *up, *num1, *num0, sep = "")