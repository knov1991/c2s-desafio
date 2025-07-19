# c2s-desafio

Fiz esse projeto para resolver o desafio proposto pela C2S.
O desafio era criar um chatbot que pudesse responder perguntas sobre carros.
O chatbot foi criado usando o LLaMA3.1 via Ollama.

Utilizei UV para rodar o projeto:
```
uv sync
uv run .\main.py
```

Caso não tenha UV instalado, pode usar o pip:
```
pip install -r requirements.txt
python main.py
```


Requisitos:
- Python (versão 3.12 - não testei outras versões)
- Ollama (model usado llama3.1 - https://ollama.com/)
- SQLAlchemy