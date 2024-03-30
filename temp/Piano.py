W, B = map(int, input().split())

def exists_in_pattern(W, B):
    # ピアノの鍵盤パターン
    pattern = "wbwbwwbwbwbw"
    white_count = pattern.count('w')
    black_count = pattern.count('b')

    # 単一のパターンで条件を満たすかどうか
    if W <= white_count and B <= black_count:
        return 'Yes'

    # パターンを跨いで条件を満たすかどうか
    for start in range(len(pattern)):
        for end in range(start, len(pattern) * 2):
            extended_pattern = pattern + pattern
            white_in_range = extended_pattern[start:end].count('w')
            black_in_range = extended_pattern[start:end].count('b')
            if white_in_range == W and black_in_range == B:
                return True

    return 'No'

# 入力されたWとBについて、条件を満たす部分が存在するかを確認
result = exists_in_pattern(W, B)
print(result)
