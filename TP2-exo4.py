import time

def affichage_reine(Q):

    if (Q == None):
        print("empty chess")
        return

    for x in Q:
        line = ""
        for col in range(len(Q)):
            if x==col:
                line+="x "
            else:
                line+="_ "
        print(line)

def reine_possible(Q,r,j):

    if not(Q[r] == -1):
        return False

    for line in range(r):
        if Q[line]==j:
            return False

    colDroite = j+1
    ligneMonte = r-1

    while (colDroite < len(Q)) and (ligneMonte >= 0):
        if Q[ligneMonte]==colDroite:
            return False
        colDroite += 1
        ligneMonte -= 1

    colGauche = j-1
    ligneMonte = r-1

    while (colGauche >= 0) and (ligneMonte >= 0):
        if Q[ligneMonte]==colGauche:
            return False
        colGauche -= 1
        ligneMonte -= 1

    return True

def placement_reines(Q, r=0):

    if r == len(Q):
        return Q
    
    for col in range(len(Q)):
        if reine_possible(Q,r,col):
            Q[r] = col
            if placement_reines(Q, r+1)==None:
                Q[r] = -1
            else:
                return Q
    
    return None

def reines(n):
    return placement_reines([-1 for j in range(0, n)])

Qa =[-1, -1, -1]
affichage_reine(Qa)
print(reine_possible([0, 2, -1, -1], 2, 3))
print(reine_possible(Qa, 0, 2))
#for i in range(4, 50): 
#    Qb = [-1 for j in range(0, i+1)]
#    affichage_reine(placement_reines(Qb))
affichage_reine(placement_reines(Qa))

debut=time.time()
affichage_reine(reines(15)) #Max reine 27 après c'est très long   
print(time.time()-debut, "secondes")