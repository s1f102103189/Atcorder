#1
S = input()

all_zeros = True
for i in range(len(S)):
    if i % 2 == 1:  # 偶数の位置をチェック
        if S[i] != '0':
            all_zeros = False
            break

if all_zeros:
    print('Yes')
else:
    print('No')


S = input()
if S[1::2] != '0' * (len(S) // 2):
    print('No')
else:
    print('Yes')

#2
N = int(input())
S = [input() for _ in range(N)]

# 各プレイヤーの勝利数をカウント
wins = [row.count('o') for row in S]

# 勝利数とプレイヤーの番号でソート
ranked_players = sorted(range(N), key=lambda i: (-wins[i], i))

# ソートされたプレイヤーの番号を出力
print(' '.join(str(i+1) for i in ranked_players))

#3
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]

now_sc = [i + 1 for i in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j] == 'o':
            now_sc[i] += a[j]

mx = max(now_sc)

for i in range(n):
    nokori = [a[j] for j in range(m) if s[i][j] == 'x']
    nokori.sort(reverse=True)
    ans = 0
    while now_sc[i] < mx:
        now_sc[i] += nokori[ans]
        ans += 1
    print(ans)
