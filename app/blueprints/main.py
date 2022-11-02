from flask import (
    Blueprint,
    render_template,
    current_app as app,
    flash,
    request,
    redirect,
    url_for,
)
from datetime import datetime
from os.path import join, isfile
from pandas import read_sql_table, read_excel

from app.forms.upload import SendFileForm
from app.core.utils.file_to_db import dataframe_to_db
from app.core.db import db

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
@bp.route("/index")
def index():
    form = SendFileForm()
    return render_template("upload.html", form=form)


@bp.route("/upload", methods=["POST", "GET"])
def upload():
    form = SendFileForm()
    if form.validate_on_submit():
        file_uploaded = form.file.data
        file_name = datetime.now().strftime(format="%Y.%m.%d.%H.%M.%S.%f")
        file_extention = file_uploaded.filename.rsplit(".", 1)[1].lower()
        path = join(app.config["UPLOAD_FOLDER"], f"{file_name}.{file_extention}")
        # validação do tamanho do arquivo
        if request.content_length > app.config["MAX_CONTENT_PATH"]:
            form.file.errors.append(
                f'Arquivo com mais de {app.config["MAX_UPLOAD_FILE_MB"]} MB'
            )
            return render_template("upload.html", form=form)
        if file_uploaded != "":
            # Extensão permitida?
            if file_extention not in app.config["ALLOWED_EXTENSIONS"]:
                form.file.errors.append(
                    f'Arquivo não aceito, envie apenas arquivos no formato: {", ".join(app.config["ALLOWED_EXTENSIONS"])}'
                )
                return render_template("upload.html", form=form)
            # verificação do mimetype, caso não seja um arquivo XLS ou CSV será recusado
            if file_uploaded.mimetype not in app.config["ALLOWED_MIMETYPES"]:
                form.file.errors.append(f"Arquivo inválido")
                return render_template("upload.html", form=form)
            file_uploaded.save(path)
            if not isfile(path):
                flash("Não foi possível salvar o arquivo", category="warning")
                render_template("upload.html", form=form)
            dataframe_to_db(path)
            try:
                to_db = dataframe_to_db(path)
                if to_db is True:
                    flash(
                        "Dados salvos com sucesso no banco de dados, veja a tabela atualizada", category="success"
                    )
                    return redirect(url_for("main.table"))
                p
            except Exception as e:
                app.logger.error("Não foi possível salvar a planilha")
                app.logger.error(e, exc_info=True)
                flash(
                    "Ocorreu um erro na tentativa de salvar o banco de dados, tente novamente",
                    category="danger",
                )
                return redirect(url_for("main.upload"))
        else:
            form.file.errors.append("Nenhum arquivo enviado")
    return render_template("upload.html", form=form)


@bp.route("/table")
def table():
    df_file_model = read_excel(app.config["DEPARA"])
    df = read_sql_table("cessao_fundo", db.session.connection())
    df = df[df_file_model[df_file_model["SHOW"] == 1]["TABELA BANCO"].values]
    df.rename(
        df_file_model.set_index("TABELA BANCO").to_dict()["COLUNA CSV"],
        axis=1,
        inplace=True,
    )
    table = df.to_html(index=False, classes="table table-dark table-striped")

    return render_template("table.html", table=table)
