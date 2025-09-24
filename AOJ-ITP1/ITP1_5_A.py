import sys

for lines in sys.stdin:
    H, W = map(int, lines.split())
    
    if H == 0 and W == 0:
        break
    
    for _ in range(H):
        print("#" * W)
    print()