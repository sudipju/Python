#!/usr/bin/python3
import sys

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
    inVal = sys.argv[1]
    intParam = float(inVal)
    #intParam = inVal
    try:
        fahrenheit = centrigradeToFahrenheit(intParam)
        print("Fahrenheit = ",fahrenheit)
        centrigrade=fahrenheitToCentrigrade(fahrenheit)
        print("centrigrade = ",centrigrade)
    except TypeError as err:
        #print("err= ", err)
        print("Type given is = ", str(err) + " but accepted types are int and float !")
        quit()
    
    

