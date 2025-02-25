from sqlalchemy.orm import Mapped, mapped_column
from backend.db import db
from werkzeug.security import generate_password_hash, check_password_hash

# === User ===
from backend.external.schemas import UserSchema

class UserModel(db.Model):
    __tablename__ = "tab_user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def serialize(self):
        """
        Retorna os dados do usuário em formato de dicionário, 
        usando o schema do Marshmallow.
        """
        schema = UserSchema()
        return schema.dump(self)
    
    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)
    
# === Animal ===
from backend.external.schemas import AnimalSchema
from sqlalchemy import LargeBinary

class AnimalModel(db.Model):
    __tablename__ = "tab_animal"
    animal_id: Mapped[int] = mapped_column("animal_id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", nullable=False)
    idade: Mapped[str] = mapped_column("idade", nullable=False)
    foto: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)  # Alterado para LargeBinary
    descricao: Mapped[str] = mapped_column("descricao", nullable=False)
    sexo: Mapped[str] = mapped_column("sexo", nullable=False)
    castracao: Mapped[str] = mapped_column("castracao", nullable=False)
    status: Mapped[str] = mapped_column("status", nullable=False)
    especie: Mapped[str] = mapped_column("especie", nullable=False)
    data_cadastro: Mapped[str] = mapped_column("data_cadastro", nullable=False)

    def __init__(self, nome, idade, foto, descricao, sexo, castracao, status, especie, data_cadastro):
        self.nome = nome
        self.idade = idade
        self.foto = foto  # Agora recebe bytes diretamente
        self.descricao = descricao
        self.sexo = sexo
        self.castracao = castracao
        self.status = status
        self.especie = especie
        self.data_cadastro = data_cadastro
        
    @property
    def serialize(self):
        schema = AnimalSchema()
        return schema.dump(self)
    
# === Adoção ===
from backend.external.schemas import AdocaoSchema

class AdocaoModel(db.Model):
    __tablename__ = "tab_adocao"

    adocao_id: Mapped[int] = mapped_column("adocao_id", primary_key=True)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    adotante_id: Mapped[int] = mapped_column("adotante_id", nullable=False)
    companha_id: Mapped[int] = mapped_column("companha_id", nullable=False)
    data_devolucao: Mapped[str] = mapped_column("data_devolucao", nullable=False)
    motivo_devolucao: Mapped[str] = mapped_column("motivo_devolucao", nullable=False)
    data_adocao: Mapped[str] = mapped_column("data_adocao", nullable=False)
    data_cadastro: Mapped[str] = mapped_column("data_cadastro", nullable=False)

    def __init__(self, animal_id, adotante_id, companha_id, data_devolucao, motivo_devolucao, data_adocao, data_cadastro):
        self.animal_id = animal_id
        self.adotante_id = adotante_id
        self.companha_id = companha_id
        self.data_devolucao = data_devolucao
        self.motivo_devolucao = motivo_devolucao
        self.data_adocao = data_adocao
        self.data_cadastro = data_cadastro
        
    @property
    def serialize(self):
        schema = AdocaoSchema()
        return schema.dump(self)
    
# === Adotante ===
from backend.external.schemas import AdotanteSchema

class AdotanteModel(db.Model):
    __tablename__ = "tab_adotante"

    adotante_id: Mapped[int] = mapped_column("adotante_id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", nullable=False)
    telefone: Mapped[str] = mapped_column("telefone", nullable=False)
    email: Mapped[str] = mapped_column("email", nullable=False)
    moradia: Mapped[str] = mapped_column("moradia", nullable=False)

    def __init__(self, nome, telefone, email, moradia):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.moradia = moradia
        
    @property
    def serialize(self):
        schema = AdotanteSchema()
        return schema.dump(self)
    
# === Lar Temporário ===
from backend.external.schemas import LarTemporarioSchema

class LarTemporarioModel(db.Model):
    __tablename__ = "tab_lar_temporario"

    lar_temporario_id: Mapped[int] = mapped_column("lar_temporario_id", primary_key=True)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    hospedeiro_id: Mapped[int] = mapped_column("hospedeiro_id", nullable=False)
    periodo: Mapped[str] = mapped_column("periodo", nullable=False)
    data_hospedagem: Mapped[str] = mapped_column("data_hospedagem", nullable=False)
    data_cadastro: Mapped[str] = mapped_column("data_cadastro", nullable=False)

    def __init__(self, animal_id, hospedeiro_id, periodo, data_hospedagem, data_cadastro):
        self.animal_id = animal_id
        self.hospedeiro_id = hospedeiro_id
        self.periodo = periodo
        self.data_hospedagem = data_hospedagem
        self.data_cadastro = data_cadastro
        
    @property
    def serialize(self):
        schema = LarTemporarioSchema()
        return schema.dump(self)
    
# === Hospedeiro ===
from backend.external.schemas import HospedeiroSchema

class HospedeiroModel(db.Model):
    __tablename__ = "tab_hospedeiro"

    hospedeiro_id: Mapped[int] = mapped_column("hospedeiro_id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", nullable=False)
    telefone: Mapped[str] = mapped_column("telefone", nullable=False)
    email: Mapped[str] = mapped_column("email", nullable=False)
    moradia: Mapped[str] = mapped_column("moradia", nullable=False)

    def __init__(self, nome, telefone, email, moradia):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.moradia = moradia
        
    @property
    def serialize(self):
        schema = HospedeiroSchema()
        return schema.dump(self)
    
# === Apadrinhamento ===
from backend.external.schemas import ApadrinhamentoSchema

class ApadrinhamentoModel(db.Model):
    __tablename__ = "tab_apadrinhamento"

    apadrinhamento_id: Mapped[int] = mapped_column("apadrinhamento_id", primary_key=True)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    nome_apadrinhador: Mapped[str] = mapped_column("nome_apadrinhador", nullable=False)
    valor: Mapped[str] = mapped_column("valor", nullable=False)
    regularidade: Mapped[str] = mapped_column("regularidade", nullable=False)

    def __init__(self, animal_id, nome_apadrinhador, valor, regularidade):
        self.animal_id = animal_id
        self.nome_apadrinhador = nome_apadrinhador
        self.valor = valor
        self.regularidade = regularidade
        
    @property
    def serialize(self):
        schema = ApadrinhamentoSchema()
        return schema.dump(self)
    
# === Procedimento ===
from backend.external.schemas import ProcedimentoSchema

class ProcedimentoModel(db.Model):
    __tablename__ = "tab_procedimento"

    procedimento_id: Mapped[int] = mapped_column("procedimento_id", primary_key=True)
    tipo: Mapped[str] = mapped_column("tipo", nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", nullable=False)
    valor: Mapped[str] = mapped_column("valor", nullable=False)
    data_procedimento: Mapped[str] = mapped_column("data_procedimento", nullable=False)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    voluntario_id: Mapped[int] = mapped_column("voluntario_id", nullable=False)
    despesa_id: Mapped[int] = mapped_column("despesa_id", nullable=False)

    def __init__(self, tipo, descricao, valor, data_procedimento, animal_id, voluntario_id, despesa_id):
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor
        self.data_procedimento = data_procedimento
        self.animal_id = animal_id
        self.voluntario_id = voluntario_id
        self.despesa_id = despesa_id
        
    @property
    def serialize(self):
        schema = ProcedimentoSchema()
        return schema.dump(self)
    
# === Campanha ===
from backend.external.schemas import CampanhaSchema

class CampanhaModel(db.Model):
    __tablename__ = "tab_campanha"

    campanha_id: Mapped[int] = mapped_column("campanha_id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", nullable=False)
    tipo: Mapped[str] = mapped_column("tipo", nullable=False)
    data_inicio: Mapped[str] = mapped_column("data_inicio", nullable=False)
    data_termino: Mapped[str] = mapped_column("data_termino", nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", nullable=False)
    local: Mapped[str] = mapped_column("local", nullable=False)

    def __init__(self, nome, tipo, data_inicio, data_termino, descricao, local):
        self.nome = nome
        self.tipo = tipo
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.descricao = descricao
        self.local = local
        
    @property
    def serialize(self):
        schema = CampanhaSchema()
        return schema.dump(self)
    
# === Doação ===
from backend.external.schemas import DoacaoSchema

class DoacaoModel(db.Model):
    __tablename__ = "tab_doacao"

    doacao_id: Mapped[int] = mapped_column("doacao_id", primary_key=True)
    doador: Mapped[str] = mapped_column("doador", nullable=False)
    valor: Mapped[str] = mapped_column("valor", nullable=False)
    data_doacao: Mapped[str] = mapped_column("data_doacao", nullable=False)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    companha_id: Mapped[int] = mapped_column("companha_id", nullable=False)
    estoque_id: Mapped[int] = mapped_column("estoque_id", nullable=False)
    comprovante: Mapped[str] = mapped_column("comprovante", nullable=False)

    def __init__(self, doador, valor, data_doacao, animal_id, companha_id, estoque_id, comprovante):
        self.doador = doador
        self.valor = valor
        self.data_doacao = data_doacao
        self.animal_id = animal_id
        self.companha_id = companha_id
        self.estoque_id = estoque_id
        self.comprovante = comprovante
        
    @property
    def serialize(self):
        schema = DoacaoSchema()
        return schema.dump(self)
    
# === Despesa ===
from backend.external.schemas import DespesaSchema

class DespesaModel(db.Model):
    __tablename__ = "tab_despesa"

    despesa_id: Mapped[int] = mapped_column("despesa_id", primary_key=True)
    valor: Mapped[str] = mapped_column("valor", nullable=False)
    data_despesa: Mapped[str] = mapped_column("data_despesa", nullable=False)
    tipo: Mapped[str] = mapped_column("tipo", nullable=False)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)
    procedimento_id: Mapped[int] = mapped_column("procedimento_id", nullable=False)
    comprovante: Mapped[str] = mapped_column("comprovante", nullable=False)

    def __init__(self, valor, data_despesa, tipo, animal_id, procedimento_id, comprovante):
        self.valor = valor
        self.data_despesa = data_despesa
        self.tipo = tipo
        self.animal_id = animal_id
        self.procedimento_id = procedimento_id
        self.comprovante = comprovante
        
    @property
    def serialize(self):
        schema = DespesaSchema()
        return schema.dump(self)
    
# === Estoque ===
from backend.external.schemas import EstoqueSchema

class EstoqueModel(db.Model):
    __tablename__ = "tab_estoque"

    estoque_id: Mapped[int] = mapped_column("estoque_id", primary_key=True)
    categoria: Mapped[str] = mapped_column("categoria", nullable=False)
    tipo_item: Mapped[str] = mapped_column("tipo_item", nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", nullable=False)
    especie_animal: Mapped[str] = mapped_column("especie_animal", nullable=False)
    quantidade: Mapped[str] = mapped_column("quantidade", nullable=False)

    def __init__(self, categoria, tipo_item, descricao, especie_animal, quantidade):
        self.categoria = categoria
        self.tipo_item = tipo_item
        self.descricao = descricao
        self.especie_animal = especie_animal
        self.quantidade = quantidade
        
    @property
    def serialize(self):
        schema = EstoqueSchema()
        return schema.dump(self)
    
# === Tarefa ===
from backend.external.schemas import TarefaSchema

class TarefaModel(db.Model):
    __tablename__ = "tab_tarefa"

    tarefa_id: Mapped[int] = mapped_column("tarefa_id", primary_key=True)
    tipo: Mapped[str] = mapped_column("tipo", nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", nullable=False)
    data_tarefa: Mapped[str] = mapped_column("data_tarefa", nullable=False)
    voluntario_id: Mapped[int] = mapped_column("voluntario_id", nullable=False)
    animal_id: Mapped[int] = mapped_column("animal_id", nullable=False)

    def __init__(self, tipo, descricao, data_tarefa, voluntario_id, animal_id):
        self.tipo = tipo
        self.descricao = descricao
        self.data_tarefa = data_tarefa
        self.voluntario_id = voluntario_id
        self.animal_id = animal_id
        
    @property
    def serialize(self):
        schema = TarefaSchema()
        return schema.dump(self)
    
# === Voluntário ===
from backend.external.schemas import VoluntarioSchema

class VoluntarioModel(db.Model):
    __tablename__ = "tab_voluntario"

    voluntario_id: Mapped[int] = mapped_column("voluntario_id", primary_key=True)
    nome: Mapped[str] = mapped_column("nome", nullable=False)
    foto: Mapped[str] = mapped_column("foto", nullable=False)
    email: Mapped[str] = mapped_column("email", nullable=False)
    telefone: Mapped[str] = mapped_column("telefone", nullable=False)

    def __init__(self, nome, foto, email, telefone):
        self.nome = nome
        self.foto = foto
        self.email = email
        self.telefone = telefone
        
    @property
    def serialize(self):
        schema = VoluntarioSchema()
        return schema.dump(self)