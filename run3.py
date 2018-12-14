from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

lista = lista[1:]
lista_personas =[]
for d in lista:
    p = Persona(d[1], d[2], d[3],d[0],d[4], d[5])
    lista_personas.append(p)

operaciones = OperacionesPersona(lista_personas)
print("Promedio notas 1" ,operaciones.obtener_promedio("nota1"))
print("Promedio notas 2" ,operaciones.obtener_promedio("nota2"))
print("Personas con notas menoresa a 15")
print(operaciones.obtener_notas_menores("nota1"))
print(operaciones.obtener_notas_menores("nota2"))
print("Obtener nombres menores que empiezan por R o J" )
print(operaciones.obtener_nombres("R","J","nota1"))
print(operaciones.obtener_nombres("R","J","nota2"))




