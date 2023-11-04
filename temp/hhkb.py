# B = int(input())
# b = False

# for i in range(18):
#     if i ** i == B:
#         b = True
#         if b == True:
#             print(i)
# print(-1)

B = int(input())
found = False

for i in range(1, int(B**0.5)+1):  # A^A will not exceed the square root of B
    if i ** i == B:
        print(i)
        found = True
        break

if not found:
    print(-1)

def find_integer_power(B):
    # We start at 1 because 0 to any power will not equal a positive B
    for A in range(1, B + 1):  # A cannot be larger than B
        if A**A == B:
            return A
    return -1


# N = int(input())
# S = input()

# count = 0
# for i in range(N-1):
#     if (S[i] == 'a') and (S[i+1] == 'b'):
#         print('Yes')
#         count += 1
#     elif (S[i] == 'b') and (S[i+1] == 'a'):
#         print('Yes')
#         count += 1
    
# if count != 1:
#     print('No')


# N = int(input())
# S = input()

# if ("ab" or "ba") in S:
#     print("Yes")
# else:
#     print("No")

N = int(input())
S = input()

if "ab" in S or "ba" in S:
    print("Yes")
else:
    print("No")
