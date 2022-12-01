class Alumno:
    nombre = ""
    nota = 0

    def conocerNota(self, nota):
        self.nota = nota
        return self.nota

    def conocerNombre(self, nombre):
        self.nombre = nombre
        return self.nombre

a = Alumno()
nombreAlumno = a.conocerNombre("Gabriel")
notaAlumno = a.conocerNota(4.5)
print("Nombre del alumno: ", nombreAlumno)
print("La nota de: ", nombreAlumno, " es: ", notaAlumno)