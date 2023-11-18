N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)

# 最大値を取得
max_value = sorted_A[0]

# 次に大きい値を探す
next_max = None
for value in sorted_A:
    if value < max_value:
        next_max = value
        break

if next_max is None:
    print("次に大きい値は存在しません。")
else:
    print(next_max)

#######################################

N = int(input())
A = list(map(int, input().split()))

# 最大値を見つける
max_num = max(A)

# 最大値以外の値からなる新しいリストを作成
filtered_A = [i for i in A if i != max_num]

# 最大値以外の数が存在しない場合のチェック
if not filtered_A:
    print("次に大きい値は存在しません。")
else:
    print(max(filtered_A))
    
############################################

N = int(input())
A = list(map(int, input().split()))

# 最大値を見つける
max_num = max(A)

# 最大値が複数回現れるかどうかを確認
if A.count(max_num) > 1:
    # 最大値以外の値からなる新しいリストを作成
    max_pop = [i for i in A if i != max_num]
    print(max(max_pop))
else:
    # 最大値を除いた残りのリストから最大値を求める
    A.remove(max_num)
    print(max(A))

###############################################
N = int(input())
A = list(map(int, input().split()))

# 最大値のインデックスを見つける
max_index = A.index(max(A))
max_num = A.pop(max_index) 

if max_num in A:
    max_pop = [i for i in A if i != max_num]
    print(max(max_pop))
else:
    print(max(A))
