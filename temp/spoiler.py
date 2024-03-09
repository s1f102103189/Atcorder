S = input()

tmp = []

for i in range(len(S)):
    if S[i] == '|':
        tmp.append(i)
        
lst = list(S)

del lst[tmp[0]:tmp[1]+1]

S = ''.join(lst)

print(S)