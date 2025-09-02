def count_twos(x: int) -> int:
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt

n = int(input())
A = list(map(int, input().split()))

# The answer is the minimum number of factors of 2 in each element.
ans = min(count_twos(a) for a in A)
print(ans)