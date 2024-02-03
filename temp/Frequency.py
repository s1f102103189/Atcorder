import collections

S = input()

counter = collections.Counter(S)
maxc = max(counter.values())

result = min(k for k, val in counter.items() if val == maxc)
print(result)