G, M, K = map(int, input().split())
glass = 0
mugcup = 0
for _ in range(K):
    if glass == G:
        glass = 0
    elif mugcup == 0:
        mugcup = M
    else:
        tmp = min(M - mugcup, G - glass)
        mugcup -= tmp
        glass += tmp
print(glass, mugcup)
