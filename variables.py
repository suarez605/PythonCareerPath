# 1
var_int = 0
var_str = ""
var_float = 0.1
var_dict = {}

#2

#a
print(type(var_int))
var_int = var_float
print(type(var_int))
#b
b_1 = b_2 = b_3 = "Hola"
print(b_1)
print(b_2)
print(b_3)

#c
var_1, var_2, var_3 = [1, 2, 3]
print(var_1)
print(var_2)
print(var_3)

#d
tupla = (1, 2, 3)
print(tupla[0])


#e
mi_lista = [1, 2, 3]
mi_lista[1] = 4
print(mi_lista)

mi_dic = {"foo": "Bar",
            "numero": 12
        }

mi_dic["bar"] = True

#f
var_int = 0
var_int += 1
print(var_int)
var_int *= 4
print(var_int)
var_int /= 2
print(var_int)


var_lista = [1, 2, 3]
print(var_lista)
var_lista += [4, 5]
print(var_lista)
var_lista *= 3
print(var_lista)

#g
var_lista = [1, 2, 3, 4, 5]
elem_1, elem_2, *resto = var_lista
print(elem_1)
print(elem_2)
print(resto)

#h
def funcion_local():
    x = 1

# Error print(x)

# i
y = 10
def funcion_global():
    global y
    y = 20
print(y)
funcion_global()
print(y)

# j 

def funcion_externa():
    z = 0
    def funcion_interna():
        nonlocal z
        z = 5
    
    funcion_interna()
    print(z)

funcion_externa()


# k DUDA

a = []
a = 0


# l 

mi_lista = [1, 2, 3, 4, 5]
mi_lista[0] = 0
mi_lista[-1] = 6
print(mi_lista)

try:
    mi_lista[12] = 33
except IndexError as ex:
    print("Error en el acceso, posicion fuera de rango.")


# m 
mi_dic = {
    "foo": "bar",
    "abc": 1
}
mi_dic["abc"] = "cde"

mi_dic["hola"] = "hello"

print(mi_dic)


# n

class MiClase():
    def __setitem__(self, key, value):
        print(f" esto es __setitem__ con valores {key}:{value}")

ins = MiClase()

ins["nueva clave"] = "nuevo valor"

# o

mi_lista = [1, 2, 3, 4]
mi_lista[1:2] = [6, 7]
print(mi_lista)


# p
mi_lista = [1, 2, 3, 4]
mi_lista[-1:-2] = [10, 11]
print(mi_lista)

# 3 Uso de nombres válidos
second_number = 10
global_var = "keyword"
my_name = "John"
import_var = 123


#4
lista  = [1, 2]
mi_elem, _ = lista
print(mi_elem)


mi_int_largo = 12_300_400_234
print(type(mi_int_largo))
print(mi_int_largo)


mi_lista = [1, 2, 3, 4]
for _, elem in enumerate(mi_lista):
    print(elem)


lista  = [1, 2, 3, 4]
mi_elem, _, mi_3_elem, _ = lista
print(mi_elem)
print(mi_3_elem)