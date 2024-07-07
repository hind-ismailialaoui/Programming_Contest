N = int(input())
S = str(input())
S2 = []
i=0
count = 0

while i <= N-3:
    if S[i:i+3] == 'ABA':
        count += 1
        i += 1
        S2.append('A')
    elif S[i:i+3] == 'BAB':
        count += 1
        i += 1
        S2.append('B')
    else:
        i +=1
print(S2)
print(count)
# N = int(input())
# S = str(input())
#
# i = 0
# c = 1
# while i <= N:
#     if S[i:i+3] == 'ABA':
#         S = S[:i+1] + S[i+3:]
#         N -= 2
#         c +=1
#     elif S[i:i + 3] == 'BAB':
#         S = S[:i + 1] + S[i + 3:]
#         N -= 2
#         c += 1
#     else:
#         i += 1
#
#
# print(c)
