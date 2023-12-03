M, D = map(int, input().split())
y = list(map(int, input().split()))

if (M == y[1]) and (D == y[2]):
    print(str(y[0] + 1)+' '+str(1)+' '+str(1))
elif (D == y[2]):
    print(str(y[0])+' '+str(y[1]+1)+' '+str(1))
else:
    print(str(y[0])+' '+str(y[1])+' '+str(y[2]+1))

