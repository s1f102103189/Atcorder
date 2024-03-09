result = []
while True:
    A = int(input())
    result.append(A)
    if A == 0:
        break
    
result.reverse()
print(*result, sep='\n')