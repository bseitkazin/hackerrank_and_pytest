class TestClass(object):
	def test_one(self):
		test_sol = solution(5, 3, [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]], 1)
		test_ans = [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution(2, 2, [[1, 2], [7, 1]], 1)
		test_ans = [[7, 1], [1, 2]]
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution(2, 2, [[1, 2], [7, 1]], 0)
		test_ans = [[1, 2], [7, 1]]
		assert test_sol == test_ans


num = 0

def kthsort(val): 
    return val[num]

def solution(n, m, arr, k):
	print(arr)
	global num
	num = k
	arr.sort(key = kthsort)
	ans = ""
	return arr
	    
if __name__ == '__main__':
	n, m = map(int, input().split())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, input().rstrip().split())))
	k = int(input())
	ans = solution(n, m, arr, k)
	for i in ans:
		print(*i)