class TestClass(object):
	def test_one(self):
		test_sol = solution(3, 2)
		test_ans = (5, 1, 6)
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution(7, 0)
		test_ans = (7, 7, 0)
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution(155, 228)
		test_ans = (383, -73, 35340)
		assert test_sol == test_ans


def solution(a, b):
	return (a + b, a - b, a * b)

if __name__ == '__main__':
	print(*solution(int(input()), int(input())), sep = "\n")