#core/views.py

from flask import render_template, request, Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    #More to come
    return render_template('index.htm')

@core.route('/info')
def info():
    return render_template('info.html')