def d(x, y): return (x % y == 0)
def nd(x, y): return (x % y != 0)
for A in range(1, 2000):
    flag = 1
    for x in range(2000):
        if not (d(90, A) and (nd(x, A) <= (d(x, 18) <= nd(x, 24)))):
            flag = 0
            continue
    if flag:
        print(A)
        
