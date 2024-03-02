import random

M = list(map(int, input().split()))

n = random.randint(1,3)
if n != M[0] + M[1]:
    print(n)