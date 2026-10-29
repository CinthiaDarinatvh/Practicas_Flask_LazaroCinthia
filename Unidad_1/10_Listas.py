#Declarando una lista
try:
      materias=["Programacion","Filosofia","Matematicas","Ingles"]
      print(materias[2])
      materias.append("Lengua y comunicacion")
      print(materias)
      materias[1]="Biologia"
      print(materias)
      materias.remove("Matematicas")
      print(materias)
except IndexError:
      print("Indice incorrecto")
