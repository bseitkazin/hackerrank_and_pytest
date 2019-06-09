import numpy

class TestClass(object):
	def test_one(self):
		test_sol = solution(["1", "2", "3"])
		test_ans = numpy.array([3., 2., 1.])
		assert (test_sol == test_ans).all()
	
	def test_two(self):
		test_sol = solution(["0", "555555555"])
		test_ans = numpy.array([555555555., 0.])
		assert (test_sol == test_ans).all()
	
	def test_three(self):
		test_sol = solution(["5", "1", "2", "17"])
		test_ans = numpy.array([17., 2., 1., 5.])
		assert (test_sol == test_ans).all()

		
def solution(arr):
	a = numpy.array(arr, float)
	sz = len(arr)
	for i in range(sz//2):
		a[i], a[sz - i - 1] = a[sz - i - 1], a[i]
	return a
		
if __name__ == '__main__':
	arr = input().strip().split(' ')
	print(solution(arr))