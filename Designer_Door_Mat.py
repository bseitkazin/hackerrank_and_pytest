n, m = map(int, input().split())

s = "WELCOME"
col = 1
hui = ".|."

for i in range(n // 2):    
    w = hui*col
    print(w.center(m, "-"))
    col += 2

print(s.center(m, "-"))

for i in range(n // 2):    
    col -= 2
    w = hui*col
    print(w.center(m, "-"))