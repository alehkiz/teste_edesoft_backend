from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
from rich.console import Console

db = SQLAlchemy(session_options={'autoflush': False})

@click.command('init-db')
@with_appcontext
def init_db():
    console = Console()
    console.print('[bold green]Iniciando banco de dados')
    from app.models.app import CessaoFundo
    db.create_all()
    
