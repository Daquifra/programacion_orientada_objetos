from errno import EADDRNOTAVAIL


class Persona:
    def __init__(self,color,edad,estatura,nombre):
        self.color = color 
        self.edad = edad 
        self.estatura = estatura
        self.nombre = nombre 
    
    def saltar(self):
        print('Estoy saltanto')

persona = Persona('café',60,175,'Santiago')
print(persona.saltar())

    