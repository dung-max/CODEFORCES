t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    last = s[-1]
    ans = 0

    for i in range(n - 1):
        if s[i] != last:
            ans += 1

    print(ans)
