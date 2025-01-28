# Flask API Template

Este repositório contém um template básico para a criação de APIs REST usando Flask, desenvolvido para ser utilizado dentro da **Datamint**. O objetivo deste projeto é fornecer uma base simples para o desenvolvimento de back-ends.

## Tecnologias Utilizadas

- **Framework**: Flask
- **Gerenciamento do projeto/dependências**: uv
- **Containerização**: Docker
- **Servidor HTTP Python WSGI**: Gunicorn
- **ORM**: SQLAlchemy
- **Banco de Dados**: SQLite
- **Migrações de Banco de Dados**: Flask-Migrate
- **Serialização de Validação de Dados**: Marshmallow
- **Documentação da API**: Swagger
- **Testes**: Pytest
- **Plataforma de Deploy**: Google Cloud Run

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

Clone o repositório:

```bash
   git clone https://github.com/datamint-br/flask-rest-api-template-datamint.git
   cd flask-rest-api-template-datamint
```

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

## Executando a aplicação com Gunicorn
Gunicorn é um servidor HTTP WSGI para ambientes UNIX que oferece um método robusto para hospedar aplicações Python em produção.

O entrypoint.sh é um script shell utilizado para iniciar a aplicação com Gunicorn. Ele garante que as variáveis de ambiente sejam carregadas e passa os parâmetros necessários para o Gunicorn. Aqui está um exemplo de conteúdo para o arquivo entrypoint.sh:

```bash
#!/bin/bash
flask db upgrade
exec gunicorn --bind 0.0.0.0:8080 "backend:create_app()" --timeout 100 --workers 4 --certfile=certs/certificate.crt --keyfile=certs/privatekey.key --access-logfile - --error-logfile -;
```

Explicação do Script
- --bind $FLASK_RUN_HOST:$FLASK_RUN_PORT: Define o endereço IP e a porta onde o Gunicorn vai ouvir as solicitações.
- --workers 3: Define o número de workers do Gunicorn para processar as solicitações. Este número deve ser ajustado com base nos recursos do servidor e carga esperada.
- "nome_do_seu_modulo:create_app()": Especifique o módulo e a função de aplicação que o Gunicorn usará para executar a aplicação.

### Execução

Certifique-se de que o script tem permissões de execução, que podem ser atribuídas com:
```bash
chmod +x entrypoint.sh
```

Para iniciar a aplicação, navegue até o diretório do projeto e execute o script entrypoint.sh com o seguinte comando:
```bash
./entrypoint.sh
```


## Executando com Docker

Criação da imagem a partir do Dockerfile
```bash
docker build --tag flask-rest-api-template .
```

Execução do container na máquina local mapeando a porta interna do container (8080) para porta da máquina hospedeira (8080)
```bash
docker run --name instance-flask-template -p 8080:8080 flask-rest-api-template
```

## Segurança

Foram incluídos os seguintes de cabeçalhos de segurança:

- HTTP Strict Transport Security (HSTS): Força o navegador a se comunicar com o site apenas através de HTTPS, mesmo que o usuário digite o endereço com HTTP. Isso previne ataques man-in-the-middle, onde um atacante intercepta a comunicação entre o usuário e o servidor.
- Referrer Policy: Controla a quantidade de informação que o navegador envia no cabeçalho Referer quando um link é clicado. O Referer indica de onde o usuário veio, e essa informação pode ser usada para rastrear usuários.
- X-frame: Determina se uma página pode ser incorporada em um iframe. Isso ajuda a prevenir ataques de clickjacking, onde um atacante engana um usuário para clicar em um elemento oculto em outra página.
- X-XSS Protection: Instrui o navegador a ativar a proteção contra XSS (Cross-Site Scripting). Essa proteção ajuda a prevenir a injeção de código malicioso em uma página web.
- Cross-Origin-Opener-Policy (COOP) e Cross-Origin-Embedder-Policy (COEP): São políticas de segurança que restringem a forma como um documento pode ser incorporado ou abrir pop-ups de outros sites. Isso ajuda a prevenir ataques de framing e phishing.
- Cross-Origin-Resource-Policy (CORP): Permite que você especifique quais tipos de recursos podem ser acessados por outros sites. Isso ajuda a prevenir ataques de CSRF (Cross-Site Request Forgery).

O intuito destes cabelhaços é restringir ataques de diversos tipos, sobretudo, forçar o uso do protocolo HTTPS através do cabeçalho HSTS e do uso de um certificado. O certificado atual é um certificado auto-assinado que foi gerado localmente através da biblioteca OpenSSL usando o seguinte comando:

```bash
openssl req -s 365 -newkey rsa:2048 -keyout privatekey.key -out certificate.crt
```

Com os seguintes parâmetros para fins de teste:

```bash
Country Name (2 letter code) [AU]:BR
State or Province Name (full name) [Some-State]:Rio de Janeiro
Locality Name (eg, city) []:Rio de Janeiro
Organization Name (eg, company) [Internet Widgits Pty Ltd]:datamint
Organizational Unit Name (eg, section) []:desenvolvimento
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:info@datamint.com.br
```

**É fortemente recomendado que cada projeto que instancie esse template crie ou utilize seu próprio certificado, podendo ser auto-assinado (como é o caso deste template) ou assinado por uma autoridade certificadora.**

### JWT

Para incrementar os mecanismos de segurança, criamos um endpoint simples de autenticação, chamado `/authentication`, que gera um token no formato JWT a partir das credenciais de um Auth Basic (username e password), do qual pode ser utilizado para validar as requisições a cada um dos endepoints separadamente. A função `jwt_required` do arquivo `decorators.py` pode ser adicionada em cada endpoint onde deve ser exigido uma autenticação via JWT, como mostra o exemplo abaixo.

```python
@app.get('/endpoint')
@jwt_required
def test(current_user):
    print(current_user)
    return "Token autenticado"
```

A implementação presente neste template serve apenas como um exemplo de geração e consumo (validação nos endpoints) de tokens JWT. Em um contexto real, provavelmente a geração do token será feita por um processo mais complexo (como uma autenticação no AD de uma Cloud, uma consulta do usuário e de suas credenciais em uma base de dados, e assim por diante) e o consumo demandará a validação de mais campos (como assinatura, issuer, etc), mas a implementação atual ainda pode servir como base para outras.

Além disso, também criamos uma nova variável chamada `SECRET_KEY`, que funciona como uma espécie de assinatura digital, garantindo a integridade e a autenticidade do token, e também o atributo `AUDIENCE` que é usado na validação do token.

Para realizar uma requisição passando o token JWT, apresentamos um exemplos a seguir:

```python
import requests

token = '<TOKEN>'
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(
                'https://api.exemplo.com/entities', 
                headers=headers
            )
```

## Testes

### Rodando Testes

Execute o seguinte comando:
```bash
pytest
```

O pytest automaticamente descobre e executa todos os testes que seguem o padrão de nomenclatura test_*.py ou *_test.py.

### Opções Úteis do Pytest

* Exibir mais detalhes:
```bash
pytest -vv
```

* Executar testes em um arquivo específico:
```bash
pytest tests/test_seu_arquivo.py
```

* Executar um teste específico:
```bash
pytest tests/test_seu_arquivo.py::test_nome_do_teste
```

* Gerar um relatório de cobertura de código (necessita do pytest-cov):
```bash
pytest --cov=backend
```

### Adicionando Novos Testes
Ao adicionar novas funcionalidades à aplicação, é importante escrever testes para garantir que o código funciona como esperado. Aqui estão algumas diretrizes para adicionar novos testes:

1. Criar um Arquivo de Teste
	- Coloque os arquivos de teste na pasta tests/.
	- Nomeie o arquivo seguindo o padrão test_nome_do_modulo.py.

Exemplo:
```bash
tests/
├── test_novo_servico.py
```

2. Importar o Módulo a Ser Testado

No seu arquivo de teste, importe as funções ou classes que deseja testar:
```bash
import pytest
from backend.novo_modulo import nova_funcao
```

3. Escrever Funções de Teste
	- Cada função de teste deve começar com test_.
	- Use as fixtures do pytest (mocker, app_context, etc.) conforme necessário.

Exemplo:
```python
def test_nova_funcao_com_caso_sucesso(mocker, app_context):
    # Arrange
    # Configuração dos mocks e dados de entrada

    # Act
    resultado = nova_funcao(parametros)

    # Assert
    assert resultado == valor_esperado
```

4. Usar o pytest-mock para Mocking
	- Utilize o `mocker` fornecido pelo `pytest-mock` para criar mocks e patches.
	- Isso é útil para isolar a função que está sendo testada e simular comportamentos de dependências externas.


Exemplo de uso do mocker:
```python
def test_nova_funcao_erro_no_servico_externo(mocker):
    # Mock da função que chama o serviço externo
    mocker.patch('backend.novo_modulo.servico_externo', side_effect=Exception('Erro no serviço'))

    # Act
    with pytest.raises(Exception) as exc_info:
        nova_funcao(parametros)

    # Assert
    assert 'Erro no serviço' in str(exc_info.value)
```

### Como fazer implantação manual no Google Cloud Run?

1. Testar a aplicação localmente com Docker

Antes de implantar no Google Cloud Run, é importante testar a imagem localmente para garantir que tudo está funcionando corretamente. Siga os passos abaixo:

Construir a imagem Docker local:
```bash
docker build -t <NOME_DA_IMAGEM> .
```

Executar a imagem:
```bash
docker run -p 8080:8080 <NOME_DA_IMAGEM>
```

Verifique se a aplicação está acessível em http://localhost:8080.

2. Fazer login no Google Cloud e configurar o Docker

Antes de enviar sua imagem para o Google Cloud, autentique-se e configure o Docker para trabalhar com o Container Registry:

Autenticar no Google Cloud:

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

3. Criar um repositório no Artifact Registry

Se você ainda não tem um repositório de artefatos, crie um no Google Cloud Artifact Registry:

Criar o repositório:
```bash
gcloud artifacts repositories create <NOME_REPOSITORIO> \
    --repository-format=docker \
    --location=us-central1 \
    --description="Repositório para imagens Docker"
```

Construir e enviar a imagem para o Container Registry

Construir a imagem Docker e enviar para o Container Registry:
```bash
docker build --tag us-central1-docker.pkg.dev/<NOME_DO_PROJETO>/<NOME_REPOSITORIO>/<NOME_DA_IMAGEM> .
```

Fazer o push da imagem para o Google Cloud:
```bash
docker push us-central1-docker.pkg.dev/<NOME_DO_PROJETO>/<NOME_REPOSITORIO>/<NOME_DA_IMAGEM>
```

5. Implantar a imagem no Google Cloud Run

Agora que a imagem está no Container Registry, você pode fazer o deploy no Cloud Run:

> 1. Fazer o deploy da imagem para o Cloud Run:
> - Na interface do Google Cloud, acesse o Artifact Registry.
	> - Encontre a imagem que você acabou de enviar.
	> - Clique nas opções da imagem e selecione “Deploy to Cloud Run”.
> 2.	Configurações recomendadas no Cloud Run:
> - CPU Allocation: Sempre alocar CPU.
> - Minimum number of instances: 1.
> - Ingress control: Allow all traffic.
> - Autoscaling:
>   - Mínimo de instâncias: 0.
>   - Máximo de instâncias: 1.
>   - CPU (vCPUs allocated): 1.


## Automação do Google Cloud via Código

https://dev.to/raviagheda/creating-a-github-action-for-deploying-to-google-cloud-run-using-docker-2ln1

Este guia mostra como automatizar o processo de deploy de uma aplicação Flask no Google Cloud Run, utilizando o GitHub Actions. Isso permite que, a cada push para uma branch específica do repositório GitHub, o código seja automaticamente buildado e deployado no ambiente em nuvem do Google, garantindo uma integração contínua (CI) e entrega contínua (CD).

Guia completo para configurar todas as etapas no Google Cloud (criação de contas de serviço, repositório do Artifact Registry e habilitação de APIs) utilizando o Google Cloud SDK e comandos do gcloud. Este guia é focado em automação para que você possa configurar tudo via linha de comando em vez de fazer manualmente pelo console.

Essa automação inclui:

1.	Configuração de contas de serviço e permissões no Google Cloud: Automação do controle de permissões e gerenciamento de acesso.
2.	Criação de repositórios no Google Artifact Registry: Armazenamento seguro e escalável de imagens Docker.
3.	Deploy automático no Google Cloud Run: Gestão simplificada de containers, executando automaticamente após o build.
4.	Integração com GitHub Actions: Configuração de pipelines de CI/CD para automação segura e eficiente.

Abaixo estão as instruções detalhadas para configurar e executar essa automação.

#### 1. Instalar e Configurar o Google Cloud SDK

Se ainda não tiver o Google Cloud SDK instalado, faça o download e configure-o seguindo este guia oficial.

Após a instalação, autentique-se na sua conta do Google Cloud:
```bash
gcloud auth login
```

Em seguida, defina o projeto que você estará utilizando para as configurações:
```bash
gcloud config set project [PROJECT_ID]
```
Substitua [PROJECT_ID] pelo ID do seu projeto no Google Cloud.

#### 2. Criar a Conta de Serviço via Código

2.1 Criar Conta de Serviço

Use o comando abaixo para criar uma nova conta de serviço. Substitua [SERVICE_ACCOUNT_NAME] pelo nome da sua conta de serviço.
```bash
gcloud iam service-accounts create [SERVICE_ACCOUNT_NAME] \
    --description="Conta de serviço para deploy no Cloud Run" \
    --display-name="Deploy Cloud Run Service Account"
```

2.2 Atribuir Papéis à Conta de Serviço

Agora, atribuímos os papéis necessários para a conta de serviço. Use os comandos abaixo para cada papel:
```bash
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/editor"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.admin"
```

2.3 Criar a Chave da Conta de Serviço

Agora, gere a chave JSON para a conta de serviço, que será usada no GitHub Actions.
```bash
gcloud iam service-accounts keys create ~/key.json \
    --iam-account [SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com
```
O arquivo key.json será salvo no diretório especificado (nesse caso, ~/). Ele deve ser copiado e adicionado como um secret no GitHub.

#### 3. Criar um Repositório no Artifact Registry via Código

Para criar o repositório do Artifact Registry onde sua imagem Docker será armazenada, use o comando abaixo. Substitua [REPOSITORY_NAME] pelo nome do repositório e [REGION] pela região onde o repositório será criado (ex.: us-central1).
```bash
gcloud artifacts repositories create [REPOSITORY_NAME] \
    --repository-format=docker \
    --location=[REGION] \
    --description="Repositório Docker para deploy no Cloud Run"
```

#### 4. Habilitar as APIs Necessárias

As APIs do Google Cloud necessárias para o deploy precisam estar habilitadas. Use os seguintes comandos para habilitar as APIs do Cloud Run e do Artifact Registry:
```bash
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

#### 5. Configurações no GitHub Actions

Agora que o Google Cloud está configurado via código, o próximo passo é adicionar os Secrets no GitHub e configurar o arquivo do workflow do GitHub Actions.

5.1 Adicionar Secrets no GitHub

No GitHub, acesse o repositório e adicione os seguintes secrets nas configurações:

	1.	GCP_SA_KEY: O conteúdo do arquivo key.json gerado na criação da chave da conta de serviço.

5.2 Adicionar variáveis de ambeinte no GitHub

No GitHub, acesse o repositório e adicione os seguintes variáveis de ambeinte nas configurações (as mesmas do arquivo .env.sample):

| Nome da Variável | Valor de Exemplo                   | Descrição                                                                                       |
|------------------|------------------------------------|------------------------------------------------------------------------------------------------ |
| `APP_ENV`        | `local`                            | Define o ambiente de execução da aplicação (ex.: `local`, `development`, `production`).         |
| `APP_NAME`       | `Flask API Rest Template`          | Nome da aplicação que pode ser usado para logs e identificação nos dashboards.                  |
| `DATABASE_URL`   | `sqlite:///database.db`            | URL de conexão com o banco de dados. No exemplo, está configurado para usar SQLite localmente.  |
| `FLASK_APP`      | `backend`                          | Define o nome do módulo ou arquivo principal da aplicação Flask (ex.: `app.py`, `backend`).     |
| `FLASK_DEBUG`    | `true`                             | Habilita o modo de debug do Flask. Use `true` em desenvolvimento e `false` em produção.         |

5.3 Criar o Arquivo de Workflow no GitHub Actions

Agora, crie o arquivo .yml na pasta .github/workflows/ do seu repositório, conforme o exemplo abaixo:
```bash
name: Deploy Cloud Run

# Define o nome do workflow
on:
  push:
    branches:
      - main  # Branch que dispara o deploy. Substitua pela branch de produção desejada.

env:
  PROJECT_ID: poc-eneva-qna  # ID do projeto Google Cloud. Substitua pelo seu próprio.
  GAR_LOCATION: us-central1  # Região onde o Artifact Registry está localizado. Substitua pela sua região.
  REPOSITORY: repository-flask-template  # Nome do repositório no Artifact Registry. Substitua pelo nome do seu repositório.
  SERVICE: flask-template-service  # Nome do serviço no Cloud Run. Substitua pelo nome do seu serviço.

jobs:
  push_container:  # Define o job que será executado. Aqui é onde todas as etapas de build, push e deploy ocorrem.
    permissions:
      contents: 'read'  # Permissão para ler o conteúdo do repositório.
      id-token: 'write'  # Permissão para gerar tokens de identidade, necessário para a autenticação no Google Cloud.

    runs-on: ubuntu-latest  # Define o ambiente onde o job será executado. Neste caso, usa uma máquina Ubuntu mais recente.

    steps:
      - name: Checkout  # Primeiro passo: faz o checkout do código da branch configurada.
        uses: 'actions/checkout@v3'  # Usa a ação padrão do GitHub para fazer o checkout.

      # Autenticação com Google Cloud
      - name: 'Google auth'  # Etapa de autenticação no Google Cloud.
        id: "auth"
        uses: google-github-actions/auth@v1.1.1  # Usa a ação oficial do Google para autenticação no Google Cloud.
        with:
          credentials_json: "${{ secrets.GCP_SA_KEY }}"  # Utiliza o secret 'GCP_SA_KEY', que deve ser configurado no GitHub secrets.

      # Setup do gcloud CLI/SDK
      - name: Set up Cloud SDK  # Instala o SDK do Google Cloud para que os comandos 'gcloud' possam ser usados.
        uses: google-github-actions/setup-gcloud@v1  # Ação oficial para configurar o Google Cloud SDK.

      # Autenticação Docker no Artifact Registry
      - name: 'Docker auth'  # Autentica o Docker para enviar imagens para o Artifact Registry.
        run: |-
          gcloud auth configure-docker ${{ env.GAR_LOCATION }}-docker.pkg.dev  # Configura o Docker para usar o Artifact Registry na região configurada.

      # Build da imagem Docker
      - name: Build Docker image  # Constrói a imagem Docker da aplicação.
        run: |
          docker build -t "${{ env.GAR_LOCATION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}:${{ github.sha }}" .
          # Comando para buildar a imagem Docker. O nome da imagem inclui a localização do Artifact Registry, ID do projeto, nome do repositório, nome do serviço e o SHA do commit atual.

      # Push da imagem Docker para o Artifact Registry
      - name: Push Docker image to Artifact Registry  # Envia a imagem Docker construída para o Artifact Registry.
        run: |
          docker push "${{ env.GAR_LOCATION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}:${{ github.sha }}"
          # Comando para fazer o push da imagem para o Artifact Registry usando o mesmo nome configurado no passo anterior.

      # Deploy no Cloud Run
      - name: Deploy to Cloud Run  # Realiza o deploy da imagem Docker no Cloud Run.
        id: deploy
        uses: google-github-actions/deploy-cloudrun@v1  # Ação oficial para realizar o deploy no Cloud Run.
        with:
          service: ${{ env.SERVICE }}  # Nome do serviço no Cloud Run.
          region: ${{ env.GAR_LOCATION }}  # Região do Cloud Run (deve ser a mesma do Artifact Registry).
          image: "${{ env.GAR_LOCATION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPOSITORY }}/${{ env.SERVICE }}:${{ github.sha }}"  # Imagem que será usada no deploy.
          # NOTE: Aqui podemos inserir as variávaies de ambiente para o Cloud Run
          env_vars: |  # Configura variáveis de ambiente para a aplicação no Cloud Run.
            APP_ENV=${{ vars.APP_ENV }}  # Exemplo de variável de ambiente (pode ser o ambiente da aplicação, ex.: production).
            APP_NAME=${{ vars.APP_NAME }}  # Nome da aplicação.
            DATABASE_URL=${{ vars.DATABASE_URL }}  # URL do banco de dados.
            FLASK_APP=${{ vars.FLASK_APP }}  # Caminho do arquivo Flask principal.
            FLASK_DEBUG=${{ vars.FLASK_DEBUG }}  # Ativa ou desativa o modo de debug do Flask.

      # Exibir a URL do serviço Cloud Run após o deploy
      - name: Show Output  # Exibe a URL do serviço Cloud Run depois que o deploy é feito.
        run: echo ${{ steps.deploy.outputs.url }}  # Mostra a URL que foi gerada pelo Cloud Run após o deploy bem-sucedido.
```

Depois de configurar corretamente o workflow no seu repositório GitHub, a execução do pipeline de deploy será automática sempre que você fizer um commit na branch configurada (no exemplo, a branch main).

Passos para rodar o Workflow:

	1.	Faça um commit na branch correta:
	•	O pipeline está configurado para disparar automaticamente com commits na branch main. Portanto, faça um commit e push das alterações nesta branch ou na branch que você tiver configurado no workflow.
	2.	Acompanhe a execução no GitHub Actions:
	•	Assim que o commit for feito, o GitHub Actions vai começar a executar o workflow. Você pode verificar o status acessando a aba Actions no repositório do GitHub.
	•	Selecione o workflow Deploy Cloud Run para ver o progresso da pipeline. Aqui, você pode visualizar os logs de cada etapa (checkout do código, build da imagem Docker, push para o Artifact Registry, deploy no Cloud Run, etc.).

Verificando que o Deploy foi bem-sucedido:
1.	Verifique a URL do serviço no Cloud Run:
	•	O passo final do pipeline exibe a URL pública gerada pelo Cloud Run para o seu serviço. Você verá algo assim nos logs da etapa Show Output:


```bash
https://<nome-do-servico>-<hash>.a.run.app
```

•	Esta URL é o ponto de entrada para sua aplicação que foi implantada no Cloud Run. Copie essa URL e cole no seu navegador para acessar a aplicação.

Dicas de verificação adicionais:

	•	Logs do Cloud Run: Se houver algum problema com o serviço, você pode verificar os logs do Cloud Run no Google Cloud Console.
	•	Acesse o Cloud Run no Google Cloud Console.
	•	Selecione o serviço implantado (o nome será o que você definiu no arquivo SERVICE no workflow).
	•	Clique em Logs para ver as mensagens de erro ou eventos da sua aplicação.
	•	Verifique o status da execução no GitHub Actions:
	•	No GitHub Actions, cada etapa do pipeline será marcada como Sucesso ou Falha. Se houver falhas, você pode expandir os logs da etapa problemática para investigar e corrigir.



Conclusão

Uma vez configurado o pipeline no GitHub Actions, o deploy para o Google Cloud Run será totalmente automatizado. Cada vez que você fizer um commit na branch configurada, o workflow vai buildar a imagem Docker, enviar para o Artifact Registry e implantar no Cloud Run. A URL gerada pelo Cloud Run será exibida no final do workflow, permitindo que você acesse e verifique a aplicação imediatamente. Caso ocorram erros, você pode acompanhar os logs detalhados no GitHub Actions ou diretamente no Google Cloud Console para resolver quaisquer problemas.

## Contribuições

Contribuições são sempre bem-vindas! Para submeter melhorias ou correções, faça um pull request.

Processo de Aprovação
* Toda alteração será revisada via pull request.
* Um pull request precisa de no mínimo 2 aprovações de engenheiros de back-end da Datamint para ser aceito.
