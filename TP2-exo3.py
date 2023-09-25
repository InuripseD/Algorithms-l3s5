import time

def swap(liste, i, j):
	liste[j],liste[i] = liste[i], liste[j]

def reverse(liste, start):
	(i, j) = (start, len(liste) - 1)
	while i < j:
		swap(liste, i, j)
		i = i + 1
		j = j - 1

#https://www.techiedelight.com/fr/find-lexicographically-next-permutations-string-sorted-ascending-order/
# Function to find lexicographically next permutations of a string.
# It returns true if the string could be rearranged as a lexicographically
# greater permutation; otherwise, it returns false.
def next_permutation(liste):

	# find the largest index `i` such that `chars[i-1]` is less than `chars[i]`
	i = len(liste) - 1

	while liste[i - 1] >= liste[i]:

		# if `i` is the first index of the string, that means we are already
		# at the highest possible permutation, i.e., the string is sorted in
		# descending order

		i = i - 1
		if i == 0:
			return False

	''' if we reach here, the substring `chars[i…n)` is sorted in descending order;
		i.e., chars[i-1] < chars[i] >= chars[i+1] >= chars[i+2] >= … >= chars[n-1] '''

	# find the highest index `j` to the right of index `i` such that
	# `chars[j] > chars[i-1]`
	j = len(liste) - 1
	while j > i and liste[j] <= liste[i - 1]:
		j = j - 1

	# swap character at index `i-1` with index `j`
	swap(liste, i - 1, j)

	# reverse substring `chars[i…n)` and return true
	reverse(liste, i)

	return True

def dicoOpti(a,b,c):

    dico = {}
    k = 0

    for mot in {a,b,c}:

        for l in list(mot):

            try: 
                #On essai juste d'appeler et si ça crash 
                #ça veut dire que la lettre n'est pas dans le dico
                dico[l]
            except:
                dico[l] = k
                k += 1

    return dico


def valeur(m, D, p):

    som = 0

    for i in range(0,len(m)):

        som += p[D[m[i]]] * 10**(len(m)-i-1)

    return som

def cryptarithme(a,b,c):

    dico = dicoOpti(a,b,c)

    perm = [i for i in range(0, len(dico)+1)]

    while next_permutation(perm) :

        va = valeur(a, dico, perm)
        vb = valeur(b, dico, perm)
        vc = valeur(c, dico, perm)

        if (va + vb) == vc:

            finalDico = {}

            for c in dico:
                finalDico[c] = perm[dico[c]]
            
            return finalDico, va, vb ,vc

    return False

dic = dicoOpti('OASIS', 'SOLEIL', 'MIRAGE')
print(dic)
debut=time.time()
#print(cryptarithme('OASIS', 'SOLEIL', 'MIRAGE'))
print(time.time()-debut, "secondes")
debut=time.time()
#print(cryptarithme('FRERE', 'SOEUR', 'BASTON'))
print(time.time()-debut, "secondes")