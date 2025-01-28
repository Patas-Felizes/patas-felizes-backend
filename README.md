# Flask API Rest Patas Felizes

## Tecnologias Utilizadas

- **Framework**: Flask
- **Gerenciamento do projeto/dependências**: uv
- **Servidor HTTP Python WSGI**: Gunicorn
- **ORM**: SQLAlchemy
- **Banco de Dados**: SQLite
- **Migrações de Banco de Dados**: Flask-Migrate
- **Serialização de Validação de Dados**: Marshmallow
- **Documentação da API**: Swagger

## Estrutura de Diretórios

```bash
.
├── backend
│   ├── blueprints
│   │   ├── __init__.py
│   │   ├── adocao.py
│   │   ├── adotante.py
│   │   ├── animal.py
│   │   ├── apadrinhamento.py
│   │   ├── auth.py
│   │   ├── campanha.py
│   │   ├── despesa.py
│   │   ├── doacao.py
│   │   ├── entity.py
│   │   ├── estoque.py
│   │   ├── hospedeiro.py
│   │   ├── lar_temporario.py
│   │   ├── procedimento.py
│   │   ├── tarefa.py
│   │   ├── voluntario.py
│   ├── config.py
│   ├── db.py
│   ├── extention.py
│   ├── external
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── adocao_service.py
│   │   ├── adotante_service.py
│   │   ├── animal_service.py
│   │   ├── apadrinhamento_service.py
│   │   ├── campanha_service.py
│   │   ├── despesa_service.py
│   │   ├── doacao_service.py
│   │   ├── entity_service.py
│   │   ├── estoque_service.py
│   │   ├── hospedeiro_service.py
│   │   ├── lar_temporario_service.py
│   │   ├── procedimento_service.py
│   │   ├── tarefa_service.py
│   │   ├── voluntario_service.py
│   ├── utils
│   │   ├── auth.py
│   │   ├── decorators.py
│   │   ├── logging.py
│   │   ├── pagination.py
│   │   ├── utils.py
├── CHANGELOG.md
├── Dockerfile
├── entrypoint.sh
├── instance
│   └── database.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── pyproject.toml
├── README.md
└── uv.lock
```

### Explicação de Cada Arquivo e Diretório

**Arquivos de Configuração e Documentação**
- **CHANGELOG.md**: Histórico de modificações do projeto.
- **Dockerfile**: Configuração para criar uma imagem Docker da aplicação.
- **.dockerignore**: Arquivos e diretórios a serem ignorados pelo Docker.
- **README.md**: Documentação principal do projeto.
- **entrypoint.sh**: Script para iniciar a aplicação com Gunicorn.
- **pyproject.toml**: Configuração de dependências e metadados do projeto.
- **uv.lock**: Arquivo de bloqueio de dependências gerado pelo `uv`.
- **.env.sample**: Modelo de variáveis de ambiente.

**Diretório backend/**
- **__init__.py**: Inicializa o diretório como um módulo Python.
- **config.py**: Configurações da aplicação.
- **db.py**: Inicialização da base de dados.
- **extention.py**: Inicialização de extensões do Flask.

**Subdiretório blueprints/**
- **__init__.py**: Inicializa o módulo blueprints.
- **Arquivos .py**: Definem rotas e funcionalidades específicas da aplicação.

**Subdiretório external/**
- **__init__.py**: Inicializa o módulo external.
- **model.py**: Modelos de dados para interações externas.
- **schemas.py**: Schemas de validação e serialização de dados.

**Subdiretório services/**
- **__init__.py**: Inicializa o módulo services.
- **Arquivos .py**: Lógica de negócios para diferentes entidades.

**Subdiretório utils/**
- **auth.py**: Funções de autenticação.
- **decorators.py**: Decoradores reutilizáveis.
- **logging.py**: Configuração de logging.
- **pagination.py**: Lógica de paginação.
- **utils.py**: Funções auxiliares gerais.

**Diretório migrations/**
- **Arquivos de migração**: Gerenciados pelo Flask-Migrate.

## Como Iniciar

### Requisitos
- [uv](https://docs.astral.sh/uv/) - Gerenciador do projeto e dependências.

Clone e entre no repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

Crie um ambiente virtual do Python 3.12 usando `uv`:

```bash
uv venv --python 3.12
```

Ative o ambiente virtual:

* No Linux/macOS:
```bash
source .venv/bin/activate
```

* No Windows:
```bash
.venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
uv sync
```

## Criar um Arquivo .env

Faça uma cópia do arquivo `.env.sample` e renomeie para `.env`:

```bash
cp .env.sample .env
```

Preencha o arquivo `.env` com suas configurações.

## Comandos para Migração de Banco de Dados

Criar um repositório de migração:

```bash
flask db init
```

Gerar uma nova versão de migração:

```bash
flask db migrate -m "Init"
```

Aplicar as migrations no banco de dados:

```bash
flask db upgrade
```

Reverter uma migration no banco de dados (se necessário):

```bash
flask db downgrade
```

## Inicie a aplicação em ambiente de desenvolvimento

Após configurar o ambiente, execute a aplicação:

```bash
flask run
```

A API estará rodando em `http://FLASK_RUN_HOST:FLASK_RUN_PORT`
- Por padrão, o Flask roda em `http://localhost:5000`

## Documentação da API com Swagger-UI

Acesse a documentação da API em:

```bash
http://FLASK_RUN_HOST:FLASK_RUN_PORT/apidocs/
```
- Exemplo: `http://localhost:5000/apidocs/`