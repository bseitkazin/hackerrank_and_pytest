import collections

T = int(input())
for _ in range(T):
	n = int(input())
	d = collections.deque([int(i) for i in input().split()])
	last = -1
	gg = 0
	for i in range(n):
		if last == -1 or last >= max([d[0], d[-1]]):
			last = max([d[0], d[-1]])
			if d[0] > d[-1]:
				d.popleft()
			else:
				d.pop()
		else:
			gg = 1
			break
	if gg:
		print("No")
	else:
		print("Yes")