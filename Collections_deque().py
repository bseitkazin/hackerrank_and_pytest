from collections import deque

class TestClass(object):
	def test_one(self):
		test_sol = solution(6, [["append", "1"], ["append", "2"], ["append", "3"], ["appendleft", "4"], ["pop"], ["popleft"]])
		test_ans = deque([1, 2])
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution(3, [["append", "1"], ["pop"], ["appendleft", "3"]])
		test_ans = deque([3])
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution(3, [["appendleft", "1"], ["pop"], ["appendleft", "9"], ["pop"]])
		test_ans = deque([])
		assert test_sol == test_ans


def solution(n, li):
	d = deque()
	for i in li:
		i.append("")
		eval("d.{}({})".format(i[0], i[1]))
	return d

if __name__ == "__main__":
	n = int(input())
	li = []
	for i in range(n):
		li.append(input().split())
	print(*solution(n, li))