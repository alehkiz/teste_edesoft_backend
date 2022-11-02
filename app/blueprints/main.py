from flask import Blueprint, render_template

from app.forms.upload import SendFileForm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/index', methods=['POST', 'GET'])
@bp.route('/main')
def index():
    form = SendFileForm()
    if form.validate_on_submit():
        return 'ok'


    return render_template('upload.html', form=form)