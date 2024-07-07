t = (int(input()))

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    min_team = min(x2-x1, y2-y1)

    x1 = x1 +  min_team
    y1 = y1 + min_team
    if y1 == y2:
        if x1 <= y2 and y2 <= x2:
            print('NO')
        else:
            print('YES')
    else:
        if y1 <= x2 and x2 <= y2:
            print('NO')
        else:
            print('YES')




    # for i in range(1,):
    #     if min(x1, y1) + i == max(x1, y1):
    #         print('YES')
    # MAX = max(x1, y1)
    # MIN = min(x1, y1)
    #
    #
    # if x1 == x2 == 0:
    #     print('YES')
    # if MIN != MAX:
    #     for i in range(MAX):
    #         MIN = MIN + i
    #         if MIN == MAX:
    #             print('NO')
    # else:
    #     print('YES')

    # elif y1 > x1:
    #     #on fait les tests coté
    #     for i in range(y1):
    #         x1= x1 + i
    #         if x1 == y1:
    #             print('YES')
    # elif x1 > y1:
    #     #on fait les tests coté team 1
    #     for i in range(x1):
    #         y1= y1 + i
    #         if x1 == y1:
    #             print('YES')
    # else:
    #     print('NO')
    