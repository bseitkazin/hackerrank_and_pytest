from itertools import groupby 
string = list(input())
string.sort()
"".join(string)
li = list()
for i, j in groupby(string):
	a = len(list(j))
	c = i
	li.append((a, -ord(c)))
for i in range(3):
	ans = max(li)
	print(chr(-ans[1]), ans[0])
	li.remove(ans)