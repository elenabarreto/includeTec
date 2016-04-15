# -*- coding: utf-8 -*-
print "___________________"
print "-*- EJERCICIO 3 -*-"
print "___________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "


presion = input("Ingrese valor de presión: ")
volumen = input("Ingrese valor de volúmen: ")
temperatura = input("Ingrese valor de temperatura: ")

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print("La masa es: ", masa)
