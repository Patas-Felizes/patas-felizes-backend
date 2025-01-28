from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    
class AnimalSchema(Schema):
    animal_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    idade = fields.Str(required=True)
    foto = fields.Str(required=True)
    descricao = fields.Str(required=True)
    sexo = fields.Str(required=True)
    castracao = fields.Str(required=True)
    status = fields.Str(required=True)
    especie = fields.Str(required=True)
    data_cadastro = fields.Str(required=True)

class AdocaoSchema(Schema):
    adocao_id = fields.Int(dump_only=True)
    animal_id = fields.Int(required=True)
    adotante_id = fields.Int(required=True)
    companha_id = fields.Int(required=True)
    data_devolucao = fields.Str(required=True)
    motivo_devolucao = fields.Str(required=True)
    data_adocao = fields.Str(required=True)
    data_cadastro = fields.Str(required=True)

class AdotanteSchema(Schema):
    adotante_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    moradia = fields.Str(required=True)

class LarTemporarioSchema(Schema):
    lar_temporario_id = fields.Int(dump_only=True)
    animal_id = fields.Int(required=True)
    hospedeiro_id = fields.Int(required=True)
    periodo = fields.Str(required=True)
    data_hospedagem = fields.Str(required=True)
    data_cadastro = fields.Str(required=True)

class HospedeiroSchema(Schema):
    hospedeiro_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    moradia = fields.Str(required=True)

class ApadrinhamentoSchema(Schema):
    apadrinhamento_id = fields.Int(dump_only=True)
    animal_id = fields.Int(required=True)
    nome_apadrinhador = fields.Str(required=True)
    valor = fields.Str(required=True)
    regularidade = fields.Str(required=True)

class ProcedimentoSchema(Schema):
    procedimento_id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    valor = fields.Str(required=True)
    data_procedimento = fields.Str(required=True)
    animal_id = fields.Int(required=True)
    voluntario_id = fields.Int(required=True)
    despesa_id = fields.Int(required=True)

class CampanhaSchema(Schema):
    campanha_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    tipo = fields.Str(required=True)
    data_inicio = fields.Str(required=True)
    data_termino = fields.Str(required=True)
    descricao = fields.Str(required=True)
    local = fields.Str(required=True)

class DoacaoSchema(Schema):
    doacao_id = fields.Int(dump_only=True)
    doador = fields.Str(required=True)
    valor = fields.Str(required=True)
    data_doacao = fields.Str(required=True)
    animal_id = fields.Int(required=True)
    companha_id = fields.Int(required=True)
    estoque_id = fields.Int(required=True)
    comprovante = fields.Str(required=True)

class DespesaSchema(Schema):
    despesa_id = fields.Int(dump_only=True)
    valor = fields.Str(required=True)
    data_despesa = fields.Str(required=True)
    tipo = fields.Str(required=True)
    animal_id = fields.Int(required=True)
    procedimento_id = fields.Int(required=True)
    comprovante = fields.Str(required=True)

class EstoqueSchema(Schema):
    estoque_id = fields.Int(dump_only=True)
    categoria = fields.Str(required=True)
    tipo_item = fields.Str(required=True)
    descricao = fields.Str(required=True)
    especie_animal = fields.Str(required=True)
    quantidade = fields.Str(required=True)
    quantidade_total = fields.Str(required=True)

class TarefaSchema(Schema):
    tarefa_id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    data_tarefa = fields.Str(required=True)
    voluntario_id = fields.Int(required=True)
    animal_id = fields.Int(required=True)

class VoluntarioSchema(Schema):
    voluntario_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    foto = fields.Str(required=True)
    email = fields.Str(required=True)
    telefone = fields.Str(required=True)

class DespesaSchema(Schema):
    despesa_id = fields.Int(dump_only=True)
    valor = fields.Str(required=True)
    data_despesa = fields.Str(required=True)
    tipo = fields.Str(required=True)
    animal_id = fields.Int(required=True)
    procedimento_id = fields.Int(required=True)
    comprovante = fields.Str(required=True)

class EstoqueSchema(Schema):
    estoque_id = fields.Int(dump_only=True)
    categoria = fields.Str(required=True)
    tipo_item = fields.Str(required=True)
    descricao = fields.Str(required=True)
    especie_animal = fields.Str(required=True)
    quantidade = fields.Str(required=True)
    quantidade_total = fields.Str(required=True)

class TarefaSchema(Schema):
    tarefa_id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    data_tarefa = fields.Str(required=True)
    voluntario_id = fields.Int(required=True)
    animal_id = fields.Int(required=True)

class VoluntarioSchema(Schema):
    voluntario_id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    foto = fields.Str(required=True)
    email = fields.Str(required=True)
    telefone = fields.Str(required=True)