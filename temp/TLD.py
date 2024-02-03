# 英小文字と . のみからなる文字列 
# S が与えられます。
# S を . で分割したときの末尾の文字列を出力してください。
# すなわち、. を含まない 
# S の接尾辞のうち最長のものを出力してください。

S = input()
result = ''

for i in range(len(S)):
    if S[i] == '.':
        result = S[i+1: ]

print(result)
