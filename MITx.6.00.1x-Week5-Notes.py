# EdX MITx.6.00.1x - Week 5 Code and notes

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

##

def foo(L):
    val = L[0]
    while (True):
        val = L[val]

# foo(b) infinate loop




def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)