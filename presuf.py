# N,M=(int(x) for x in input().split())
# S = input()
# T = input()

# if (S == T) and (N == M):
#     print(3)
# elif T.endswith(S):
#     print(2)
# elif T.find(S) == 0:
#     print(1)
# else:
#     print(0)

N, M = (int(x) for x in input().split())
S = input()
T = input()

if T.startswith(S) and T.endswith(S):
    print(0)
elif T.startswith(S):
    print(1)
elif T.endswith(S):
    print(2)
else:
    print(3)
