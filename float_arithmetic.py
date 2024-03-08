import csv

def ex_2(temp_input, epsilon, data):
    resultados = []
    for elem in data:
        if abs(temp_input - float(elem[1])) < epsilon:
            resultado = {
                "temperature": elem[1],
                "difference": abs(temp_input - float(elem[1])),
                "time": elem[0]
            }
            resultados.append(resultado)
    print([f"Hour {elem['time']}" for elem in resultados])


def format(elem):
    return "{:.2f}".format(float(elem[1]))



with open("./temperatures.csv", "r") as file:
    data = list(csv.reader(file, delimiter=","))

    #temp_input = float(input("Introduce un valor de temperatura.\n"))
    #epsilon_input = float(input("Introduce un valor de epsilon.\n"))

    #Ej 2
    #ex_2(temp_input, epsilon_input, data[1:])

    #Ej 3
    result = list(map(format, data[1:11]))
    for elem in result:
        print(elem)

    #Ej 3.a
    for valor in data[1:10]:
        print(f"{float(valor[1])}")

    #Ej 3.b
    for valor in data[1:10]:
        print(f"{float(valor[1]):>6.2f}")

    #Ej 3.c
    for valor in data[1:10]:
        print(f"{float(valor[1]):.2e}")

    #Ej 4a
    sum_total = 0
    for elem in data[1:]:
        sum_total += float(elem[1])
    promedio = (sum_total/len(data[1:]))
    print(promedio)

    # Ej 4b
    sum_total = 0
    for elem in data[1:]:
        sum_total += float(elem[1])
    promedio = (round(sum_total, 2)/len(data[1:]))
    print(promedio)

    # Ej 4c
    sum_total = 0
    for elem in data[1:]:
        sum_total += round(float(elem[1]), 2)
    promedio = (sum_total/len(data[1:]))
    print(promedio)

    # Ej 4d
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    sum_total_float = 0
    sum_total_str = 0
    for elem in data[1:]:
        sum_total_float += Decimal(float(elem[1]))
        sum_total_str += Decimal(elem[1])
    promedio_float = (sum_total_float/len(data[1:]))
    promedio_str = (sum_total_str/len(data[1:]))
    print(f"Float: {promedio_float}   String: {promedio_str}")
    # Si hay diferencias por como redondea la funcion float el str

    sum_total_float = 0
    sum_total_str = 0
    for elem in data[1:]:
        sum_total_float += Decimal(float(elem[1])).normalize()
        sum_total_str += Decimal(elem[1]).normalize()
    promedio_float = sum_total_float.normalize()/len(data[1:])
    promedio_str = sum_total_str.normalize()/len(data[1:])
    print(f"Float: {promedio_float}   String: {promedio_str}")

    # Aparentemente no hay cambios


    # Ej 4e
    data_list = [float(elem[1]) for elem in data[1:]]
    print(sum(data_list)/len(data_list))
    
    # Ej 4f
    from math import fsum
    print(fsum(data_list)/ len(data_list))

    # Ej 4g
    import numpy as np
    print(np.mean(data_list))

    # Ej 4h
    from fractions import Fraction
    ratio_fractions = [Fraction(elem[2]) for elem in data[1:]]
    print(float(sum(ratio_fractions) / len(ratio_fractions)))
    # Comprueba que Fraction.from_float devuelve el mismo resultado que as_integer_ratio()
    value = 1.75
    fraction_from_float = Fraction.from_float(value)
    fraction_as_ratio = Fraction(value).as_integer_ratio()
    print("Fraction.from_float():", fraction_from_float)
    print("as_integer_ratio():", fraction_as_ratio)
    # El valor de ambas es el mismo pero representado de diferente forma

    #Ej 4i
    from statistics import mean
    print(mean(data_list))

    #Ej 4j
    print(f"Valor Real: {promedio}")
    print(f"Valor Statistics: {mean(data_list)}   Porcentaje Error: {((promedio - mean(data_list))/promedio) * 100}")
    print(f"Valor fsum: {fsum(data_list)/ len(data_list)}   Porcentaje Error: {((promedio - fsum(data_list)/ len(data_list))/promedio) * 100}")
    

    #Ej 5

    data_hex = [elem[3] for elem in data[1:]]
    print(data_hex[0])
    print(float.fromhex(data_hex[0]))
    print(f"{float.fromhex(data_hex[0]):.2e}")

    #Ej 6
    from decimal import Decimal
    contador_menos_uno = 0
    contador_cero = 0
    contador_uno = 0

    for temperatura in data_list:
        comparacion = Decimal.compare(Decimal(temperatura), Decimal(0))
        if comparacion < 0:
            contador_menos_uno += 1
        elif comparacion == 0:
            contador_cero += 1
        else:
            contador_uno += 1

    print(f"-1:  {contador_menos_uno}")
    print(f"0:  {contador_cero}")
    print(f"1:  {contador_uno}")

    #Ej 7
    import numpy as np
    import matplotlib.pyplot as plt

    fft_resultado = np.fft.fft(data_list)
    frecuencias = np.fft.fftfreq(len(data_list))
    indice_maximo = np.argmax(fft_resultado)
    periodo = 1 / np.abs(frecuencias[indice_maximo])
    # plt.plot(data_list)
    # plt.title('Temperaturas')
    # plt.xlabel('Hora')
    # plt.ylabel('Temperatura')
    # plt.text(len(data_list) // 2, max(data_list), f'Periodo: {periodo:.2f} horas')
    #plt.show()


    #Ej 8
    suma_prueba = 1.1 + 2.2
    if suma_prueba == 3.3:
        print("Son iguales")
    else:
        print("Son diferentes")
    
    # Son diferentes debido la precision de los numeros con coma flotante y el redondeo
        
    # Ej 8a
    resultado = Decimal('1.1') + Decimal('2.2')
    if resultado == Decimal('3.3'):
        print("Son iguales")
    else:
        print("Son diferentes")

    #Con la clase Decimal soluconamos los problemas de coma flotante
        
    # Ej 8b
    resultado_sum = sum([1.1, 2.2])
    resultado_fsum = fsum([1.1, 2.2])
    if resultado_sum == 3.3:
        print("El resultado con sum es igual a 3.3")
    else:
        print("El resultado con sum no es igual a 3.3")

    if resultado_fsum == 3.3:
        print("El resultado con fsum es igual a 3.3")
    else:
        print("El resultado con fsum no es igual a 3.3")

    #La precision sigue sin ser la adecuada
        
    #Ej 8c
    resultado = Fraction(11, 10) + Fraction(22, 10)
    if resultado == Fraction(33, 10):
        print("El resultado es igual a 3.3")
    else:
        print("El resultado no es igual a 3.3")

    #Si resulta igualm sin embargo si uso floats:
    resultado = Fraction(1.1) + Fraction(2.2)

    # Compara el resultado con 3.3
    if resultado == Fraction(3.3):
        print("El resultado es igual a 3.3")
    else:
        print("El resultado no es igual a 3.3")

    #No es igual
        
    #Ej 9
    fraccion = Fraction(10, 81)
    decimal = Decimal(float(fraccion))
    flotante = float(decimal)
    import sys
    digitos_flotante = sys.float_info.dig
    precision_decimal = getcontext().prec
    print(f"preciosiones -> float {digitos_flotante}    decimal {precision_decimal}")

    getcontext().prec = 25
    getcontext().prec = 50

    #Ej º0

    import random
    import math
    muestra = 100
    # muestra = 10000000
    #FLOAT
    dentro = 0
    for i in range(muestra):
        x = random.random()
        y = random.random()
        distancia = math.sqrt(x**2 + y**2)

        dentro += 1 if distancia < 1 else 0
    estimacion = (dentro / muestra) * 4
    error_relativo = abs(estimacion - math.pi) / math.pi
    print(f"Estimacion de pi: {estimacion}")
    print(f"Error relativo: {error_relativo}")
    
    #DECIMAL
    dentro = 0
    for i in range(muestra):
        x = Decimal(random.random())
        y = Decimal(random.random())
        distancia = math.sqrt(x**2 + y**2)
        dentro += 1 if distancia < 1 else 0
    estimacion = Decimal(dentro / muestra) * 4
    error_relativo = abs(estimacion - Decimal(math.pi)) / Decimal(math.pi)
    print(f"Estimacion de pi con decimal: {estimacion}")
    print(f"Error relativo con decimal: {error_relativo}")

    # Aparentemente con Decimal la precision es muy superios, sobretodo al aumentar muestras
    # Estimacion de pi: 3.1410428
    # Error relativo: 0.0001750238335847526
    # Estimacion de pi con decimal: 3.1414596000000001296825757890474051237106323242188
    # Error relativo con decimal: 0.000042352273023350247920140289758973767971158058687523

    #Ej 11
    import sys

    # total = 0.0
    # i = 0

    # while True:
    #     total += 1.0
    #     i += 1
    #     if total == float('inf'):
    #         break

    # print(f"Total de iteraciones con float antes de 'infinito': {i}")

    #DECIMAL
    # total = Decimal('0')
    # i = 0

    # try:
    #     while True:
    #         total += Decimal('1')
    #         i += 1
    # except MemoryError:
    #     print(f"Total de iteraciones con decimal {i} iteraciones.")


    #Ej 12
    class Joya():
        quilate = 0.0

        def __init__(self, quilates: float) -> None:
            self.quilate = quilates

        def __float__(self) -> float:
            return self.quilate/24*100
        
        def __str__(self) -> str:
            return f"Pureza: {self.quilate}"
        
    def ordenar_pureza (joyas: list[Joya]) -> list:
        return sorted(joyas, key=lambda joya: float(joya))
    
    lista_joyas = [Joya(10.0), Joya(24.0), Joya(12.0), Joya(9.0)]

    lista_joyas = ordenar_pureza(lista_joyas)
    for joya in lista_joyas:
        print(joya)

    #Ej 13
        
    def binarios(cadena: str):
        if len(cadena) != 32:
            raise Exception("La cadena debe tener 32 bits de longitud.")

        signo = cadena[0]
        exponente = cadena[1:9]
        mantisa = cadena[9:]
        #primero calculo el signo -> 0 es positivo y 1 es negativo
        valor_signo = (-1) ** int(signo)
        #ahora el exponente
        valor_exponente = int(exponente, 2) - 127
        #mantisa
        valor_mantisa = 1 + sum(int(bit) * 2 ** (-index) for index, bit in enumerate(mantisa, start=1))
        return valor_signo * (2**valor_exponente) * valor_mantisa    
    print(binarios("01000010111101100000000000000000"))

    #Struct
    import struct   
    def binarios_struct(cadena: str):
        if len(cadena) != 32:
            raise Exception("La cadena debe tener 32 bits de longitud.")
        int_bits = int(cadena, 2)
        packed = struct.pack('I', int_bits)
        return struct.unpack('f', packed)[0]
    print(binarios_struct("01000010111101100000000000000000"))

    # 5.5
    #01000000101100000000000000000000

    # 10
    #01000001001000000000000000000000

    #0.002
    #00111011000000110001001001101111