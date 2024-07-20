# A - Piling Up

R =int(input())

if R < 100:
    print(100-R)
elif R < 200:
    print(200-R)
elif R < 300:
    print(300-R)
else:
    print(399-R)

# B - Japanese Cursed Doll

N, T, P = map(int, input().split())
L = list(map(int, input().split()))

c = 0

def compter_p(L, T):
    p = 0
    for l in L:
        if l >= T:
            p = p + 1
    return(p)

p = compter_p(L,T)

if p < P:
    while(p < P):
        for i in range(0, len(L)):
            L[i] += 1
        p = compter_p(L, T)
        c = c + 1
print(c)