

# 1 

a = "Esto es un String"
print(len(a))
print(a[a.find("es")])
print(a.upper())

def func_1(cadena: str) -> bool:
    return True if cadena[0] == cadena[-1] else False


print(func_1("Hola"))
print(func_1("Holh"))
print(func_1("HolH"))

# 2 

# en python los strings una vez creados no pueden ser modificados (inmutabilidad) y si queremos cambiar algo del string, debemos crear una copia del original con la modificacion


def reemplazo(string, nuevo_caracter, posicion):
    if posicion < 0 or posicion >= len(string):
        raise ValueError("posicion invalida")
    
    nuevo_string = string[:posicion] + nuevo_caracter + string[posicion+1:]
    return nuevo_string

try:
    a[2] = "e"
except Exception as ex:
    print(ex)


# 3

a = "alvaro"
b = "alvaro"

print(a == b)
print(a is b)

c = "".join(["a", "l", "v", "a", "r", "o"])
print(c)
print(c == a)
print(c is a)


# a is b devuelve True porque el interprete de python optimiza el uso de los strings mas pequeños que son iguales, apuntando a las mismas variables

# 4

def concatenar_palabras(lista_palabras):
    cadena_concatenada = ", ".join(lista_palabras)
    return cadena_concatenada

palabras = ["manzana", "naranja", "plátano", "uva"]
resultado = concatenar_palabras(palabras)
print("Cadena concatenada:", resultado)

def repetir_string(cadena, numero, separador):
    cadena_repetida = (separador.join([cadena] * numero))
    return cadena_repetida

resultado = repetir_string("Hola", 3, ", ")
print("Cadena repetida:", resultado)


# 5

texto = "Crea una función que reciba un string y un número, y devuelva el string repetido el número de veces indicado, añadiendo un separador entre repeticiones."
print(texto.replace("un", "*******"))
print(texto.find("veces"))
texto_split = texto.split(",")
print(texto_split)
print(" ".join(texto_split))


def clean(string_list):
    clean_list = []
    for string in string_list:
        clean_string = string.strip()
        clean_list.append(clean_string)
    
    return clean_list

list_strings = [
    "   Hello world!   ",
    "   some spaces      "
]
print("Lista limpia:", clean(list_strings))


# 6 
def posiciones_vocales(cadena):
    vocales = "aeiouAEIOU"
    posiciones = []

    for indice, caracter in enumerate(cadena):
        if caracter in vocales:
            posiciones.append(indice)
    
    return posiciones

texto = "Hello World!"
print("Posiciones de las vocales:",  posiciones_vocales(texto))


def invertir_string(cadena):
    caracteres_invertidos = []
    for caracter in cadena:
        caracteres_invertidos.insert(0, caracter)
    
    cadena_invertida = "".join(caracteres_invertidos)
    return cadena_invertida

texto = "Python"
print("Cadena invertida:", invertir_string(texto))


# 7

def extraer_fecha(fecha):
    año = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    
    return año, mes, dia

fecha = "2024-11-06"
año, mes, dia = extraer_fecha(fecha)
print(f"Año: {año}, Mes: {mes}, Día: {dia}")


def recortar_string(cadena):
    if len(cadena) > 6:
        return cadena[3:-3]
    else:
        return ""

texto = "¡Hola, mundo!"
resultado = recortar_string(texto)
print("Cadena recortada:" + resultado)



#8 

def formato_fstring(nombre, apellido, edad):
    result = f"Hola, soy {nombre} {apellido} y tengo {edad} años"
    return result

print(formato_fstring("Alvaro", "Suarez", 27))


def formato_format(nombre, apellido, edad):
    result = "Hola, soy {} {} y tengo {} años".format(nombre, apellido, edad)
    return result

print(formato_format("Alvaro", "Suarez", 27))


# 9

def contar_lineas(texto_multilinea):
    lineas = texto_multilinea.splitlines()
    return len(lineas)

poema = """ 
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Fusce cursus quam non velit ultrices, sit amet vestibulum 
justo consectetur. Integer consequat, turpis a accumsan
ullamcorper, odio dui hendrerit libero, sit amet efficitur
dolor lacus a magna. Quisque nec metus ac nisi congue fermentum."""

print("Número de líneas en el poema:", contar_lineas(poema))

def mostrar_ruta_raw():
    ruta_raw = r"C:\Users\Usuario\Documentos\archivo.txt"
    print("Raw string:", ruta_raw)
    ruta_normal = "C:\\Users\\Usuario\\Documentos\\archivo.txt"
    print("String normal:", ruta_normal)
    return ruta_raw == ruta_normal

es_igual = mostrar_ruta_raw()
print("¿Las rutas son iguales?", es_igual)


# 10

def convertir_numeros(cadena_numero):
    numero_entero = int(cadena_numero)
    numero_flotante = float(cadena_numero)
    numero_binario = bin(numero_entero)
    numero_hexadecimal = hex(numero_entero)
    return numero_entero, numero_flotante, numero_binario, numero_hexadecimal

resultado = convertir_numeros("42")
print("Entero:", resultado[0])
print("Flotante:", resultado[1])
print("Binario:", resultado[2])
print("Hexadecimal:", resultado[3])


def convertir_a_lista_enteros(cadena_numeros):
    lista_de_strings = cadena_numeros.split(",")
    lista_de_enteros = [int(numero) for numero in lista_de_strings]
    
    return lista_de_enteros

resultado = convertir_a_lista_enteros("1,2,3,4,5")
print("Lista de enteros:", resultado)


# 11
def codificar_y_decodificar(texto):
    texto_codificado = texto.encode("utf-8")
    print("Texto codificado (UTF-8):", texto_codificado)
    texto_decodificado = texto_codificado.decode("utf-8")
    print("Texto decodificado (UTF-8):", texto_decodificado)

texto = "¡Hola, mundo! にちこんは"
codificar_y_decodificar(texto)


#12

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

persona = Persona("Juan", 30)
print("str(persona):", str(persona))
print("repr(persona):", repr(persona))



def representacion_repr(lista_objetos):
    return ", ".join([repr(obj) for obj in lista_objetos])

persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 40)
lista_personas = [persona1, persona2]

resultado = representacion_repr(lista_personas)
print("Representaciones repr():", resultado)


#13

class Calculadora:
    """
    Una clase simple para realizar operaciones matemáticas básicas.
    
    Métodos:
    suma(a, b) -> float: Suma dos números.
    resta(a, b) -> float: Resta el segundo número del primero.
    multiplica(a, b) -> float: Multiplica dos números.
    divide(a, b) -> float: Divide el primer número por el segundo.
    """
    
    def suma(self, a, b):
        """
        Suma dos números.
        
        Parámetros:
        a (int o float): El primer número a sumar.
        b (int o float): El segundo número a sumar.
        
        Retorna:
        float: El resultado de la suma de `a` y `b`.
        
        Ejemplo:
        >>> calculadora = Calculadora()
        >>> calculadora.suma(2, 3)
        5
        """
        return a + b

    def resta(self, a, b):
        """
        Resta el segundo número del primero.
        
        Parámetros:
        a (int o float): El número al que se le restará.
        b (int o float): El número que se va a restar.
        
        Retorna:
        float: El resultado de la resta de `a` y `b`.
        
        Ejemplo:
        >>> calculadora = Calculadora()
        >>> calculadora.resta(5, 3)
        2
        """
        return a - b

    def multiplica(self, a, b):
        """
        Multiplica dos números.
        
        Parámetros:
        a (int o float): El primer número.
        b (int o float): El segundo número.
        
        Retorna:
        float: El resultado de multiplicar `a` y `b`.
        
        Ejemplo:
        >>> calculadora = Calculadora()
        >>> calculadora.multiplica(2, 3)
        6
        """
        return a * b

    def divide(self, a, b):
        """
        Divide el primer número por el segundo. Si el divisor es cero, devuelve un error.
        
        Parámetros:
        a (int o float): El número que será dividido.
        b (int o float): El número que divide `a`.
        
        Retorna:
        float: El resultado de dividir `a` entre `b`.

        Levanta:
        ValueError: Si `b` es cero.
        
        Ejemplo:
        >>> calculadora = Calculadora()
        >>> calculadora.divide(6, 2)
        3.0
        >>> calculadora.divide(6, 0)
        ValueError: No se puede dividir entre cero
        """
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

calculadora = Calculadora()
print(calculadora.suma(2, 3))   
print(calculadora.resta(5, 3))    
print(calculadora.multiplica(2, 3)) 
try:
    print(calculadora.divide(6, 0))  # debe dar error
except ValueError as e:
    print(e)
