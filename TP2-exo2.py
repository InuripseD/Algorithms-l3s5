import time

def lecture_sudoku(nom):
    with open(nom) as f:
        F = []
        n = 0
        start = True
        for ligne in f:
            if start: 
                n = int(ligne[0])
                start = False
            else:
                L = ligne.split()
                F = F + [int(v) for v in L]
    return F, n

def affiche_sudoku(G, n):

    nbLigne = 0

    while nbLigne<n**2:

        nbColone = 0

        ligne = ""

        while nbColone<n**2:
            if not G[(nbLigne*(n**2))+nbColone] == 0:
                ligne += str(G[(nbLigne*(n**2))+nbColone])
            else :
                ligne += "_"
            if not (nbColone==((n**2)-1)):
                ligne += " "
            nbColone+=1
        
        if(nbLigne*n**2==0 or nbLigne*n**2==9):
            print(nbLigne*n**2, "   ", ligne)
        else:
            print(nbLigne*n**2, "  ", ligne)

        nbLigne+=1

    return None


def AngleDeZone(n, u):
    Q,R = divmod(u,n**2)
    qq, rq = divmod(Q,n)
    qr, rr = divmod(R,n)
    corner = (n**2)*n*qq + n * qr
    return corner

def zone(n, u):
    angle = AngleDeZone(n, u)
    VoisinDeZone = []

    for i in range(0,n):
        for j in range(0,n):
            VoisinDeZone.append(angle + ((n**2) * i) + j)
    
    return VoisinDeZone


def valide(G, n, u, x):
    if u > n**4:
        return False
    
    if not (G[u] == 0):
        return False

    for voisin in zone(n,u):
        if G[voisin]==x:
            return False 

    q,r=divmod(u,n**2)

    for i in range(q*(n**2),(q*(n**2))+(n**2)):
        if G[i]==x:
            return False

    for i in range(r,r+(n**2)*n**2-(n*n),n**2):
       if G[i]==x:
            return False
        
    return True

def sudoku(G, n, u = 0):

    if u==n**4:
        return G

    if not (G[u] == 0):
        return sudoku(G, n, u+1)

    for i in range(n**2):
        if valide(G, n, u, i+1):
            G[u] = i+1
            if sudoku(G, n, u+1)==None:
                G[u]=0
            else:
                return G
    return None   

Fichier="./sudokus/sudoku-3-facile-7.txt"#ça peut être très long en moyen et difficile.
print("Formule du fichier: "+Fichier)
F,n=lecture_sudoku(Fichier)
#print(F)
#print(n)
affiche_sudoku(F,n)
Zone=zone(3,7)
#print(Zone)
debut=time.time()
#print(valide(F, n, 37, 7))
m = sudoku(F, n)
affiche_sudoku(m,n)
print(time.time()-debut, "secondes")
