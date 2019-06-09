from itertools import combinations
n = int(input())
arr = input().split()
k = int(input())
tr = 0
fl = 0
for i in combinations(arr, k):
	if i.count('a'):
		tr += 1
	fl += 1
print(tr / fl)