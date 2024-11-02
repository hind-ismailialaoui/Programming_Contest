# Stocker les chaînes dans une liste en utilisant une boucle
S = [input(f"S{i+1} = ") for i in range(8)]

# Compter les occurrences de '#' dans chaque chaîne en utilisant sum
total_hashes = sum(s.count('#') for s in S)

c = 64 

for i in range(8):
    nb = S[i].count('#')
    if  nb > 0:
        c = c - 8 - 7 * nb 
        if
