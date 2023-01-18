areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55,
"habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

#Imprimeix el segon element
print(areas[1])

#Imprimeix l'últim element
print(areas[-1])

#Imprimeix l'àrea de la terrassa
print(areas[5])

#Imprimeix del primer element al tercer element
print(areas[1:4])

#Imprimeix del tercer element a l’últim
print(areas[3:])

#Imprimeix el total de l'àrea de les dues habitacions
print(areas[9] + areas[11])

#Modifica l’àrea del lavabo i imprimir la nova list area
areas[7] = 15
print(areas)

#Afegeix l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
areas.append("pati interior")
areas.append(2.78)
print(areas)