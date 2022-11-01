from os import listdir, mkdir
from os.path import isdir, isfile, join
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import CessaoFundo, Base
from rich.console import Console
from pandas import read_csv, read_excel, to_datetime
from pandas.core.frame import DataFrame
DEFAULT_DST = 'arquivos'
DEPARA_FILE = 'depara.xlsx'

console = Console()
engine = create_engine("sqlite:///db.db")
conn = engine.connect()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

console.print('[bold green]Criando banco de dados')
Base.metadata.create_all(engine)

def dataframe_to_db(df : DataFrame):
    '''
    Recebe um ´DataFrame´ e insere em um modelo e salva em banco de dados'''

    df_file_model = read_excel(DEPARA_FILE).set_index('COLUNA CSV')
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
    for idx, row in df.iterrows():
        cf = CessaoFundo()
        if not session.query(CessaoFundo).filter(CessaoFundo.ID_EXTERNO == int(row['ID_EXTERNO'])).first() is None:
            console.print(f'[bold red]ID {row["ID_EXTERNO"]} já cadastrado')
            continue
        for col in row.index:
            setattr(cf, col, row[col])
        session.add(cf)
    session.commit()

if __name__ == '__main__':

    if not isdir(DEFAULT_DST):
        console.print('[bold green]Criando pasta')
        mkdir(DEFAULT_DST)

    files = [x for x in listdir(DEFAULT_DST)]
    while True:
        if len(files) == 1:
            name = join(DEFAULT_DST,files[0])
            break
        if len(files) == 0:
            console.print(f'[bold red]Nenhum arquivo encontrado, cole o arquivo em {DEFAULT_DST}')
        else:
            console.print(f'[bold red]Existe mais de um arquivo em {DEFAULT_DST}')
            name = console.input('[bold red]Informe o nome do arquivo: ')
            if not isfile(join(DEFAULT_DST, name)):
                console.print('[bold red]Arquivo inválido, tente novamente')
            else:
                console.print('[bold green]Arquivo válido')
                name = join(DEFAULT_DST, name)
                break
        console.input('[bold red]Arquivo adicionado?')
        files = [x for x in listdir(DEFAULT_DST)]

    df = read_csv(name, sep=';', encoding = "ISO-8859-1")
    dataframe_to_db(df)