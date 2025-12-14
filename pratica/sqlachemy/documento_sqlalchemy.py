"""
SQLAlchemy

Um kit ferramentas para trabahar com banco de dados SQL e Python
A ideia principal é abstrair as chamadas para drivers especificos
de banco de dados.

O toolkit suporta:

* Async e Sync
* Anotações de tipos e forma dinâmica
* implementa a DBAPI (PEP 249)
* Suporte cPython PyPy
* ORM
* Sistemas de plugins
* Eventos 

Inicial em 2005 primeira release em 2006
Criando por Michel Bayer
    * SQLAlchemy 
    * MAKO
    * Alembic
Atualizado na versão 2.0.27
Licença MIT
Cross Plataforma

# pip install sqlachemy
"""

# |=====================================================================================|

"""
Um entendimento geral

ORM:
Object Relational Mapper (ORM)
-----------------------------------------------------------------------------------------------
CORE:
Schema / type - SQL Expression language - Engine
Connection Pooling Dialect
------------------------------------------------------------------------------------------------
DBAPI

Explicando o CORE:

O core é o componenete mais basico do SQLAlchemy. Responsável por
criar a conexão com banco de dados, fazer buscas e definir tipos.

Alguns componentes importantes são:

Engine:
    * Connection: interface parece comunicar com o banco
    * Dialeto: Mecanismos especificos para cada banco de dados
    * Pool: Deixa conexão em memória para ser mais facil reutilização
SQL Expression Language: Construções em Python para representar SQL
SCHEMAS/TYPES: Contruções em python que representam tabelas, colunas e tipos de dados. 

Engine:

A engine, é o coração do alchemy, é ma fárica de conexões com o banco de dados

O objetivo dela é que de forma dinâmica podemos nos comunicar com diferentes drivers de banco
de dados usando dialetos especificos para cada banco de dados

Engine
    ----> Dialeto
                ----> DBAPI

Dialetos:

A engine fabrica de conexão com a base de dados especifica usando os 
dialetos, Dialetos são chamados diretas para os divers especificos para 
databases especificos.

Por exemplos, o SQLAlchemy suporta nativamente:

    * SQLite
    * PostgreSQL
    * MySQL / MariaDB
    * Oracle
    * Microsoft SQL Server

Contando com diversas implementações via pluging como CookroachDB,
Firebird, Amazon Redshift, etc.

Pool:

Uma instrução relativamente cara de IO é criação de conexão com o
banco de dados. Por esse motivo, o sqlalchemy armazenamento as conexões
em um 'reservatório' de conexão. chamado Pool.

ACID
A = Atomicidade
conceito de atomicidade, é quando num banco de dados, 
garante que as coisas funcione de forma concistente.

Result:

O resultado obtido no executado

O resultado obtido no execute é um objeto chamado Result ele
implementa diversos métodos, além de ser um iterável

    * fatchone() pega o primeiro
    * fatchmany(3) partimos(3) pega alguns valores
    * fatchall() pega todos os valores
    * first() pega 1, mas não da erro se não conseguir 

"""

