from sqlalchemy import create_engine, text
import os

string_conexao = os.environ['db_conexao_string']
engine = create_engine(string_conexao,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def carrega_vagas_db():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT * FROM vagas"))
        vagas = []
        for vaga in resultado.all():
            vagas.append(vaga._asdict())
        return vagas
