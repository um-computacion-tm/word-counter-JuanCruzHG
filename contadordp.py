
import unittest

def contar_palabras(palabra):
        palabras = {}
        for word in palabra.split():
            if word in palabras:
                palabras[word] += 1
        else:
            palabras[word] = 1
        return palabras

class TestContarPalabras(unittest.TestCase):
    def test_hola(self):
        resultado = contar_palabras('hola')
        self.assertEqual(resultado, {"hola" : 1})

    def test_2(self):
        resultado = contar_palabras('perro negro')
        self.assertEqual(resultado, {"perro" : 1, "negro" : 1})
            
    def test_3(self):
        resultado = contar_palabras('el perro es negro')
        self.assertEqual(resultado, {"el" : 1, "perro" : 1, "es" : 1, "negro" : 1})
            
    def test_4(self):
        resultado = contar_palabras('gato gato perro perro')
        self.assertEqual(resultado, {"gato" : 2, "perro" : 2})


if __name__ == '__main__':
    unittest.main()