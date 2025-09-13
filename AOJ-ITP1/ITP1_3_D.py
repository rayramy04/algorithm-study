n = 0

a, b, c = map(int, input().split())

div = []
for i in range(1, c + 1):
    if c % i == 0:
        div.append(i)

for i in range(a, b + 1):
    if i in div:
        n += 1

print(n)