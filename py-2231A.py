# Codeforces 2231A
# Constructive Algorithm

t = int(input())

for _ in range(t):
    n = int(input())

    arr = []

    # Generate odd numbers
    for i in range(n):
        arr.append(2 * i + 1)

    print(*arr)