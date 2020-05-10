# python alignment.py
def indent(ind,prin):
    lenth = 40
    if ((len(ind))%2) != 0:
        lenth += 1
    return print(('{:->'+str(lenth)+'}').format(ind))
def printed(n):
    return print(n, end="")
def pgp(n):
    indent(n,printed("O   "),)

def indem(ind):
    lenth = 15
    if (len(ind))%2 != 0:
        lenth += 1
    return ('O'+'{:->'+str(lenth)+'}').format(ind)

