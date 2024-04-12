#Ej 1
# >>> None = 1
#   File "<stdin>", line 1
#     None = 1
#     ^^^^
# SyntaxError: cannot assign to None

#Ej 2
# None + 1
# Traceback (most recent call last):
#   File "/Users/alvaro.suarez/Documents/PythonCareerPath/none_sentinel_values.py", line 9, in <module>
#     None + 1
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# Ej 3
print(None == None)
# == compara que dos objetos sean el mismo, su igualdad, None es igual que None, por eso es True
print(None is None)
# is compara las posiciones de memoria de dos elementos, en este caso ambos son el mismo ya que 
# None esta ubicado en una posicion concreta de memoria

# Ej 4
print(bool(None))
# se obtiene False


#Ej 5
def hola_mundo():
    print("Hola mundo")

mi_var = hola_mundo()
print(mi_var)
# El resultado es None
print(type(mi_var))
# class NoneType

print(type(type(mi_var)))
# class type

# Ej 6
def mi_func(param):
    if param == None:
        return True
    return False

# Ej 7
mi_dic = {
    "a": None
}
# a
print({}.get("key", 1) == {"key": None}.get("key"))
# se puede añadir un valor default a la funcion get para que sustituya al valor por defecto None cuando la key no es encontrada
# asi los resultados no son iguales y no se cumple la igualdad

# b
sentinel = object()
print({}.get("key", sentinel) == {"key": None}.get("key", sentinel))
# Es falsa ya que sentinel que es el objeto recuperado del primer diccionario mientras que del segundo es None y no son iguales