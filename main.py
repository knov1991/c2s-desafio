from src.db.carros import get_session, listar_carros

def main():
    # Carrega a sessão e listar os carros
    session = get_session()
    carros_disponiveis = listar_carros(session)

    print("\n🚗 Carros disponíveis:")
    for carro in carros_disponiveis:
        print(f"  - {carro}")


if __name__ == "__main__":
    main()
