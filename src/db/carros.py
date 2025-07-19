from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()

class Carro(Base):
    __tablename__ = "carros"
    
    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    motorizacao = Column(Numeric(2, 1))
    combustivel = Column(String)
    cor = Column(String)
    quilometragem = Column(Integer)
    portas = Column(Integer)
    transmissao = Column(String)
    preco = Column(Integer)

def gerar_carros_fake(session, quantidade=20):
    tuplas_marca_modelo = [
        ("Volkswagen", "Gol"),
        ("Volkswagen", "Polo"),
        ("Volkswagen", "T-Cross"),
        ("Chevrolet", "Onix"),
        ("Chevrolet", "Tracker"),
        ("Chevrolet", "Spin"),
        ("Fiat", "Uno"),
        ("Fiat", "Argo"),
        ("Fiat", "Pulse"),
        ("Toyota", "Corolla"),
        ("Toyota", "Hilux"),
        ("Toyota", "Yaris"),
        ("Ford", "Ka"),
        ("Ford", "EcoSport"),
        ("Ford", "Fusion"),
        ("Renault", "Sandero"),
        ("Renault", "Duster"),
        ("Hyundai", "HB20"),
        ("Hyundai", "Creta"),
        ("Nissan", "Kicks"),
        ("Nissan", "Versa"),
        ("Honda", "Civic"),
        ("Honda", "Fit"),
        ("Honda", "HR-V"),
    ]

    for _ in range(quantidade):
        marca, modelo = random.choice(tuplas_marca_modelo)
        carro = Carro(
            marca=marca,
            modelo=modelo,
            ano=random.randint(2000, 2025),
            motorizacao=random.choice(["1.0", "1.3", "1.5", "1.6", "2.0", "2.5", "3.0"]),
            combustivel=random.choice(["Gasolina", "Diesel", "Eletrico", "Hibrido"]),
            cor=random.choice(["Preto", "Branco", "Cinza","Azul", "Verde", "Vermelho"]),
            quilometragem=random.randint(0, 100000),
            portas=random.randint(2, 5),
            transmissao=random.choice(["Manual", "Automatico"]),
            preco=random.randint(10000, 1000000),
        )
        session.add(carro)
    session.commit()

def get_session():
    engine = create_engine('sqlite:///carros.db')
    
    # Coloquei para remover e recriar todos os carros novamente para sempre ter dados novos para teste
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    gerar_carros_fake(session)

    return session

def listar_carros(session):
    carros = session.query(Carro).all()
    return [
        f"{carro.marca} {carro.modelo} {carro.motorizacao} ({carro.ano}) | {carro.combustivel} | "
        f"{carro.transmissao} | {carro.cor} | {carro.quilometragem} KM | {carro.portas} portas | R${carro.preco}"
        for carro in carros
    ]
