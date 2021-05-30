
from Asignaturas.ModAsignatura import ModAsignatura
from Asignaturas.CtrAsignatura import CtrAsignatura
ctr = CtrAsignatura()

asignatura1 = ModAsignatura(4,'CALCULO DIFERENCIA','CAL.DIFERENCIAL',4,4.5)
ctr.actualizar(asignatura1)
if ctr.actualizar(asignatura1)== True:
    print('Actualizado Correcto')
else:
    print('Actualizado InCorrecto')


#r=ctr.buscar('MATEMATICA BASICA')
r= ctr.buscarId(8)

for i in r:
    print(i[1])
'''
if ctr.ingresar(asignatura1)== True:
    print('Registro guardado')
else:
    print('Error al guardar')

if ctr.eliminar(3)== True:
    print('Registro Eliminar')
else:
    print('Error al Eliminar')
    '''


asignaturas = ctr.consulta()
for p,valor in enumerate(asignaturas):
    print(p,valor)


    #print("{} {}".format(asignatura[0], asignatura[1],asignatura[2],asignatura[3],asignatura[4]))