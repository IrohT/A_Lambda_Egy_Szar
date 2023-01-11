List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
 
 
def secl(lista,fgv):    l = [];    exec("for y in fgv(lista): l.append(y[-2])");  return l
print(secl(List, lambda x: (sorted(i) for i in x)))


bho = lambda lista: [y[-2] for y in [sorted(sor) for sor in lista]]
print(bho(List))
