from flask import Blueprint, render_template


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/index')
@bp.route('/main')
def index():
    return render_template('base.html')