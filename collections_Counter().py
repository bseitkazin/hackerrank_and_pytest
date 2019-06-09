from collections import Counter

class TestClass(object):
	def test_one(self):
		test_sol = solution(10, [2, 3, 4, 5, 6, 8, 7, 6, 5, 18], 6, [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]])
		test_ans = 200
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 6, [[1, 55], [2, 45], [1, 55], [5, 40], [7, 60], [10, 100]])
		test_ans = 110
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution(3, [2, 3, 2], 3, [[3, 4], [2, 2], [2, 7]])
		test_ans = 13
		assert test_sol == test_ans
	  

def solution(X, owner, N, li):
	shop = Counter(owner)
	ans = 0
	for i in li:
		size, cost = i
		if shop.get(size):
			shop[size] -= 1
			ans += cost
	return ans

if __name__ == "__main__":
	X = int(input())
	owner = [int(i) for i in input().split()]
	N = int(input())
	li = []
	for i in range(N):
		li.append(map(int, input().split()))
	print(solution(X, owner, N, li))
	