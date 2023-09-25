# Take a list and a number and return a sublist with a sum that give our number or return False.
def find_combi_positive_backtrack(T, t, S = [] ):

    if sum(S) == t:
        return S

    if sum(S) > t or len(S)==len(T):
        return False

    S.append(T[len(S)])

    if not (find_combi_positive_backtrack(T, t, S)==False) :
        return S
    
    S.pop()
    S.append(0)

    if not (find_combi_positive_backtrack(T, t, S)==False) :
        return S

    S.pop()
    return False

Tab = [5,2,7,3,8]
print(find_combi_positive_backtrack(Tab, 15, []))
