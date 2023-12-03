import math

D = int(input())

def min_difference(D):
    min_diff = float('inf')
    max_limit = int(math.sqrt(D)) + 2 

    for x in range(max_limit):
        y = int(math.sqrt(D - x**2))
        diff = abs(x**2 + y**2 - D)
        if diff < min_diff:
            min_diff = diff

    return min_diff

print(min_difference(D))
