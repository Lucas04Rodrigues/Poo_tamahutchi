class Animal():
    def _init_(self,nome, cor):
      self.nome=nome
      self.cor=cor
    def comer(self):
        print(f"O {self.nome} {self.cor} foi comer.... ")
    def EmitirSom(self):
        print(f"O {self.nome} {self.cor} Cantou")
class Gato(Animal):
    def _init_(self,nome, cor):
        super(). _init_( nome, cor)
    def comer(self):
        print(f"O {self.nome} {self.cor} foi comer.... ")
    def EmitirSom(self):
        print(f"O {self.nome} {self.cor} está miando")
class Cachorro(Animal):
    def _init_(self, nome, cor):
        super(). _init_( nome, cor)
    def comer(self):
        print(f"O {self.nome} {self.cor} foi comer.... ")
    def EmitirSom(self):
        print(f"O {self.nome} {self.cor} está lantindo. ")
class Coelho(Animal):
    def _init_(self, nome, cor):
        super()._init_(nome, cor)

    def comer(self):
        print(f"O {self.nome} {self.cor} foi comer.... ")

    def EmitirSom(self):
        print(f"O {self.nome}{self.cor} está ronronando . ")
class Vaca(Animal):
    def _init_(self, nome, cor):
        super()._init_(nome, cor)
    def comer(self):
        print(f"O {self.nome} {self.cor} e está comendo.... ")
    def EmitirSom(self):
        print(f"O {self.nome} {self.cor} está Moando. ")