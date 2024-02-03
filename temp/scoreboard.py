N = int(input())
result_x = 0
result_y = 0

for _ in range(N):
    x, y = map(int, input().split())
    result_x += x
    result_y += y

if result_x > result_y:
    print("Takahashi")
elif result_x < result_y:
    print("Aoki")
else:
    print('Draw')