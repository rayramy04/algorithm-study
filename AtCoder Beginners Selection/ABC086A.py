a, b = map(int, input().split())

mul = a * b

# judge even or add
if mul % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
faster solution

if a % 2 == 0 or b % 2 == 0:
    print("Even")
else:
    print("Odd")
"""