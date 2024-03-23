class RegistroAlunos:
    def __init__(self):
        self.registroAlunos = []

    def adicionar_aluno(self, matricula, nome, idade, nota):
        self.registroAlunos.append({
            "matricula": matricula,
            "nome": nome,
            "idade": idade,
            "nota": nota
        })
    
    def remover_aluno(self, matricula):
        for aluno in self.registroAlunos:
            if aluno["matricula"] == matricula:
                self.registroAlunos.remove(aluno)
                return f"O Aluno(a) com matrícula {matricula} foi removido com sucesso!"
        return "Aluno(a) não encontrado(a)!"

    def buscar_aluno_binario(self, matricula):
        inicio = 0
        fim = len(self.registroAlunos) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.registroAlunos[meio]["matricula"] == matricula:
                aluno_encontrado = self.registroAlunos[meio]
                return f"Aluno encontrado: {aluno_encontrado['nome']} (Matrícula: {aluno_encontrado['matricula']}, Idade: {aluno_encontrado['idade']}, Nota: {aluno_encontrado['nota']})"
            elif self.registroAlunos[meio]["matricula"] < matricula:
                inicio = meio + 1
            else:
                fim = meio - 1
        return "Aluno não encontrado."
    
    def buscar_aluno_sequencial(self, matricula):
        for aluno in self.registroAlunos:
            if aluno["matricula"] == matricula:
                return f"Aluno encontrado: {aluno['nome']} (Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}, Nota: {aluno['nota']})"
        return "Aluno não encontrado."
    
    def listar_alunos(self):
        lista_alunos = ""
        for aluno in self.registroAlunos:
            lista_alunos += f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}\n"
        return lista_alunos

registro_alunos = RegistroAlunos()

registro_alunos.adicionar_aluno(1, "João", 20, 8.5)
registro_alunos.adicionar_aluno(2, "Maria", 21, 9.0)
registro_alunos.adicionar_aluno(3, "José", 22, 7.0)
registro_alunos.adicionar_aluno(4, "Ana", 23, 10.0)

print("Remoção de Aluno:")
print(registro_alunos.remover_aluno(3))

print('--'*30)
print("Busca binária:")
print(registro_alunos.buscar_aluno_binario(2))

print('--'*30)
print("Busca sequencial:")
print(registro_alunos.buscar_aluno_sequencial(4))

print('--'*30)
print("Lista de alunos:")
print(registro_alunos.listar_alunos())
