class Mamifero:
    def caminar(self):
        raise Exception("Este metodo solopuede ser implementado en las subclasees")
    def nadar(self):
        raise Exception("Este metodo solopuede ser implementado en las subclasees")

class Perro(Mamifero):
    def caminar(self):
        print("EL perro camina")

class Ballena(Mamifero):
    def nadar(self):
        print("La ballena nada")


if __name__=="__main__":
perro = Perro()
ballena = Ballena()

perro.caminar()
ballena.nadar()
