# crear una clase para trabajar con una **Persona**. Agregarle **3 atributos de instancia**, por lo menos** 2 de clase**, el **constructor y dos métodos (uno con parámetros y otro sin parámetro). **
#Luego instanciar a dos personas y mostrarlas por consola. 

class Persona:
    def __init__(self, nombre, edad, genero):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar(self):
        return f"Esto es un saludo y mi nombre es: {self.nombre}."

    def cumplir_anios(self, anios):
        self.edad += anios
        return f"{self.nombre} tiene {self.edad} anios."

# Aca instancio dos personas X
persona1 = Persona("Pepe", 30, "Masculino")
persona2 = Persona("Miriam", 25, "Femenino")

# Muestro data por consola
print(persona1.saludar())
print(persona2.saludar())
print(persona1.cumplir_anios(5))
print(persona2.cumplir_anios(3))


#Crear una clase Atleta, que tenga su nombre, apellido, altura,  peso, teléfono e índice de masa corporal (descripción) . Decidir que atributos deben ser públicos y cuales privados. Crear los métodos get y set que crea necesarios.

#Donde el imc es es peso dividido, la altura al cuadrado. con la altura en metros.

class Atleta:
    def __init__(self, nombre, apellido, altura, peso, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
        self.__imc = self.calculo_imc()

    def calculo_imc(self):
        altura_metros = self.altura / 100 
        return self.peso / (altura_metros ** 2)

    def get_imc(self):
        return self.__imc

    def set_peso(self, nuevo_peso):
        self.peso = nuevo_peso
        self.__imc = self.calculo_imc()

    def get_datos(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "altura": self.altura,
            "peso": self.peso,
            "telefono": self.telefono,
            "imc": self.get_imc()
        }
        
# Aca instancio un atleta
atleta1 = Atleta("Juan", "Perez", 180, 75, "123456789")
print(atleta1.get_datos())

atleta1.set_peso(80)
print(atleta1.get_datos())  

# Modifico la altura
atleta1.altura = 575
print(atleta1.get_datos())

atleta2 = Atleta("Maria", "Lopez", 165, 60, "987654321")
print(atleta2.get_datos())

atleta2.set_peso(90)
print(atleta2.get_datos())  
