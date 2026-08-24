def sumar(numeros):
  #Regla 1: String vacio
  if numeros == "":
    return 0
  
  # Regla 3 y Nueva Funcionalidad: Admite saltos de linea
  numeros = numeros.replace("\n", ",")
  if "," in numeros:
    partes = numeros.split(",")
    return sum(int(numero) for numero in partes)

  #Regla 3: Un solo número
  return int(numeros)

 