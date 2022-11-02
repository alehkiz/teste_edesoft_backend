from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
import click
from flask.cli import with_appcontext
from rich.console import Console

db = SQLAlchemy(session_options={'autoflush': False})

@click.command('init-db')
@with_appcontext
def init_db():
    console = Console()
    console.print('[bold green]Iniciando banco de dados')
    if not database_exists(db.engine.url):
        console.print('[bold green]Criando banco de dados')
        create_database(db.engine.url)
        console.print('[bold green]Banco de dados criado')
    from app.models.app import CessaoFundo
    console.print('[bold green]Criando tabelas')
    db.create_all()
    console.print('[bold green]Fim.')
    
