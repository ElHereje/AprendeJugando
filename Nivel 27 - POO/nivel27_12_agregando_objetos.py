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
    
    def __init__(self, asignatura):
        self.asignatura = asignatura
        self.alumnos = []
        
    def matricular_alumno(self, alunmno):
        self.alumnos.append(alunmno)
        
    def anular_matricula(self, nombre_alunmno):
        self.nombre_alumno = nombre_alunmno

astronomia = Curso("Astronomia")

javier = Alumno("Javier", 30)
susana = Alumno("Susana", 35)
raquel = Alumno("Raquel", 40)

astronomia.matricular_alumno(javier)
astronomia.matricular_alumno(susana)
astronomia.matricular_alumno(raquel)

astronomia.anular_matricula(susana)