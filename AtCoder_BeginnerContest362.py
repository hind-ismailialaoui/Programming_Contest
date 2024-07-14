#A

R, G, B = map(int, input().split())
C = str(input())

if C[0] == "R":
    print(min(G, B))
elif C[0] == "G":
        print(min(R, B))
else:
    if C[0] == "B":
        print(min(R, G))

#B 

import math

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

# en A
BC = (xb-xc)**2 + (yc-yb)**2
AB = math.sqrt((xb-xa)**2 + (yb-ya)**2)
AC = math.sqrt((yc-ya)**2 + (xc-xa)**2)
if BC == round(AC**2) + round(AB**2) :
    print("Yes")
else: 
    # en B
    AC = (xc-xa)**2 + (yc-ya)**2
    BA = math.sqrt((xb-xa)**2 +(yb-ya)**2)
    BC = math.sqrt((yc-yb)**2 + (xc-xb)**2)

    if AC == round(BA**2) + round(BC**2) :
        print("Yes")

    else: 
        # en C
        AB = (xb-xa)**2 + (yb-ya)**2
        CA = math.sqrt((xc-xa)**2 + (yc-ya)**2)
        CB = math.sqrt((yc-yb)**2 + (xc-xb)**2)
        if AB == round(CA**2) + round(CB**2):
            print("Yes")
        else:
            print("No")


