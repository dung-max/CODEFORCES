import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]; idx += 1
        a = data[idx:idx+n]; idx += n
        b = data[idx:idx+n]; idx += n

        A0 = 0
        B0 = 0
        last_diff = -1

        for i in range(n):
            A0 ^= a[i]
            B0 ^= b[i]
            if a[i] != b[i]:
                last_diff = i + 1  

        if A0 == B0:
            out.append("Tie")
        else:
            if last_diff == -1:
                out.append("Ajisai" if A0 > B0 else "Mai")
            else:
                out.append("Ajisai" if (last_diff % 2 == 1) else "Mai")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
