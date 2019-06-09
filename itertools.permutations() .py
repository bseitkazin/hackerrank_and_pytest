from itertools import permutations
string, k = input().split()
k = int(k)
ans = list(permutations(string, k))
ans.sort()
for i in ans:
	print("".join(i))	
