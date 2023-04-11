
def prom():
    
    for nombre in alumnos:
        promedio.append((calificaciones[nombre][0]+calificaciones[nombre][1])/2)
        print(nombre.rjust(10), str((calificaciones[nombre][0]+calificaciones[nombre][1])/2).rjust(11))
    return promedio

def prom_gen():

    general = sum(promedio)/len(notas_1)
    print('El promedio general es: ',str(round(general,2)))

def alta():

    maximo = promedio.index(max(promedio))
    print(alumnos[maximo], 'tiene el promedio de notas más alto con un valor de', promedio[maximo])

def baja():

    minimo = (notas_1+notas_2).index(min(notas_1+notas_2))
    print(alumnos[minimo], 'tiene la nota más baja con un puntaje de', (notas_1+notas_2)[minimo])


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
promedio = []

#Transformo el string en una lista con formato regular. Cada elemento de la lista representa el nombre del alumno, con la primera letra en mayúscula y el resto en minúscula
alumnos = []

alumnos_aux = nombres.replace('\n', ' ').replace('\'', '').strip(" ").split(',')

for lista in alumnos_aux:
    alumnos.append(lista.strip().capitalize())


#Creo un diccionario para relacionar alumno con calificaciones
calificaciones = {}

for i in range(len(alumnos)):
    calificaciones[alumnos[i]] = (notas_1[i], notas_2[i])

print("""Promedio de calificaciones de cada estudiante
--------------------------------------------------------""")
print("""Estudiante        Calificación promedio""")
print("""--------------------------------------------------------""")
prom()
print("""--------------------------------------------------------""")
prom_gen()
print("""--------------------------------------------------------""")
alta()
print("""--------------------------------------------------------""")
baja()
print("""--------------------------------------------------------""")

