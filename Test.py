import unittest
import LibNumerosComplejos

#Tests Libreria de numeros complejos
#hecho por Santiago Córdoba Dueñas

c1 = (5.5, -9)
c2 = (-3, 6)
c3 = (1, 2)
c4 = (4, -0.5)


class Testlibcomplejos(unittest.TestCase):
    def test_suma(self):

        self.assertAlmostEqual(LibNumerosComplejos.suma(c1, c2)[0], 2.5)
        self.assertAlmostEqual(LibNumerosComplejos.suma(c1, c2)[1], -3)

        self.assertAlmostEqual(LibNumerosComplejos.suma(c3, c4)[0], 5)
        self.assertAlmostEqual(LibNumerosComplejos.suma(c3, c4)[1], 1.5)

    def test_multiplicacion(self):

        self.assertAlmostEqual(LibNumerosComplejos.multiplicacion(c1, c2)[0], 37.5)
        self.assertAlmostEqual(LibNumerosComplejos.multiplicacion(c1, c2)[1], 60)

        self.assertAlmostEqual(LibNumerosComplejos.multiplicacion(c3, c4)[0], 5)
        self.assertAlmostEqual(LibNumerosComplejos.multiplicacion(c3, c4)[1], 7.5)


    def test_resta(self):

        self.assertAlmostEqual(LibNumerosComplejos.resta(c1, c2)[0], 8.5)
        self.assertAlmostEqual(LibNumerosComplejos.resta(c1, c2)[1], -15)

        self.assertAlmostEqual(LibNumerosComplejos.resta(c3, c4)[0], -3)
        self.assertAlmostEqual(LibNumerosComplejos.resta(c3, c4)[1], 2.5)


    def test_division(self):

        self.assertAlmostEqual(LibNumerosComplejos.division(c1, c2)[0], -1.5666666666666667)
        self.assertAlmostEqual(LibNumerosComplejos.division(c1, c2)[1], -0.133333333333333335)

        self.assertAlmostEqual(LibNumerosComplejos.division(c3, c4)[0], 0.18461538461538463)
        self.assertAlmostEqual(LibNumerosComplejos.division(c3, c4)[1], 0.5230769230769231)


    def test_moduloc(self):

        self.assertAlmostEqual(LibNumerosComplejos.moduloc(c1), 10.55)
        self.assertAlmostEqual(LibNumerosComplejos.moduloc(c2), 6.71)


    def test_conjugado(self):

        self.assertAlmostEqual(LibNumerosComplejos.conjugado(c1)[0], 5.5)
        self.assertAlmostEqual(LibNumerosComplejos.conjugado(c1)[1], 9)

        self.assertAlmostEqual(LibNumerosComplejos.conjugado(c2)[0], -3)
        self.assertAlmostEqual(LibNumerosComplejos.conjugado(c2)[1], -6)


    def test_polar_a_cartesiano(self):

        self.assertAlmostEqual(LibNumerosComplejos.polar_a_cartesiano(c1)[0], -5.01)
        self.assertAlmostEqual(LibNumerosComplejos.polar_a_cartesiano(c1)[1], -2.27)

        self.assertAlmostEqual(LibNumerosComplejos.polar_a_cartesiano(c2)[0], -2.88)
        self.assertAlmostEqual(LibNumerosComplejos.polar_a_cartesiano(c2)[1], 0.84)


    def test_fase(self):

        self.assertAlmostEqual(LibNumerosComplejos.fasec(c1), 5.26)
        self.assertAlmostEqual(LibNumerosComplejos.fasec(c2), 2.03)


if __name__ == '__main__':
    unittest.main()