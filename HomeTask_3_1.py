list=[2, 'cat', 7, 2, 9, 'cat', 7, 42]
def hw31(L):
    L1=[]
    for i in L:
        if i not in L1:
            L1.append(i)
    L = L1
    return L
print(hw31(list))
