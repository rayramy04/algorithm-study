import sys

results = []

for i in sys.stdin:
    
    a, op, b = i.strip().split()
    
    if op == "?": # better to handle exceptions before converting values to numbers.
        break
    
    a = int(a)
    b = int(b)

    if op == "+":
        result = a+b
    elif op == "-":
        result = a-b
    elif op == "*":
        result = a*b
    elif op == "/":
        result = a//b

    results.append(result)

for n in results:
    print(n)

"""
import sys

for line in sys.stdin:
    a, op, b = line.strip().split()

    if op == "?":   # 終了条件
        break

    a = int(a)
    b = int(b)

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)
"""