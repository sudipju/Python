#!/usr/bin/python3
from temperatureConverter import *
import sys

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