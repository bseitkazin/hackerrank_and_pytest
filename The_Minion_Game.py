def minion_game(string):
	Stuart = 0
	Kevin = 0
	index = 0
	for i in string:
		if i in "AIOEU":
			Kevin += len(string) - index
		else:
			Stuart += len(string) - index
		index += 1
	if Stuart < Kevin:
		print("Kevin", Kevin)
	elif Stuart > Kevin:
		print("Stuart", Stuart)
	else:
	 print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)