import sys
from collections import Counter
def solve():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    idx = 1
    out = []
    for _ in range(q):
        n = int(data[idx]); idx +=1
        s = data[idx].decode()
        i = data[idx+1].decode()
        idx += 2
        out.append("YES" if Counter(s)== Counter(i) else "NO")
    sys.stdout.write("\n".join(out))
if __name__ == "__main__":
    solve()