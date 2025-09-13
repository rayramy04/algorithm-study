while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:
        n, m = m, n
    print(n, m)