#DarinaS
#Matriz del abecedario 
abecedario=[
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L'],
    ['M','N','Ñ','O'],
    ['P','Q','R','S'],
    ['T','U','V','W'],
    ['X','Y','Z',' ']
]

for i in range(0,7): 
    for j in range(0,4): 
        print(f"[{i}] [{j}] = {abecedario[i][j]}")