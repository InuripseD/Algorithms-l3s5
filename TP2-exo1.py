def clause(s):
    L = s.split()
    return [int(v) for v in L[:-1]]

def parseur(nom):
    with open(nom) as f:
        F = []
        n = 0
        for ligne in f:
            if ligne[0] == 'c': continue
            if ligne[0] == 'p':
                L = ligne.split()
                n = int(L[-2])
            else: 
                F.append(clause(ligne))
    return F, n

def affiche(F):
    s=''
    for j in range(0,len(F)):
        C=F[j]
        s=s+'('
        for i in range(0,len(C)):
            if C[i]<0:
                s=s+'¬'
            s=s+'x'+str(abs(C[i]))
            if i==len(C)-1:
                s=s+')'
            else:    
                s=s+' ∨ '
        if j!=len(F)-1:
            s=s+' ∧ '
    return s

################################################################

def valide(F, A):
    for C in F:
        ok = False
        for l in C:
            if (l * A[abs(l)-1]) > 0 :
                ok = True
        if not ok :
            return False
    return True

################################################################

def aff_suivante(A):
    i = 0
    n = len(A)
    while i < n and A[i]==1:
        A[i] = -1
        i+=1
    if i == n:
        return None
    A[i]=1
    return A

def test_aff_suivante(n):
    A = [ -1 for i in range(0,n)]
    while not(A==None):
        print(A)
        A = aff_suivante(A)
    return None
        
#########################################################################

def sat_exhau(F, n):
    A = [-1] * n
    while not(A==None):
        if valide(F, A):
            return A
        A = aff_suivante(A)
    return A

def elimination(F, n, b):
    psi=[]
    for C in F:
        Cv = []
        sat = False
        for l in C:
            if (abs(l) == n) and (l * b > 0):
                sat = True
            elif not(abs(l)==n):
                Cv.append(l)
        if not(sat) :
            psi.append(Cv)
    return psi

def sat_backtrack(F, n):
    if(len(F)==0):
        return [1 for i in range(0,n)]
    for C in F:
        if len(C) == 0:
            return None
    for b in [-1, 1]:
        psi = elimination(F, n, b)
        A = sat_backtrack(psi, n-1)
        if not(A==None):
            return A + [b]
    return None

###############################################################################

print("-------------------------------------------------------")
Fichier="./cnf/random-25-sat.cnf"
print("Formule du fichier: "+Fichier)
F,n=parseur(Fichier)
print("Récupérée sous forme de tableau: ",F)
print("Nombre de variables: ",n)
print("Formule SAT: ",affiche(F))
print("-------------------------------------------------------")
#print(valide(F, [1,1,-1]))
#print(valide(F, [-1,-1,1]))
print("-------------------------------------------------------")
print(test_aff_suivante(3))
print("-------------------------------------------------------")
print(sat_exhau(F, n))
print(elimination(F, n, -1))
print(sat_backtrack(F, n))