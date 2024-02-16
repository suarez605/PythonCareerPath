import list_comprehensions

def test_list_comprehension_correct():
    personas = [("Alvaro", 32, "Ingeniero", "Madrid"),
                ("Carla", 44, "Profesora", "Barcelona"),
                ("Pedro", 21, "Enfermero", "Sevilla")]
    assert len(list_comprehensions.nombres_mayores_30(personas)) == 2

def test_list_comprehension_zero():
    personas = [("Alvaro", 29, "Ingeniero", "Madrid"),
                ("Carla", 24, "Profesora", "Barcelona"),
                ("Pedro", 21, "Enfermero", "Sevilla")]
    assert len(list_comprehensions.nombres_mayores_30(personas)) == 0

def test_list_comprehension_limit():
    personas = [("Alvaro", 29, "Ingeniero", "Madrid"),
                ("Carla", 31, "Profesora", "Barcelona")]
    assert len(list_comprehensions.nombres_mayores_30(personas)) == 1

def test_list_comprehension_negatives():
    personas = [("Alvaro", -34, "Ingeniero", "Madrid"),
                ("Carla", 31, "Profesora", "Barcelona")]
    assert len(list_comprehensions.nombres_mayores_30(personas)) == 1
