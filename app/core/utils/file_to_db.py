from os import listdir, mkdir
from os.path import isdir, isfile, join
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rich.console import Console
from pandas import read_csv, read_excel, to_datetime, to_numeric
from pandas.core.frame import DataFrame
from flask import current_app as app
from app.models.app import CessaoFundo
from app.core.db import db
from sqlalchemy.dialects import postgresql


console = Console()
def dataframe_to_db(file_path : str):
    '''
    Recebe uma string de um arquivo válido e salva em banco de dados, conforme a configuração geral do aplicativo
    '''
    file_extention = file_path.rsplit('.', 1)[1].lower()
    DIC_FUNC = {'csv': {'func': read_csv, 'params': {'sep':';', 'encoding':"ISO-8859-1"}}}
    if not isfile(file_path):
        raise FileNotFoundError('Arquivo não existe')
    if not file_extention in app.config['ALLOWED_EXTENSIONS']:
        raise Exception('Arquivo inválido')
    
    df = DIC_FUNC[file_extention]['func'](file_path, **DIC_FUNC[file_extention]['params'])

    df_file_model = read_excel(app.config['DEPARA']).set_index('COLUNA CSV')
    
    df.rename(df_file_model.to_dict()['TABELA BANCO'], axis=1, inplace=True)
    df['IOF'] = df['IOF'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['VALOR_DO_EMPRESTIMO'] = df['VALOR_DO_EMPRESTIMO'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['TAXA_DE_JUROS'] = df['TAXA_DE_JUROS'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['PRINCIPAL'] = df['PRINCIPAL'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['JUROS'] = df['JUROS'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['COMISSAO'] = df['COMISSAO'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['VALOR_PARCELA'] = df['VALOR_PARCELA'].str.replace(',', '.').str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['DATA_DE_EMISSAO'] = to_datetime(df['DATA_DE_EMISSAO'], format='%d/%m/%Y')
    df['DATA_DE_VENCIMENTO'] = to_datetime(df['DATA_DE_VENCIMENTO'], format='%d/%m/%Y')
    df['DATA_DE_COMPRA_CCB'] = to_datetime(df['DATA_DE_COMPRA_CCB'], format='%d/%m/%Y')
    df['DOC_ORIGINADOR'] = df['DOC_ORIGINADOR'].replace(r"[^0-9\d\_]+", '', regex=True)
    for idx, row in df.iterrows():
        cf = CessaoFundo()
        for col in row.index:
            setattr(cf, col, row[col])
        db.session.add(cf)
    try:
        db.session.commit()
        return True
    except Exception as e:
        raise Exception(e, 'Não foi possível salvar os dados')
