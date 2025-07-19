from src.agent.chat import ChatCarroAgent
from src.db.carros import get_session, listar_carros

def main():
    print("🔧 Iniciando sistema de carros com IA (LLaMA3.1 via Ollama)...")

    session = get_session()
    carros_disponiveis = listar_carros(session)

    print("\n🚗 Carros disponíveis:")
    for carro in carros_disponiveis:
        print(f"  - {carro}")

    print("\n💬 Chat iniciado! (Digite 'sair', 'tchau', 'bye' ou 'exit' para encerrar)")
    agente = ChatCarroAgent(session=session)

    while True:
        pergunta = input("\n👤 Você: ")
        if pergunta.lower() in ["sair", "tchau", "bye", "exit"]:
            print("👋 Encerrando o chat. Até mais!")
            break

        resposta = agente.responder(pergunta)
        print(f"🤖 Agente: {resposta}")


if __name__ == "__main__":
    main()
