import sys

for line in sys.stdin:
    H, W = map(int, line.split())
    
    if (H, W) == (0, 0):
        break
    
    for i in range (H):
        result = ""
        
        if i % 2 == 0:
            for _ in range(W//2):
                result += "#."
            if W%2 == 1:
                result += "#"
                
        else:
            for _ in range(W//2):
                result += ".#"
            if W%2 == 1:
                result += "."
    
        print(result)
    print()

"""
    for i in range(H):
        row = ""
        for j in range(W):
            if (i + j) % 2 == 0:
                row += "#"
            else:
                row += "."
        print(row)

縦と横を足し合わせて判別するって事もできる。
"""