n = int(input())
for i in range(n):
	s = input()
	dig = 0
	alpha = 0
	check = 0
	for j in s:
		if j.isdigit():
			dig += 1
		elif j.isupper():
			alpha += 1
	if len(s) == 10 and dig >= 3 and alpha >= 2 and s.isalnum() and len(set(list(s))) == 10:
		print("Valid")
	else:
		print("Invalid")
		