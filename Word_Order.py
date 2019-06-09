n = int(input())
d = dict()
ans = []
for i in range(n):
	s = input()
	if d.get(s) == None:
		d[s] = 1
		ans.append(s)
	else:
		d[s] += 1
print(len(ans))
for i in ans:
	print(d[i], end = " ")		
