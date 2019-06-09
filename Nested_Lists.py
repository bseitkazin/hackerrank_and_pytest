if __name__ == '__main__':
	arr = list()
	for _ in range(int(input())):
		name = input()
		score = float(input())
		arr.append((score, name))
	arr.sort()
	second_min = None
	for i in range(1, len(arr)):
		if arr[i][0] != arr[i - 1][0]:
			second_min = arr[i][0]
			break
	if (second_min == None):
		print(None)
	else:
		for i in arr:
			if i[0] == second_min:
				print(i[1])
	