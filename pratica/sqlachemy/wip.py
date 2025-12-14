from sqlalchemy import create_engine # fabrica de conexões
 
# Criando banco de dados em memória
engine = create_engine(
    #'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
    'sqlite://'
)

# print(engine)
# print(engine.dialect)

conn = engine.connect()

print(conn)

conn.close()