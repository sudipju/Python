#!/usr/bin/python3
import unittest

class TestTemperatureConverterMethods(unittest.TestCase):
    
    def test_CentigradeToFahrenheit(self) :
        self.assertAlmostEqual(centrigradeToFahrenheit(20),68.0,places=6)

    def test_FahrenheitToCentigrade_Negative(self) :
        self.assertNotAlmostEqual(fahrenheitToCentrigrade(21),68.0,places=6)

    def test_FahrenheitToCentigrade_Positive(self) :
        self.assertAlmostEqual(fahrenheitToCentrigrade(200),93.34,places=1)

    def test__typeCheker_Str_Negative(self) :
        self.assertRaises(TypeError,_typeCheker, "sudip")

    def test__typeCheker_List_Negative(self) :
        self.assertRaises(TypeError,_typeCheker, ["sudip","Johan"])

    def test__typeCheker_Positive_Int(self) :
        _typeCheker(int(20))

    def test__typeCheker_Positive_Float(self) :
        _typeCheker(float(20.0))

def _typeCheker(param):
    if (type(param) == int) :
        param=float(param)
    elif (type(param) == float) :
        param=param
    else:
        errorType=type(param).__name__
        raise TypeError(str(errorType))
    return param

def centrigradeToFahrenheit(centigradeVal):
    Tc = _typeCheker(centigradeVal)
    Tf = (9/5)*Tc + 32
    return Tf

def fahrenheitToCentrigrade(fahrenheit):
    Tf = _typeCheker(fahrenheit)
    Tc = (5/9)*(Tf - 32)
    return Tc

if __name__=='__main__':
    unittest.main()
    

