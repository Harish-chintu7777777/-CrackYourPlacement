def printDups(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    res = []
    for i in d:
        if d[i] > 1:
            res.append(i)
    return res

