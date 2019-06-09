def merge_the_tools(string, k):
	for i in range(0, len(string), k):
		s = string[i:i+k]
		was = {}
		for j in s:
			if was.get(j) != 1:
				was[j] = 1
				print(j, end = "")
		print()
		
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)