from etudiant import etudiant
from external import external
E = external()
V = etudiant(12,"IBRAHIM",43)
print(V)
#E.data_insert(V)
rows = E.data_recover()
print (rows)


