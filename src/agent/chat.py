from src.agent.prompts import system_prompt
from src.db.carros import Carro
import ollama

class ChatCarroAgent:
    def __init__(self, session):
        self.session = session
        self.messages = [
            { "role": "system", "content": system_prompt }
        ]

    def buscar_carros(self):
        carros = self.session.query(Carro).all()
        return "\n".join([
            f"{carro.marca} {carro.modelo} {carro.motorizacao} ({carro.ano}) | {carro.combustivel} | "
            f"{carro.transmissao} | {carro.cor} | {carro.quilometragem} KM | {carro.portas} portas | R${carro.preco}"
            for carro in carros
        ])

    def responder(self, pergunta: str) -> str:
        carros_str = self.buscar_carros()

        contexto = f"""
        Abaixo está a lista de carros disponíveis no estoque:
        {carros_str}

        Com base nessa lista, responda as perguntas do usuário de forma personalizada.
        """

        self.messages.append({ "role": "user", "content": contexto + "\n\nPergunta: " + pergunta })

        # Usei llama3.1 por já ter ele instalado e já estava usando para estudo
        resposta = ollama.chat(
            model="llama3.1",
            messages=self.messages,
            options={
                "temperature": 0.1,
                "top_p": 0.8,
                "max_tokens": 1024,
                "stream": False,
            }
        )

        conteudo = resposta['message']['content']
        self.messages.append({ "role": "assistant", "content": conteudo })

        return conteudo
