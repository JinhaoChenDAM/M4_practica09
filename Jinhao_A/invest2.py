"""
Imprimir el total dels diners acumulats
després de 7 anys, utilitzant variables (comentari a afegir al codi)
"""
savings = 100
increase = 1.1
for i in range(7):
    savings *= increase
result = savings
print(result)