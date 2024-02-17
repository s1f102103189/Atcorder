N = int(input())
result = ''

for i in range(N+N+1):
    if i % 2 == 0:
        result += '1'
    elif i % 2 == 1:
        result += '0'

print(result)