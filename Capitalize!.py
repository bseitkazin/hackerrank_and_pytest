import math
import os
import random
import re
import sys

class TestClass(object):
	def test_one(self):
		test_sol = solution("chris alan")
		test_ans = "Chris Alan"
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution("2FsW Eee rock")
		test_ans = "2FsW Eee Rock"
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution("asd")
		test_ans = "Asd"
		assert test_sol == test_ans


def solution(s):
	s = list(s)
	for i in range(len(s)):
		if (i == 0 or s[i - 1] == ' '):
			s[i] = s[i].upper()
	s = "".join(s)
	return s

if __name__ == '__main__':
    s = input()
    result = solution(s)
    print(result)
