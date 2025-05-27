t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    sums = {}

    for _ in range(k):
        b, c = map(int, input().split())
        
        if b in sums:
            sums[b] =+ c
        
        else:
            sums[b] = c
    
    sorted_sums = sorted(sums.values(), reverse=True)

    top_n_sums = sorted_sums[:n]

    result_sum = sum(top_n_sums)

    print(result_sum)



    