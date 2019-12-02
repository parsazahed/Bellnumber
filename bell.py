import math
def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
n = int(input("n: "))

def bellnum(n):
    bell = 0
    if n == 0:
        return 1
    for i in range(0, n):
        bell += nCr(n-1,i) * bellnum(i)
    return bell
print(bellnum(n))