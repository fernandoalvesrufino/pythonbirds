class Pessoa:
    def __init__(self, *filhos, nome=None, idade=22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    morant = Pessoa(nome='Morant')
    luka = Pessoa(morant, nome='Luka')
    print(Pessoa.cumprimentar(luka))
    print(id(luka))
    print(luka.cumprimentar())
    print(luka.nome)
    print(luka.idade)
    for filho in luka.filhos:
        print(filho.nome)
    luka.sobrenome = 'Doncic'               # Possível adicionar atributos dinamicamente
    del luka.filhos                         # Possível remover atributos dinamicamente
    print(luka.__dict__)
    print(morant.__dict__)
