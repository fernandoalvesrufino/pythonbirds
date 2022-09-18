class Pessoa:
    olhos = 2                                # Este é o chamado atributo default, ou atributo de classe

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
    print(id(morant))
    print(luka.cumprimentar())
    print(luka.nome)
    print(luka.idade)
    for filho in luka.filhos:
        print(filho.nome)
    luka.sobrenome = 'Doncic'               # Possível adicionar atributos dinamicamente
    del luka.filhos                         # Possível remover atributos dinamicamente
    morant.olhos = 1
    del morant.olhos
    print(luka.__dict__)                    # Mostra quais são os atributos de instância de um objeto
    print(morant.__dict__)                  # O __dict__ não apresenta os atributos de classe, apenas o de instância
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(morant.olhos)                     # a não ser que eu insira o atributo no objeto
    print(luka.olhos)
    print(id(Pessoa.olhos), id(morant.olhos), id(luka.olhos))
