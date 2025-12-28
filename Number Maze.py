import sys
from itertools import permutations

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1

    cache = {}  

    out = []
    for _ in range(t):
        n_str = data[idx].decode()
        j = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3

        if n_str not in cache:
            ps = [''.join(p) for p in permutations(n_str)]
            ps.sort()
            cache[n_str] = ps

        ps = cache[n_str]
        s = ps[j - 1]
        tcode = ps[k - 1]

        A = sum(1 for i in range(len(s)) if s[i] == tcode[i])
        B = len(s) - A  

        out.append(f"{A}A{B}B")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
