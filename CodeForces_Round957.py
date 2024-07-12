t = (int(input()))
# s = []
for _ in range(t):
    a, b, c = map(int, input().split())
    l = [a,b,c]

    val_max = max(a,b,c)
    nb_occ= l.count(val_max)

    print(val_max)
    print(nb_occ)