import pytest
from backend.services.entity_service import (
    get_all_entities,
    list_entities_service,
    get_entity_by_id,
    get_entity_service,
    insert_entity_service,
    list_entities_paginated_service
)
from backend.external.model import EntityModel
from backend.db import db

# Testes para get_all_entities
# def test_get_all_entities_returns_entities(mocker, app_context):
#     # Arrange
#     mock_entity = mocker.Mock()
#     mock_query = mocker.Mock()
#     mock_query.all.return_value = [mock_entity]
#     mocker.patch('backend.services.entity_service.EntityModel.query', mock_query)

#     # Act
#     with app_context:  # Certifique-se de que o contexto da aplicação esteja ativo durante o teste
#         result = get_all_entities()

#     # Assert
#     assert result == [mock_entity]


# def test_get_all_entities_returns_empty_list(mocker, app_context):
#     # Arrange
#     mock_query = mocker.Mock()
#     mock_query.all.return_value = []
#     mocker.patch('backend.services.entity_service.EntityModel.query', mock_query)

#     # Act
#     result = get_all_entities()

#     # Assert
#     assert result == []


def test_list_entities_service_returns_entities(mocker,app_context):
    # Arrange
    mock_entity1 = mocker.Mock()
    mock_entity1.serialize = {'id': 1, 'attr1': 'valor1', 'attr2': 'valor2'}
    mock_entity2 = mocker.Mock()
    mock_entity2.serialize = {'id': 2, 'attr1': 'valor3', 'attr2': 'valor4'}
    mock_result_data = [mock_entity1.serialize, mock_entity2.serialize]
    mocker.patch('backend.services.entity_service.get_all_entities', return_value=[mock_entity1, mock_entity2])

    # Act
    result = list_entities_service()

    # Assert
    assert result['status'] == 200
    # Assert
    assert result['data'] == mock_result_data


def test_get_all_entities_returns_empty_list(mocker, app_context):

    # Arrange
    mock_result_data = []
    mocker.patch('backend.services.entity_service.get_all_entities', return_value=mock_result_data)

    # Act
    result = list_entities_service()

    # Assert
    assert result['status'] == 404
    assert result['message'] == "Nenhuma entidade encontrada no banco de dados."

def test_list_entities_service_exception(mocker,app_context):
    # Arrange
    mock_get_all_entities = mocker.patch('backend.services.entity_service.get_all_entities', side_effect=Exception('Erro no banco de dados'))

    # Act
    result = list_entities_service()

    # Assert
    assert result['status'] == 500
    assert 'Erro ao consultar ou listar entidades' in result['message']
    assert 'Erro no banco de dados' in result['message']
    assert 'traceback' in result

# Testes para get_entity_service
def test_get_entity_service_entity_found(mocker,app_context):
    # Arrange
    mock_entity = mocker.Mock()
    mock_entity.serialize = {'id': 1, 'attr1': 'valor1', 'attr2': 'valor2'}
    mocker.patch('backend.services.entity_service.get_entity_by_id', return_value=mock_entity)

    entity_id = 1

    # Act
    result = get_entity_service(entity_id)

    # Assert
    assert result['status'] == 200
    assert result['data'] == mock_entity.serialize

def test_get_entity_service_entity_not_found(mocker,app_context):
    # Arrange
    mocker.patch('backend.services.entity_service.get_entity_by_id', return_value=None)
    entity_id = 1

    # Act
    result = get_entity_service(entity_id)

    # Assert
    assert result['status'] == 404
    assert result['message'] == f"Entidade com ID {entity_id} não foi encontrada."

def test_get_entity_service_exception(mocker,app_context):
    # Arrange
    mocker.patch('backend.services.entity_service.get_entity_by_id', side_effect=Exception('Erro no banco de dados'))
    entity_id = 1

    # Act
    result = get_entity_service(entity_id)

    # Assert
    assert result['status'] == 500
    assert f"Erro ao consultar a entidade com ID {entity_id}" in result['message']
    assert 'Erro no banco de dados' in result['message']
    assert 'traceback' in result

# Testes para insert_entity_service
def test_insert_entity_service_no_content():
    # Arrange
    content = None

    # Act
    result = insert_entity_service(content)

    # Assert
    assert result['status'] == 400
    assert result['message'] == "Erro de validação"

def test_insert_entity_service_missing_attributes():
    # Arrange
    content = {'attr1': 'valor1'}  # 'attr2' está faltando

    # Act
    result = insert_entity_service(content)

    # Assert
    assert result['status'] == 400
    assert result['message'] == "Erro de validação"

def test_insert_entity_service_success(mocker):
    # Arrange
    content = {'attr1': 'valor1', 'attr2': '2'}

    mock_entity_instance = mocker.Mock()
    mock_entity_instance.entity_id = 1
    mock_entity_instance.attr1 = content['attr1']
    mock_entity_instance.attr2 = content['attr2']

    mock_entity_model = mocker.patch('backend.services.entity_service.EntityModel', return_value=mock_entity_instance)
    mock_session_add = mocker.patch('backend.services.entity_service.db.session.add')
    mock_session_commit = mocker.patch('backend.services.entity_service.db.session.commit')

    # Act
    result = insert_entity_service(content)

    # Assert
    mock_session_add.assert_called_once_with(mock_entity_instance)
    mock_session_commit.assert_called_once()
    assert result['status'] == 200
    assert result['data'] == {
        'id': 1,
        'attr1': 'valor1',
        'attr2': '2'
    }

def test_insert_entity_service_exception(mocker):
    # Arrange
    content = {'attr1': '1', 'attr2': '2'}

    mock_entity_instance = mocker.Mock()
    mock_entity_model = mocker.patch('backend.services.entity_service.EntityModel', return_value=mock_entity_instance)
    mock_session_add = mocker.patch('backend.services.entity_service.db.session.add', side_effect=Exception('Erro no banco de dados'))

    # Act
    result = insert_entity_service(content)

    # Assert
    assert result['status'] == 500
    assert 'Erro ao inserir dados da entidade' in result['message']
    assert 'Erro no banco de dados' in result['message']
    assert 'traceback' in result

#Testa se a função retorna corretamente uma lista de entidades paginadas.
def test_list_entities_service_with_entities(mocker,app_context):

    # Arrange
    mock_entity1 = mocker.Mock()
    mock_entity1.serialize = {'id': 1, 'attr1': 'valor1', 'attr2': 'valor2'}
    mock_entity2 = mocker.Mock()
    mock_entity2.serialize = {'id': 2, 'attr1': 'valor3', 'attr2': 'valor4'}
    mock_result_data = [mock_entity1, mock_entity2]

    mock_paginated_entities = mocker.patch('backend.services.entity_service.get_paginated_entities')
    mock_paginated = mock_paginated_entities.return_value
    mock_paginated.items = mock_result_data


    mock_paginated.page = 1
    mock_paginated.per_page = 10
    mock_paginated.total = 2
    mock_paginated.pages = 1
    mock_paginated.has_next = False
    mock_paginated.has_prev = False
    mock_paginated.next_num = None
    mock_paginated.prev_num = None

    # Act
    response = list_entities_paginated_service(page=1, per_page=10)

    # Assert
    assert response["status"] == 200
    assert len(response["data"]) == 2
    assert response["data"][0] == {'id': 1, 'attr1': 'valor1', 'attr2': 'valor2'}
    assert response["pagination"]["page"] == 1
    assert response["pagination"]["per_page"] == 10
    assert response["pagination"]["total_items"] == 2
    assert response["pagination"]["total_pages"] == 1
    assert response["pagination"]["next_page"] is None

def test_list_entities_service_no_entities(mocker, app_context):
    """
    Testa o caso onde não há entidades para a página solicitada.
    """
    # Arrange
    # Mock do resultado da paginação sem entidades
    mock_paginated_entities = mocker.patch('backend.services.entity_service.get_paginated_entities')
    mock_paginated = mock_paginated_entities.return_value
    mock_paginated.items = []
    mock_paginated.page = 1
    mock_paginated.per_page = 10
    mock_paginated.total = 0
    mock_paginated.pages = 1
    mock_paginated.has_next = False
    mock_paginated.has_prev = False
    mock_paginated.next_num = None
    mock_paginated.prev_num = None

    # Act
    response = list_entities_paginated_service(page=1, per_page=10)

    # Assert
    print(response)
    assert response["status"] == 404
    assert response["message"] == "Nenhuma entidade encontrada no banco de dados para a página 1 com 10 itens por página."

def test_list_entities_service_exception(mocker, app_context):
    """
    Testa o caso onde uma exceção é lançada.
    """
    # Arrange
    # Mock para simular uma exceção
    mock_paginated_entities = mocker.patch('backend.services.entity_service.get_paginated_entities')
    mock_paginated_entities.side_effect = Exception("Erro inesperado")

    # Act
    response = list_entities_paginated_service(page=1, per_page=10)

    # Assert
    print(response)
    assert response["status"] == 500
    assert "Erro ao consultar ou listar entidades" in response["message"]
    assert "Erro inesperado" in response["message"]