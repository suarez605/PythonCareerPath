import csv


def nombres_mayores_30(personas: list):
    return [persona[0] for persona in personas if int(persona[1]) > 30]

def ciudades_unicas(personas: list):
    return {persona[3] for persona in personas}

def conteo_profesiones(personas):
    return {persona_profesion[2]: sum(1 for persona in personas if persona[2] == persona_profesion[2]) for persona_profesion in personas[1:]}

def promedio_edad(personas):
    edades = (int(persona[1]) for persona in personas)
    return sum(edades) / len(personas)

if __name__ == "__main__":
    with open("./data.csv", "r") as file:
        data = list(csv.reader(file, delimiter=","))[1:]
        result_list = nombres_mayores_30(data)
        result_set = ciudades_unicas(data)
        result_dict = conteo_profesiones(data)
        result_generators = promedio_edad(data)
        print(result_generators)