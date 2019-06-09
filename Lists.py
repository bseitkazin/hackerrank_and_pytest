if __name__ == '__main__':
	n = int(input())
	List = list()
	for i in range(n):
		command, *arr = input().split()
		if command == "insert":
			if int(arr[0]) <= len(List): List.insert(int(arr[0]), int(arr[1]))
			else: print("Can't. Size is low")
		elif command == "print":
			print(List)
		elif command == "remove":
			if List.count(int(arr[0])): List.remove(int(arr[0]))
			else: print("We haven't")
		elif command == "append":
			List.append(int(arr[0]))
		elif command == "sort":
			List.sort()
		elif command == "pop":
			List.pop()
		elif command == "reverse":
			List.reverse()