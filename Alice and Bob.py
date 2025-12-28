import sys
from bisect import bisect_left, bisect_right

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]; a = data[idx + 1]; idx += 2
        v = data[idx:idx + n]; idx += n  # already sorted

        left = bisect_left(v, a)              # count of v < a
        right = n - bisect_right(v, a)        # count of v > a

        if right > left:
            b = a + 1
        else:
            b = a - 1  # a >= 1 so b >= 0

        if b < 0:
            b = 0
        elif b > 2_000_000_000:
            b = 2_000_000_000

        out.append(str(b))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
