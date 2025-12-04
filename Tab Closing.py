import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        a, b, n = map(int, input().split())
        if a == b or n <= a // b:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    solve()
