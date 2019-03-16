from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEquals(Calculadora().sumar(""), 0, "Cadena vacia")
