if __name__ == '__main__':
	n = int(input())
	arr = [int(i) for i in input().split()]
	first_max = max(arr)
	second_max = None
	for i in arr:
		if i < first_max and (second_max == None or second_max < i):
			second_max = i
	print(second_max)