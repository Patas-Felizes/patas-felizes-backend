# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)

## [Não publicado]
- Implementar lógica de JWT para validação dos endpoins
- Criar deploy automático no Cloud Run e documentar. Configurar deploy contínuo automático e documentar no README.md.

## [0.0.13] - 2024-10-14
### Adicionado
- Arquivo de workflow com as etapas do GitHub Actions (.github/workflows/pipeline.yaml) para deploy no Google Cloud Run

### Modificado
- Dockerfile: Porta padrão exposta no Dockerfile alterada de 5000 para 8080 para compatibilidade com Cloud Run.
- entrypoint.sh: Ajustes no script de entrada para desativar certificados
- README.md: Atualização para refletir as mudanças no uso da porta 8080 em vez da 5000, além de adição de instruções detalhadas sobre como configurar o pipeline de CI/CD com GitHub Actions e Google Cloud Run.

## [0.0.12] - 2024-10-04

### Adicionado
- Configura o uv como gerenciador do projeto e gerenciador de dependências

## [0.0.11] - 2024-10-02

### Adicionado
- Tutorial de deploy manual no Cloud Run, passo a passo no README.md para o deploy manual no Cloud Run e Documentação estrutura do projeto(pastas, módulos e arquivos)

## [0.0.10] - 2024-10-01

### Adicionado
- Implementação inicial do HTTPS

## [0.0.9] - 2024-09-27

### Adicionado
- Validação de Dados usando Marshmallow.
- Serialização de Dados usando Marshmallow.

## [0.0.8] - 2024-09-26

### Corrigido

- Inclusão das variáveis de ambiente no Dockerfile e exposição da porta 5000;
- Processo de build e execução foi testado e aprovado.

## [0.0.7] - 2024-09-26

### Adicionado
- Função para lidar com paginação, incluindo links para as páginas anteriores e próximas em - backend.ultils.pagination
- Os serviços get_paginated_entities e list_entities_paginated_service que suporta, a paginação dos resultados para Entity.
- O endpoint /entities-paginated para permitir a consulta de entidades de forma paginada.
- Testes para para o novo serviço list_entities_paginated_service

## [0.0.6] - 2024-09-25

### Adicionado
- Modelagem das tabelas usando formato mais moderno do Flask-SQLAlchemy
- Inicialização do Flask-Migrate (+ Alembic)

## [0.0.5] - 2024-09-25

### Adicionado
- Atualizar entrypoint.sh para usar Gunicorn, testar a execução e documentar no README.md
- Testes unitários e documentar no README.md

## [0.0.4] - 2024-09-24

### Adicionado
- Service da entidade entity para reduzir a lógica dentro dos blueprints

## [0.0.3] - 2024-09-20

### Adicionado
- Configurar logs na aplicação

## [0.0.2] - 2024-09-19

### Adicionado
- Arquivo de CHANGELOG.md

### Removido
- arquivo de todo.txt

## [0.0.1] - 2024-09-17

### Adicionado

- Estrutura inicial do projeto com pastas `backend`, `migrations` e `tests`.
- Configuração básica da aplicação `Flask`.
- `requirements.txt` para dependências Python.
- `.env.sample` para variáveis de ambiente.
- Suporte para migrações de banco de dados com `Flask-Migrate`.
- Configuração para `Flask-Migrate` para gerenciar migrações de banco de dados.
- Rotas iniciais da API no módulo `backend`.
