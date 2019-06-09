from collections import OrderedDict

def solution(n, ):
	or_dict = OrderedDict()
	for i in range(n):
		l = input().split()
		price = int(l.pop())
		try:
			or_dict[" ".join(l)] += price
		except:
			or_dict[" ".join(l)] = price
	for i in or_dict:
		print(i, or_dict[i])
	

n = int(input())
	