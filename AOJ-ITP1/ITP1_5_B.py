import sys

for line in sys.stdin:
    H, W = map(int, line.split())
    
    if H == 0 and W == 0:
        break
    
    print("#" * W)
    
    for _ in range(H-2):
        print("#" + "."*(W-2) +"#")
    
    print("#" * W)
    
    print()