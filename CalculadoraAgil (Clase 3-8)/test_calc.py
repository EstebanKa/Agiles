import pytest
from calc import suma, multiplicacion, sumar, division

def test_suma():
    assert suma(1, 2) == 3

def test_multiplicacion():
    assert multiplicacion(2, 2) == 4

# Agregamos esta nueva prueba que va a fallar
def test_suma_neg():
    assert suma(-2, -1) == -3


#TEST IA
# Nivel 1: La estructura AAA y aserciones básicas
def test_sumar_numeros_positivos():
    # 1. ARRANGE (Preparar): Definimos el escenario y los datos de prueba
    numero1 = 5
    numero2 = 7
    resultado_esperado = 12

    # 2. ACT (Actuar): Ejecutamos la unidad de código aislada
    resultado_obtenido = sumar(numero1, numero2)

    # 3. ASSERT (Afirmar): El framework verifica que todo coincida (Self Validation)
    assert resultado_obtenido == resultado_esperado

# Nivel 2: Parametrización
# Le pasamos una lista de tuplas: (numero1, numero2, resultado_esperado)
@pytest.mark.parametrize("num1, num2, esperado", [
    (1, 2, 3),        # Caso 1: Positivos
    (-1, -1, -2),     # Caso 2: Negativos
    (0, 5, 5),        # Caso 3: Sumar cero
    (100, 200, 300)   # Caso 4: Números más grandes
])
def test_suma_multiple(num1, num2, esperado):
    # 1. Arrange y Act integrados gracias a pytest
    resultado = suma(num1, num2)
    
    # 2. Assert
    assert resultado == esperado

#Nivel 3: Fixtures (Preparación del entorno)
# Definimos el Fixture usando el decorador de pytest
@pytest.fixture
def configuracion_inicial():
    # Acá prepararíamos el entorno real (ej: simular un cliente o conexión a base de datos)
    # Para nuestro caso, devolvemos un diccionario con datos fijos listos para usar
    print("\n[Preparando el escenario de prueba...]")
    datos = {
        "usuario": "Admin",
        "valor_base": 100,
        "multiplicador": 5
    }
    return datos

# Le pasamos el nombre EXACTO del fixture como parámetro a nuestro test
def test_multiplicacion_con_entorno(configuracion_inicial):
    # El test ya arranca con los datos cargados e inyectados por el fixture
    base = configuracion_inicial["valor_base"]
    multiplicador = configuracion_inicial["multiplicador"]
    
    # Actuar
    resultado = multiplicacion(base, multiplicador)
    
    # Afirmar
    assert resultado == 500
    assert configuracion_inicial["usuario"] == "Admin"

# Manejando excepciones con pytest
# Test para verificar el manejo de excepciones
def test_division_por_cero():
    # ACT y ASSERT se combinan en este bloque 'with'
    with pytest.raises(ValueError) as info_error:
        division(10, 0)
    
    # Opcional pero recomendado: Verificamos que el mensaje del error 
    # sea exactamente el que nosotros programamos.
    assert str(info_error.value) == "No se puede dividir por cero"