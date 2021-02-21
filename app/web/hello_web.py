from flask import render_template, Blueprint


hello_web = Blueprint('hello_web', __name__)


@hello_web.route('/web/hello/', defaults={'name': 'world'})
@hello_web.route('/web/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
