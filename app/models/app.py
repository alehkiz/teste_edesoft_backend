from app.core.db import db



class CessaoFundo(db.Model):
    ID_CESSAO = db.Column(db.Integer, nullable=False, primary_key=True)
    ORIGINADOR = db.Column(db.String(250), nullable=False)
    DOC_ORIGINADOR = db.Column(db.Integer, nullable=False)
    CEDENTE = db.Column(db.String(250), nullable=False)
    DOC_CEDENTE = db.Column(db.String(250), nullable=False)
    CCB = db.Column(db.Integer, nullable=False)
    ID_EXTERNO = db.Column(db.Integer, nullable=False)
    CLIENTE = db.Column(db.String(250), nullable=False)
    CPF_CNPJ = db.Column(db.String(50), nullable=False)
    ENDERECO = db.Column(db.String(250), nullable=False)
    CEP = db.Column(db.String(50), nullable=False)
    CIDADE = db.Column(db.String(250), nullable=False)
    UF = db.Column(db.String(50), nullable=False)
    VALOR_DO_EMPRESTIMO = db.Column(db.Numeric(10,2), nullable=False)
    VALOR_PARCELA = db.Column(db.Numeric(10,2), nullable=False)
    TOTAL_PARCELAS = db.Column(db.Integer, nullable=False)
    PARCELA = db.Column(db.Integer, nullable=False)
    DATA_DE_EMISSAO = db.Column(db.Date, nullable=False)
    DATA_DE_NASCIMENTO = db.Column(db.Date, nullable=False)
    PRECO_DE_AQUISICAO = db.Column(db.Numeric(10,2), nullable=False)
