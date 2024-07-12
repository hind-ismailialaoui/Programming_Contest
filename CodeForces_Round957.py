# A. Only Pluses

t = (int(input()))
# s = []
for _ in range(t):
    a, b, c = map(int, input().split())
    l = [a,b,c]

    val_max = max(a,b,c)
    val_min= min(a,b,c)
    val_milieu= between_min_max = [x for x in l if x != val_min and x != val_max][0]
    nb_occ= l.count(val_max)

    print(val_max)
    print(nb_occ)

    if nb_occ == 1:
        for i in range(5):
            val_min = val_min + i
            