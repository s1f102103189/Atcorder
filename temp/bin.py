N = int(input())

binary_number = bin(N)[2:]

count = 0
for i in reversed(binary_number):
   if i == '0':
       count += 1
   else:
       break
print(count)