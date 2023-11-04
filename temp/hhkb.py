B = int(input())
b = False

for i in range(18):
    if i ** i == B:
        b = True
        if b == True:
            print(i)
print(-1)

N = int(input())
S = input()

count = 0
for i in range(N-1):
    if (S[i] == 'a') and (S[i+1] == 'b'):
        print('Yes')
        count += 1
    elif (S[i] == 'b') and (S[i+1] == 'a'):
        print('Yes')
        count += 1
    
if count != 1:
    print('No')


N = int(input())
S = input()

if ("ab" or "ba") in S:
    print("Yes")
else:
    print("No")
