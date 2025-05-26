class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade


p1 = Produto("Arroz", "R$24,00", 300)
p2 = Produto("Feijão", "R$06,99", 220)


print(p1.nome, p1.preço, p1.quantidade)  
print(p2.nome, p2.preço, p2.quantidade)  