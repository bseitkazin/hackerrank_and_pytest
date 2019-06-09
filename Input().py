x, k = map(int, input().split())
string = "a = " + input()
a = 0
exec(string)
print(k == a)
	