from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class SendFileForm(FlaskForm):
    file = FileField('Arquivo',  name='file', validators=[DataRequired('Item Obrigatório')])

    submit = SubmitField('Enviar')