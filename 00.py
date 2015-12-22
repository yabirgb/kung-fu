# -*- coding: utf-8 -*-
# Author: Yabir Garcia
# Email: zanklord@gmail.com

import time

start = time.time()

def evaluar(texto1, texto2):
    return texto1 == texto2 or sorted(texto1) == sorted(texto2)

print evaluar("abcc", "abcc")
print evaluar("acbc", "abcc")
print evaluar("acf", "abcc")

#Ejercicio del email
print evaluar("abcdef", "cafedb")

print "Executed in " + str(time.time() - start) + " seconds"