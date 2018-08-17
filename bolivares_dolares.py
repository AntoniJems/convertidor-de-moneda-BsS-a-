# -*- coding: UTF-8 -*-
'''
Created on Aug 15, 2018

@author: Antoni
'''



from pip._vendor.distlib.compat import raw_input


dolar_hoy = 5000000/100000

def calculator(bolivares):
    return bolivares / dolar_hoy


def run():
    print("CALCULADORA DE DIVISAS")
    print("convierte bolivares soberanos a dólares")
    print("")

    bolivares = float(raw_input("ingresa la cantidad de bolivares: "))
    resultado_bolivares = calculator(bolivares)
    
    print("{} bolivares soberanos son ${} dólares".format(bolivares,resultado_bolivares))
    print(" ")

if __name__ == '__main__':
    run()