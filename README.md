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

Abaixo está a estrutura de diretórios do projeto Flask, com uma explicação de cada pasta e arquivo:

```bash
.
├── CHANGELOG.md
├── Dockerfile
├── .dockerignore
├── README.md
├── entrypoint.sh
├── pyproject.toml
├── uv.lock
├──.env.sample
├── migrations
├── backend
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── extention.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   ├── entity.py
│   │   └── auth.py
│   ├── external
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   └── entity_service.py
│   └── utils
│       ├── logging.py
│       ├── pagination.py
│       ├── utils.py
│       ├── auth.py
│       └── decorators.py
├── certs
│   ├── certificate.crt
│   └── privatekey.key
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_entity.py
```
**Explicação de Cada Arquivo e Diretório**

**Arquivos de Configuração e Documentação**

* CHANGELOG.md: Documento que registra todas as mudanças feitas no projeto ao longo do tempo. Útil para acompanhar o histórico de modificações, como adições de novas features, correções de bugs e melhorias.
* Dockerfile: Arquivo de configuração usado para criar uma imagem Docker da aplicação. Define como a aplicação será construída, quais dependências serão instaladas e como a aplicação será executada em um ambiente Docker.
* .dockerignore: arquivo similar ao `.gitignore` utilizado para especificar quais arquivos e diretórios devem ser ignorados pelo Docker durante a construção de uma imagem. Isso reduz o tamanho da imagem, melhora a performance e minimiza possíveis problemas de segurança.
* README.md: Arquivo de documentação principal do projeto. Inclui instruções de instalação, configuração, execução da aplicação e outras informações relevantes para desenvolvedores.
* entrypoint.sh: Um script shell utilizado para iniciar a aplicação com o servidor Gunicorn. Ele carrega as variáveis de ambiente e executa a aplicação.
* pyproject.toml: arquivo de configuração de projetos em Python para especificar as dependências e metadados do projeto, bem como ferramentas de build, linters, verificadores de tipo, etc. Ele é parte do PEP 518 e substitui o uso de arquivos como `setup.py` em algumas ferramentas modernas de gerenciamento de pacotes, como o uv, Poetry e o Pipenv
* uv.lock: arquivo gerado automaticamente pelo gerenciador de pacote `uv` utilizado no projeto, para garantir a reprodutibilidade do ambiente. Ele contém as versões exatas das dependências instaladas no projeto, garantindo que, ao instalar o projeto em outro ambiente, as mesmas versões dos pacotes sejam utilizadas, evitando incompatibilidades, problemas de versão e problemas de segurança (evitar a instalação de pacotes maliciosos).
* .env.sample: Esse arquivo é um modelo de variáveis de ambiente que a aplicação usa para configurar aspectos como o nome da aplicação, o ambiente de execução, as configurações de rede e o banco de dados.


**Diretório backend/**
Esse diretório contém o código principal da aplicação. Ele está organizado em diferentes subdiretórios para uma melhor separação de responsabilidades.
* __init__.py: Arquivo que inicializa o diretório backend como um módulo Python. Esse arquivo é necessário para que o Python reconheça o diretório como parte de um pacote.
* config.py: Arquivo de configuração que define variáveis importantes da aplicação, como chaves de API, strings de conexão com banco de dados e configurações de ambiente (desenvolvimento, produção, etc.).
* db.py: Esse arquivo contém a inicialização da base de dados
* extention.py: Gerencia a inicialização de extensões do Flask, como a integração Migrate e CORS

**Subdiretório blueprints/**
Os blueprints no Flask permitem uma organização modular da aplicação, separando diferentes rotas e funcionalidades em pequenos componentes.

* blueprints/: Diretório que contém os blueprints da aplicação.
* __init__.py: Inicializa o blueprint do módulo blueprints, permitindo que ele seja importado em outros lugares.
* entity.py: Define as rotas relacionadas a uma entidade específica da aplicação.

**Subdiretório external/**
Esse diretório armazena o código responsável por interações externas.
* __init__.py: Inicializa o módulo external, possibilitando que seus arquivos sejam importados em outros lugares.
* model.py: Define os modelos de dados que são usados para interações externas.
* schemas.py: Define os schemas de validação e serialização de dados usando bibliotecas como marshmallow, para garantir que os dados externos estejam no formato correto.

**Subdiretório services/**
A lógica de negócios é geralmente separada em serviços. Aqui ficam as funções que lidam com as operações de alto nível sobre os dados.
* __init__.py: Inicializa o módulo services.
* entity_service.py: Contém a lógica de negócios para a entidade. Por exemplo, se houver um CRUD (Create, Read, Update, Delete) para uma entidade, toda a lógica de manipulação de dados será tratada aqui, incluindo validações e chamadas ao banco de dados.

**Subdiretório utils/**
Esse diretório contém funções utilitárias e ferramentas de suporte usadas por diferentes partes da aplicação.
* logging.py: Configura o sistema de logging da aplicação, permitindo registrar atividades e eventos importantes durante a execução do código (por exemplo, erros e solicitações).
* pagination.py: Contém a lógica de paginação, usada para dividir grandes conjuntos de dados em partes menores, facilitando o consumo de listas em requisições da API.
* utils.py: Arquivo para funções auxiliares gerais que podem ser usadas em diferentes partes da aplicação.

**Diretório certs/**
Contém os certificados SSL para garantir a segurança da comunicação entre o cliente e o servidor, utilizando HTTPS.
* certificate.crt: O certificado público que é usado para criptografar a comunicação com o servidor.
* privatekey.key: A chave privada que corresponde ao certificado, necessária para estabelecer conexões seguras.

**Diretório migrations/**
Esse diretório é gerado automaticamente pelo Flask-Migrate. Contém os arquivos de migração do banco de dados, que são usados para criar, modificar e gerenciar o esquema do banco ao longo do tempo.

## Como Iniciar

### Requisitos
- [uv](https://docs.astral.sh/uv/) - Gerenciador do projeto e dependências.
  - Recomendação de vídeo que dá um overview sobre a ferramenta: https://www.youtube.com/watch?v=tJYKrViTvJM

Clone e entre no repositório

Crie um ambiente virtual do Python 3.12 usando `uv`:
* No Linux/macOS/Windows:
```bash
uv venv --python 3.12 <NOME_VENV_OPTIONAL>
```
- Por default, caso não seja informado o valor <NOME_VENV_OPTIONAL>, então o nome do ambiente virutal será `.venv`

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
- Esse comando é equivalente ao `pip install -r requirements.txt`,

Como alternativa e para manter a compatibilidade com o `pip`, é possível usar o uv para instalar o `requirements.txt`. Para isso, basta adicionar o comando `uv` antes do `pip` e, dessa forma, pode ser usado como:
```bash
uv pip install -r requirements.txt
```
- Esse comando é equivalente ao próprio `pip install ...` só que mais rápido

Para adicionar uma nova dependência ao projeto:
```bash
uv add <NOME_PACOTE>
```
- Com esse comando além de instalar o pacote ao projeto, também atualiza as dependências no arquivo `pyproject.toml`

Da maneira alternativa, também é possível instalar um pacote de uma forma similar ao `pip install <NOME_PACOTE>`, mantendo a compatibilidade com o `pip`,  basta adicionar o comando `uv` antes do `pip`:
```bash
uv pip install <NOME_PACOTE>
```
- Esse comando é equivalente ao próprio `pip install <NOME_PACOTE>` só que mais rápido, porém não atualiza as dependências no arquivo `pyproject.toml`, por isso, não é recomendado.

## Criar um Arquivo .env:
No terminal, faça uma cópia do arquivo .env.sample e renomeie para .env:
```bash
cp .env.sample .env
```

Abra o arquivo .env e preencha com suas configurações. Exemplo:
```bash
# Configuração do banco de dados: usa SQLite com um arquivo de banco de dados local (em um caminho específico).
DATABASE_URL=sqlite:///database.db

# Exemplo comentado de como conectar a um banco PostgreSQL, incluindo usuário, senha, e banco de dados.
#DATABASE_URL=postgresql://db_user:db_password@localhost/db_dev
```

## Comandos para Migração de Banco de Dados
Aqui estão os principais comandos para gerenciar as migrações do banco de dados usando Flask-Migrate

Criar um repositório de migração:
```bash
flask db init
```
- Observação: vale ressaltar que esse comando só é utilizado apenas uma única vez no projeto, já que esse comando que irá iniciar o diretório `migrations` com as configurações iniciais.

Gerar uma nova versão de migração:
```bash
flask db migrate -m "Init"
```
- O campo `-m` é usado para dar um nome/título para a migration, de forma análoga ao `git commit -m '<MENSAGEM>'`

Aplicar as migrations no banco de dados:
```bash
flask db upgrade
```

(Se necessário) Para reverter uma migration no banco de dados:
```bash
flask db downgrade
```

## Inicie a aplicação em ambiente de desenvolvimento:
Após configurar o ambiente, execute a aplicação com o seguinte comando:
```bash
flask run
```

A API estará rodando em http://FLASK_RUN_HOST:FLASK_RUN_PORT

## Documentação da API com Swagger-UI

Este projeto inclui integração com Swagger-UI para documentação automática da API. Assim que a aplicação estiver rodando, você poderá acessar a documentação no seguinte endereço:

```bash
http://FLASK_RUN_HOST:FLASK_RUN_PORT/apidocs/
```

Aqui, você poderá visualizar e testar os endpoints diretamente da interface do Swagger.