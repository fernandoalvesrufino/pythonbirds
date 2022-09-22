class Pessoa:
    olhos = 2                                # Este é o chamado atributo default, ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod                                     # decorator
    def metodo_estatico():                            # Funciona como uma função atrelada a classe e independe do objeto
        return 42                                     # não precisa receber atributo

    @classmethod
    def nome_e_atributos_de_classe(cls):              # Utilizado quando quero acessar dados da própria classe
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):                           # Sobrescrita de método
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3                                         # Sobrescrita de atributo de classe


if __name__ == '__main__':
    morant = Mutante(nome='Morant')
    luka = Homem(morant, nome='Luka')
    print(Pessoa.cumprimentar(luka))
    print(id(luka))
    print(id(morant))
    print(luka.cumprimentar())
    print(luka.nome)
    print(luka.idade)
    for filho in luka.filhos:
        print(filho.nome)
    luka.sobrenome = 'Doncic'               # Possível adicionar atributos dinamicamente
    del luka.filhos                        # Possível remover atributos dinamicamente
    morant.olhos = 1
    del morant.olhos
    print(luka.__dict__)                    # Mostra quais são os atributos de instância de um objeto
    print(morant.__dict__)                  # O __dict__ não apresenta os atributos de classe, apenas o de instância
    print(Pessoa.olhos)
    print(morant.olhos)                     # a não ser que eu insira o atributo no objeto
    print(luka.olhos)
    print(id(Pessoa.olhos), id(morant.olhos), id(luka.olhos))
    print(Pessoa.metodo_estatico(), morant.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), morant.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(morant, Pessoa))
    print(isinstance(morant, Homem))
    print(morant.olhos)
    print(luka.cumprimentar())
    print(morant.cumprimentar())


