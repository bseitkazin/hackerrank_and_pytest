from itertools import groupby
s = list(input())
for i,j in groupby(s):
    print((len(list(j)), int(i)), end = " ")