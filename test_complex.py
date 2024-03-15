from complex_numbers import Complex


def test_addition():
    num1 = Complex(2, 3)
    num2 = Complex(4, 5)
    result = num1 + num2
    assert str(result) == "6 + 8i"
    
def test_subtraction():
    num1 = Complex(2, 3)
    num2 = Complex(4, 5)
    result = num1 - num2
    assert str(result)  == "-2 - 2i"
    
def test_multiplication():
    num1 = Complex(2, 3)
    num2 = Complex(4, 5)
    result = num1 * num2
    assert str(result) == "-7 + 22i"
    
def test_division():
    num1 = Complex(2, 3)
    num2 = Complex(4, 5)
    result = num1 / num2
    assert result.real == 0.5609756097560976
    assert result.imaginary == 0.04878048780487805
    
def test_modulus():
    num = Complex(3, 4)
    result = num.mod()
    assert result == 5.0
    
def test_argument():
    num = Complex(1, 1)
    result = num.arg()
    assert result == 0.7853981633974483

def test_argument_2():
    num = Complex(3, 2)
    result = num.arg()
    assert result == 0.5880026035475675
    