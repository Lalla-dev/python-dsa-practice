t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    mx = 0
    for i in range(n - 1):
        mx = max(mx, a[i] - a[i + 1])
 
    for i in range(1, n):
        if a[i] < a[i - 1]:
            a[i] += mx
 
    ok = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ok = False
            break
 
    print("YES" if ok else "NO")