class Animal:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitirSom(self):
        pass

    def correr(self):
        pass


class AnimalInvalidoException(Exception):
    def _init_(self, mensagem):
        super()._init_(mensagem)


class AnimalTeste:
    @staticmethod
    def testarAnimais():
        dog = Cachorro("Rex", 12)
        horse = Cavalo("Thor", 10)
        sloth = Preguica("Side", 5)
        duck = Pato("Donald", 11)

        animals = [dog, horse, sloth, duck]

        for animal in animals:
            print(animal.emitirSom())
            print(animal.correr())


class Cachorro(Animal):
    def _init_(self, nome, idade):
        super()._init_(nome, idade)

    def emitirSom(self):
        return "Au Au"

    def correr(self):
        return self.nome + " está correndo!"


class Cavalo(Animal):
    def _init_(self, nome, idade):
        super()._init_(nome, idade)

    def emitirSom(self):
        return "Relincho"

    def correr(self):
        return self.nome + " está correndo!"


class Main:
    @staticmethod
    def main():
        zoo = Zoologico()

        dog = Cachorro("nasus", 12)
        horse = Cavalo("hecarim", 10)
        sloth = Preguica("Side", 5)
        duck = Pato("Tio Patinhas", 11)

        try:
            zoo.adicionarAnimal(dog)
            zoo.adicionarAnimal(horse)
            zoo.adicionarAnimal(sloth)

            zoo.adicionarAnimal(duck)  
        except AnimalInvalidoException as e:
            print("Erro:", e)

        print()
        zoo.mostrarAnimais()
        print()

        vet = Veterinario()
        try:
            vet.examinar(dog)
            vet.examinar(horse)
            vet.examinar(sloth)

           
            vet.examinar(duck)  
        except AnimalInvalidoException as e:
            print("Erro:", e)

        print()

        AnimalTeste.testarAnimais()


class Pato(Animal):
    def _init_(self, nome, idade):
        super()._init_(nome, idade)

    def emitirSom(self):
        return "quack quack"

    def correr(self):
        return self.nome + " está andando!"


class Preguica(Animal):
    def _init_(self, nome, idade):
        super()._init_(nome, idade)

    def emitirSom(self):
        return "Som de preguiça"

    def correr(self):
        return self.nome + " é uma preguiça e não consegue correr rápido."


class Veterinario:
    def examinar(self, animal):
        if isinstance(animal, (Cachorro, Cavalo, Preguica)):
            print("Examinando", animal.nome + "...")
            print(animal.emitirSom())
        else:
            raise AnimalInvalidoException("Tipo de Animal Inválido = " + animal.nome)


class Zoologico:
    def _init_(self):
        self.jaulas = [None] * 10
        self.contadorJaulas = 0

    def adicionarAnimal(self, animal):
        if self.contadorJaulas < 10:
            if isinstance(animal, (Cachorro, Cavalo, Preguica)):
                self.jaulas[self.contadorJaulas] = animal
                self.contadorJaulas += 1
            else:
                raise AnimalInvalidoException("Tipo de Animal Inválido para ser adicionado ao zoo = " + animal.nome)
        if self.contadorJaulas >= 10:
            print("Zoológico está cheio.")

    def mostrarAnimais(self):
        for animal in self.jaulas:
            if animal is not None:
                print(animal.emitirSom())
                print(animal.correr())


Main.main()