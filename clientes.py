class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.nota = nota
        self.turma = turma  


# Criando objetos
a1 = Aluno("Maria", "1C", 70)
a2 = Aluno("João", "3A", 18)


print(a1.nome, a1.nota, a1.turma)
print(a2.nome, a2.nota, a2.turma) 