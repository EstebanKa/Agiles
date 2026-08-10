def sumar(numeros):
  #Regla 1: String vacio
  if numeros == "":
    return 0

  #Regla 2: Dos numeros separados por coma
  if "," in numeros:
    partes = numeros.split(",")
    return int(partes[0]) + int(partes[1])

  #Regla 3: Un solo número
  return int(numeros)
 