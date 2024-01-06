N = int(input())
for a in range(N + 1):
   for b in range(N + 1 - a):
       for c in range(N + 1 - a - b):
          if a + b + c <= N:
             print(f"{a} {b} {c}")