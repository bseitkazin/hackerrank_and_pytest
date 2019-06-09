import calendar

class TestClass(object):
	def test_one(self):
		test_sol = solution(6, 20, 2019)
		test_ans = "THURSDAY"
		assert test_sol == test_ans
	
	def test_two(self):
		test_sol = solution(8, 5, 2015)
		test_ans = "WEDNESDAY"
		assert test_sol == test_ans
	
	def test_three(self):
		test_sol = solution(6, 9, 2019)
		test_ans = "SUNDAY"
		assert test_sol == test_ans

def solution(month, day, year):
	cal = calendar.Calendar()
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	for i in cal.itermonthdays2(year, month):
		if i[0] == day:
			return days[i[1]].upper()

if __name__ == "__main__":
	month, day, year = map(int, input().split())
	print(solution(month, day, year))