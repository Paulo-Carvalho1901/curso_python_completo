from sqlalchemy import create_engine # fabrica de conexões
 
# Criando banco de dados em memória
engine = create_engine(
    #'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
    'sqlite://'
)

print(engine.pool)

# print(engine)
# print(engine.dialect)

conn1 = engine.connect()
conn2 = engine.connect()
conn1.close
conn2.close
conn3 = engine.connect()

print(engine.pool.status())

# conn.close()