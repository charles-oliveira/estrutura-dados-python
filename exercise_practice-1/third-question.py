class FilaAtendimento:
    def __init__(self):
        self.pacientes = {}
        self.fila_prioridade = []

    def adicionar_paciente(self, registro, nome, idade, prioridade):
        paciente_info = {'nome': nome, 'idade': idade, 'prioridade': prioridade}
        self.pacientes[registro] = paciente_info
        self.fila_prioridade.append((prioridade, registro))
        self.fila_prioridade.sort()

    def remover_proximo_paciente(self):
        if not self.fila_prioridade:
            return None
        _, registro = self.fila_prioridade.pop(0)
        paciente = self.pacientes.pop(registro)
        return paciente

    def listar_pacientes(self):
        return [registro for _, registro in self.fila_prioridade]

# Exemplo de uso
fila = FilaAtendimento()

# Adicionando alguns pacientes
fila.adicionar_paciente(1, "João", 30, 2)
fila.adicionar_paciente(2, "Maria", 25, 1)
fila.adicionar_paciente(3, "Pedro", 40, 3)
fila.adicionar_paciente(4, "Ana", 35, 2)

# Listando os pacientes na fila
print("Pacientes na fila:")
print(fila.listar_pacientes())

# Removendo o próximo paciente da fila
proximo_paciente = fila.remover_proximo_paciente()
print("\nPróximo paciente a ser atendido:")
print(proximo_paciente)

# Listando os pacientes novamente após a remoção
print("\nPacientes na fila após a remoção:")
print(fila.listar_pacientes())
