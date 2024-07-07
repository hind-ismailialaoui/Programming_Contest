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
    #
    #
    #
    #
    #1 CREATE EXTERNAL TABLE Faits (
SK Etablissement INT,
3 SK_Temps INT,
4 SK_Patient INT,
5 SK Localisation INT,
6 SK_Professionnel INT,
7 SK Diagnostic INT,
8 b_Consult_Etab_Periode INT,
9
Nb_Consult_Diag_Periode INT,
10 Nb_Hospi_Periode INT,
11
Nb Hospi Diag Periode INT,
12
Nb_Hospi_Sexe_Age INT,
13
Nb Consult_Pro INT,
14
15 Nb_Deces_Loca_Periode INT,
Nb Satis Loca Periode INT
16 )
17 ROW FORMAT DELIMITED
18 FIELDS TERMINATED BY
19 STORED AS TEXTILE
20 LOCATION '/user/hive/data/ProjetBD/Table Faits'
