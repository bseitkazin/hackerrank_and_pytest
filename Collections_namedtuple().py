from collections import namedtuple

class TestClass(object):
	def test_one(self):
		names = namedtuple("names",    "ID         MARKS      NAME       CLASS")
		test_sol = solution(5, names, ["1          97         Raymond    7",         
									   "2          50         Steven     4",         
									   "3          91         Adrian     9",         
									   "4          72         Stewart    5",         
									   "5          80         Peter      6"])
		test_ans = 78.00
		assert test_sol == test_ans
	
	def test_two(self):
		names = namedtuple("names",    "MARKS      CLASS      NAME       ID")
		test_sol = solution(5, names, ["92         2          Calum      1",         
									   "82         5          Scott      2",         
									   "94         2          Jason      3",         
									   "55         8          Glenn      4",         
									   "82         2          Fergus     5"])
		test_ans = 81.00
		assert test_sol == test_ans
	
	def test_three(self):
		names = namedtuple("names",    "ID         MARKS      NAME       CLASS ")
		test_sol = solution(1, names, ["1          97         Raywill    7"])
		test_ans = 97.00
		assert test_sol == test_ans
		

def solution(n, names, l):
	suma = 0
	for i in l:
		a, b, c, d = i.split() 
		xz = names(a, b, c, d)
		suma += int(xz.MARKS)
	return suma / n

if __name__ == "__main__":
	n = int(input())
	names = namedtuple("names", input())
	l = []
	for i in range(n):
		 l.append(input())
	print(solution(n, names, l))

	
