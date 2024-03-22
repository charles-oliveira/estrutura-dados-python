class Clinica:
    def __init__(self, fila_espera):
        """
        Inicializa a clínica com uma lista vazia de pacientes atendidos
        e uma fila de espera.
        
        Args:
            fila_espera (FilaEspera): Objeto representando a fila de espera da clínica.
        """
        self.pacientes_atendidos = []
        self.fila_espera = fila_espera
    
    def atender_proximo(self):
        if self.fila_espera.tamanho_fila() == 0:
            print('Não há pacientes na fila.')
        else:
            paciente = self.fila_espera.proximo_paciente()
            self.pacientes_atendidos.append(paciente)



class FilaEspera:
    def __init__(self):
        self.lista_espera = []

    def adicionar_paciente(self, paciente):
        self.lista_espera.append(paciente)
        
    def proximo_paciente(self):
        """
        Retorna e remove o próximo paciente da fila de espera.
        
        Returns:
            Paciente: O próximo paciente na fila de espera.
        
        Raises:
            ValueError: Se não houver pacientes na fila de espera.
        """
        if len(self.lista_espera) == 0:
            raise ValueError('Não há mais pacientes.')
        return self.lista_espera.pop(0)
    
    def tamanho_fila(self):
        return len(self.lista_espera)
        

# Testes
fila_espera_exemple = FilaEspera()
fila_espera_exemple.adicionar_paciente('Ana')
fila_espera_exemple.adicionar_paciente('Carlos')


clinica = Clinica(fila_espera_exemple)
clinica.atender_proximo()
clinica.atender_proximo()
print(clinica.pacientes_atendidos)  
print(f"Resta(m) ser(em) atendido(s): {fila_espera_exemple.tamanho_fila()} paciente(s)")  

print('-'*30)
print('Adicionando mais pacientes...')
print('-'*30)

fila_espera_exemple.adicionar_paciente('Maria')
fila_espera_exemple.adicionar_paciente('João')
print(f"Resta(m) ser(em) atendido(s): {fila_espera_exemple.tamanho_fila()} paciente(s)")

