## Felipe Calvache

import numpy as np
# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)
# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)
# Resta complejos representados como una tupla (real, imaginaria}
def restacplx(a,b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real, img)
# Dividir complejos representados como una tupla (real, imaginaria)
def divcplx(a,b):
    real = ((((m[0] * n[0]) + (m[1] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    img = ((((m[1] * n[0]) - (m[0] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    return (real, img)
# Modulo de un complejo
def modcplx(a, b):
    real = a ** 2
    img = b ** 2
    m = int(real) + int(img)
    mod = m ** 1/2
    return mod
# Conjugado de un complejo
def conjugado(c):
    real = c[0]
    img = -c[1]
    return (real, img)
# Conversión entre representaciones polar y cartesiano
def toPolar(c):
    theta = np.arctan2(c[1],c[0])
    rho = np.sqrt((c[0] * c[0]) + (c[1] * c[1]))
    return (rho, theta)
# Fase de un número complejo 
def Fasecmplx(c):
    fase = np.arctan2(c[1], c[0])
    return fase
def pryttypinting2(s):
    print(round(s), 5)
def prettyprinting(c):
    #Para cartesianos
    print( str(c[0]) + "+" + str(c[1]) + "i")
def polprettyprinting(c):
    #Para polares
    print( str(c[0]) + " e^(i " + str(c[1]) + ")")
prettyprinting(sumacplx((2,3),(4,7)))
prettyprinting(multcplx((2,3),(4,7)))
prettyprinting(restacplx((2,3),(4,7))
prettyprinting(divcplx((2,3),(4,7))
prettyprinting2(modcplx((2,3)))
prettyprinting(conjugado((2, 3)))
polprettyprinting(toPolar((-3,-2)))
prettyprinting2 (Fasecplx((2,3)))
