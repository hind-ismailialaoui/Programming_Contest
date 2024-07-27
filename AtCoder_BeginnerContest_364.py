N = int(input())
S = [input() for _ in range(N)]

couple = False

for i in range(0, len(S)-2):
    if S[i]=='sweet' and S[i+1]=='sweet':
        couple = True
        print('No')
        break

if not couple:
    print('Yes')