def multpoly(p1, p2):
    res = {}
    for exp1, pwr1 in p1:
        for exp2, pwr2 in p2:
        if pwr1 + pwr2 not in res:
            res[pwr1 + pwr2] = exp1 * exp2
        else:
            res[pwr1 + pwr2] += exp1 * exp2
    res = del0(res)
    return (format(res))
