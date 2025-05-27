#A


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    is_valide=True

    for i in range(1, n):
        if a[i] - a[i-1] not in [-7, -5, 5, 7]:
            print("no")
            is_valide = False
            break

    if is_valide:
        print("yes")


#B