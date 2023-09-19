from math import sqrt
    

class Complex:
    """
    Atttibutes :
    real
    img
    Methods:
    add
    sub
    mul
    truediv 
    get_real
    get_img
    get_magnitude
    mod
    """

    def __init__(self, real, img):
        self.__real= float(real)
        self.__img= float(img)

    def get_real(self):
        """
        Returns:
            float : real part
        """
        return self.__real

    def get_img(self):
        """AI is creating summary for get_img

        Returns:
            [float]: [imaginary part]
        """
        return self.__img

    def __add__(self, num2):
        temp_real= self.get_real() + num2.get_real()
        temp_img= self.get_img() + num2.get_img()
        return Complex(temp_real, temp_img)

    def __sub__(self, num2):
        temp_real= self.get_real() - num2.get_real()
        temp_img= self.get_img() - num2.get_img()
        return Complex(temp_real, temp_img)

    def __mul__(self, num2):
        temp_real = (self.get_real() * num2.get_real()) - \
            (self.get_img() * num2.get_img())
        temp_img = (self.get_real() * num2.get_img()) + \
            (num2.get_real() * self.get_img())
        return Complex(temp_real, temp_img)

    def __truediv__(self, num2):
        mag = num2.get_magnitude()
        temp_real = ((self.get_real() * num2.get_real()) +
                     (self.get_img() * num2.get_img())) / mag
        temp_img = ((self.get_img() * num2.get_real()) -
                    (num2.get_img() * self.get_real())) / mag
        return Complex(temp_real, temp_img)

    def get_magnitude (self):
        """
        Returns:
            float: magnitude
        """
        return self.get_real() ** 2 + self.get_img() ** 2

    def mod (self):
        """
        Returns:
            string: formatted value of mod
        """
        return f"{sqrt(self.get_magnitude()):.2f}"

    def __str__(self):
        if self.get_img() >= 0:
            return f"{self.get_real():.2f} + {self.get_img():.2f}i"
        return f"{self.get_real():.2f} - {abs(self.get_img()):.2f}i"


num_1 = Complex(3, 2)
num_2 = Complex(-4, -5)
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1.mod())
print(num_2.mod())
