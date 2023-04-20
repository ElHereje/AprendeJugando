'''programa que gestione la matriculación de alumnos
en determinados cursos.
definir métodos que:
* agregen alumnos al curso
* eliminen alumnos del curso.
* defina la edad media de los alumnos'''

class Alumno:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return self.nombre
    
    
class Curso:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def __str__(self):
        return self.nombre
        
    def matricular_alumno(self, alunmno):
        self.alumnos.append(alunmno)
        
    def anular_matricula(self, alumno):
        self.alumnos.remove(alumno)

    def edad_media_alumno(self):
        media = 0
        for alumno in self.alumnos:
            media += alumno.edad
        media = media / len(self.alumnos)
        return media
    
    def mostrar_alumnos(self):
        print(f"Alumnos del curso {self}:")
        for alumno in self.alumnos:
            print(f"- {alumno}")

astronomia = Curso("Astronomia")

javier = Alumno("Javier", 30)
susana = Alumno("Susana", 35)
raquel = Alumno("Raquel", 40)

astronomia.matricular_alumno(javier)
astronomia.matricular_alumno(susana)
astronomia.matricular_alumno(raquel)

astronomia.anular_matricula(susana)

# esto lo vamos a realizar con el método "Mostrar alumnos"
# print(f"Alumnos del curso {astronomia}:")
# for alumno in astronomia.alumnos:
#     print(f"- {alumno}")
astronomia.mostrar_alumnos()

print(f"Edad media del curso {astronomia}: {astronomia.edad_media_alumno()}")
