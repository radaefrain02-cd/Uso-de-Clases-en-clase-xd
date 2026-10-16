class Persona:
    def __init__ (self,nombres,apellidos,edad,estCivil,ci,cel,sexo,ocupacion, correo, direccion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.estCivil = estCivil 
        self.ci = ci
        self.cel = cel
        self.sexo = sexo
        self.ocupacion = ocupacion
        self.correo = correo
        self.direccion = direccion

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombres} eres mayor de edad"
        else:
            return f"{self.nombres} eres menor de edad"

Persona1 = Persona("Carlos","Vaca",10,"Casado",99546542,75646212,"Masculino","Docente","adfoagd@gmail.com","Pampahasi 321")

print(Persona1.es_mayor_de_edad())