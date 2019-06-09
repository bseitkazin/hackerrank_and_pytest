if __name__ == '__main__':
	s = input()
	cur = list()
	for i in s:
		if i.isalnum():
			cur.append(i)
	s = "".join(cur)
	print(s.isalnum())
	print(not s.isdigit() and s.isalnum())
	print(not s.isalpha() and s.isalnum())
	print(s.upper() != s and not s.isdigit() and s.isalnum())
	print(s.lower() != s and not s.isdigit() and s.isalnum())