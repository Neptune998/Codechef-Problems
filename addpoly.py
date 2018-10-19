def del0(d):
    res = {}
    for key, val in d.items():
        if val != 0:
            res[key] = val
    return res


def format(d):
  li = []
  for key, val in sorted(d.items(), reverse=True):
      li.append((val, key))
  return li

def addpoly(p1,p2):
    '''Function to add two polynomial'''
    res={}
    for exp1,pwr1 in p1:
        for exp2,pwr2 in p2:
            if pwr1==pwr2:
                res[pwr1]=exp1+exp2
    for exp,pwr in p1:
        if pwr not in res:
            res[pwr]=exp
    for exp,pwr in p2:
        if pwr not in res:
            res[pwr]=exp
    res=del0(res)
    return(format(res))