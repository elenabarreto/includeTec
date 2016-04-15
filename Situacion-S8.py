print "________________________________________"
print "-*- CALCULO DEL PROMEDIO DE MATERIAS -*-"
print "________________________________________"
print " "
print " "
print " "
print "_______________________________________________________________________________"
print " "
print "*************** "
print "*  MATEMATICA  *"
print "*************** "
print " "
print " "

notaexm= input ("Ingrese la nota del examen de matematica ")
exam=0.90
print " "
notat1= input ("Ingrese la nota de la tarea 1 de matematica ")
notat2= input ("Ingrese la nota de la tarea 2 de matematica ")
notat3= input ("Ingrese la nota de la tarea 3 de matematica ")
notam=0.10
promnotam = (notat1 +notat2 +notat3)/3
promediomat = (notaexm * exam) + ( promnotam* notam)
print "La nota de matematica es ",promediomat
print " "
print " "

print " "
print "_______________________________________________________________________________"
print " "
#fisica
print " "
print "*************** "
print "*   FISICA     *"
print "*************** "
print " "
print " "
notaexf= input ("Ingrese la nota del examen de fisica ")
examf=0.80

print " "
notat1f= input ("Ingrese la nota de la tarea 1 de fisica ")
notat2f= input ("Ingrese la nota de la tarea 2 de fisica ")

notaf=0.20
promnotaf = (notat1f +notat2f)/2
promediofis = (notaexf * examf) + ( promnotaf* notaf)
print "La nota fisica es ",promediofis
print " "
print " "
print "_______________________________________________________________________________"
print " "

#quimica
print " "
print "*************** "
print "*   QUIMICA   *"
print "*************** "
print " "
print " "
notaexq= input ("Ingrese la nota del examen de quimica ")
exaq=0.85

print " "
notat1q= input ("Ingrese la nota de la tarea 1 de quimica ")
notat2q= input ("Ingrese la nota de la tarea 2 de quimica ")
notat3q= input ("Ingrese la nota de la tarea 3 de quimica ")
notaq=0.15
promnotaq = (notat1 +notat2 +notat3)/3
promedioqui = (notaexq * exaq) + ( promnotaq* notaq)
print "La  nota de quimica es ",promedioqui

promediotot= (promediomat + promediofis +promedioqui)/3

print " "
print " "
print "Promedio total de laS materias ",promediotot
print "_______________________________________________________________________________"
print " "
