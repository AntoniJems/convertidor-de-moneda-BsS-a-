# -*- coding: UTF-8 -*-
'''
Created on Aug 15, 2018

@author: Antoni
'''


from pip._vendor.distlib.compat import raw_input

def calculator(dolares):
    mex_to_col_rate= 50
    return mex_to_col_rate * dolares


def run():
    print("CALCULADORA DE DIVISAS")
    print("convierte  dólares a   bolivares soberanos")
    print("")

    dolares = float(raw_input("ingresa la cantidad de dólares: "))
    resultado_bolivares = calculator(dolares)
    
    print("${} dólares son {} bolivares soberanos".format(dolares,resultado_bolivares))
    print(" ")

if __name__ == '__main__':
    run()