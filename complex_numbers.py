import math

class Complex():
    def __init__(self, real: int, imaginary: int) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real = self.real * other.real + self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real - self.real * other.imaginary
        return Complex(real/denominator, imaginary/denominator)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i" if self.imaginary > 0 else f"{self.real} - {abs(self.imaginary)}i" 
    
    def mod(self):
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def arg(self):
        return math.atan(self.imaginary/self.real) if self.real != 0 else None    



def complex_to_polar(complex_num):    
    return math.sqrt(complex_num.real**2 + complex_num.imag**2) , math.atan(complex_num.imag/complex_num.real) if complex_num.real != 0 else 0.0


def complex_sqrt(complex_num, exponent):
    module, argument = complex_to_polar(complex_num=complex_num)
    return  math.pow(module, 1/exponent)


def complex_sqrt_moivre(complex_num):
    module, argument = complex_to_polar(complex_num=complex_num)
    module_sqrt = math.sqrt(module)
    argument_sqrt = argument / 2
    real_sqrt = module_sqrt * math.cos(argument_sqrt)
    imag_sqrt = module_sqrt * math.sin(argument_sqrt)
    return complex(real_sqrt, imag_sqrt)


def complex_root_moivre(complex_num, exponent):
    module, argument = complex_to_polar(complex_num=complex_num)
    module_root = math.pow(module, 1/exponent)
    argument_root = argument / exponent
    real_root = module_root * math.cos(argument_root)
    imag_root = module_root * math.sin(argument_root)
    return complex(real_root, imag_root)



def mandelbrot(complex_num, num_iter):
    z = complex(0, 0)
    for i in range(0, num_iter):
        z = z**2 + complex_num
        if abs(z) > 2:
            return i+1
    return num_iter

import matplotlib.pyplot as plt
import numpy as np

def generate_mandelbrot_image(width, height, max_iterations):
    image = np.zeros((height, width), dtype=np.uint8)
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    step_x = (xmax - xmin) / width
    step_y = (ymax - ymin) / height
    for i in range(height):
        for j in range(width):
            c = complex(xmin + j * step_x, ymax - i * step_y)
            iterations = mandelbrot(c, max_iterations)
            color = int(255 * iterations / max_iterations)
            image[i, j] = color
    return image

#image = generate_mandelbrot_image(1000, 1000, 100)
#plt.imshow(image, cmap='gray')
#plt.show()

def generate_mandelbrot_different_center(width, height, max_iter, center=-0.833+0.215j, zoom=1):
    iterations_matrix = np.zeros((height, width), dtype=np.int32)
    real_range = zoom * 2
    imag_range = zoom * 2
    step_x = real_range / width
    step_y = imag_range / height
    start_real = center.real - (real_range / 2)
    start_imag = center.imag + (imag_range / 2)
    
    for y in range(height):
        for x in range(width):
            c = complex(start_real + x * step_x, start_imag - y * step_y)
            iterations_matrix[y, x] = mandelbrot(c, max_iter)
    norm_iterations_matrix = (255 * iterations_matrix / np.max(iterations_matrix)).astype(np.uint8)
    plt.imshow(norm_iterations_matrix, cmap='gray', extent=[start_real, start_real + real_range, start_imag - imag_range, start_imag])
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.savefig('mandelbrot.png')
    plt.show()

generate_mandelbrot_different_center(5000, 5000, 200, center=-0.833+0.215j, zoom=0.05)