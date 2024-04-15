class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local
    
    def __str__(self):
        return f"Título: {self.titulo}\nData: {self.data}\nHora: {self.hora}\nLocal: {self.local}\n"

class AgendaEventos:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def editar_evento(self, indice, novo_evento):
        if 0 <= indice < len(self.eventos):
            self.eventos[indice] = novo_evento
            print("Evento editado com sucesso!")
        else:
            print("Índice inválido!")

    def remover_evento(self, indice):
        if 0 <= indice < len(self.eventos):
            del self.eventos[indice]
            print("Evento removido com sucesso!")
        else:
            print("Índice inválido!")

    def listar_eventos(self):
        for i, evento in enumerate(self.eventos):
            print(f"Evento {i+1}:")
            print(evento)

if __name__ == "__main__":
    agenda = AgendaEventos()

    # Adicionando alguns eventos de exemplo
    evento1 = Evento("Reunião de equipe", "2024-04-15", "10:00", "Sala de Conferências")
    evento2 = Evento("Almoço com cliente", "2024-04-17", "12:30", "Restaurante X")
    evento3 = Evento("Apresentação do Projeto", "2024-04-20", "15:00", "Escritório do Cliente")

    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)
    agenda.adicionar_evento(evento3)

    # Listando todos os eventos
    print("Lista de Eventos:")
    agenda.listar_eventos()

    # Editando um evento existente
    novo_evento = Evento("Entrevista de Emprego", "2024-04-18", "09:00", "Escritório da Empresa")
    agenda.editar_evento(1, novo_evento)

    # Listando todos os eventos após a edição
    print("\nLista de Eventos após edição:")
    agenda.listar_eventos()

    # Removendo um evento
    agenda.remover_evento(2)

    # Listando todos os eventos após a remoção
    print("\nLista de Eventos após remoção:")
    agenda.listar_eventos()