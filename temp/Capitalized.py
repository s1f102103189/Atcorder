S = input()

# S が1文字の場合
if len(S) == 1:
    if S.isupper():
        print('Yes')
    else:
        print('No')
else:
    a = S[0]
    b = S[1:]

    # 先頭の文字が大文字かつ残りが小文字かチェック
    if a.isupper() and b.islower():
        print('Yes')
    else:
        print('No')
