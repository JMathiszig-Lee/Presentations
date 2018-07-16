from flask import Flask
from flask import render_template, abort
from jinja2 import TemplateNotFound


app = Flask(__name__)

app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)
@app.route("/")
def hello():
    return "<a href='/TIVAmodels'>TIVA models</a>"


@app.route('/<presentation_name>/', methods=['GET'])
def landing(presentation_name):
    try:
        return render_template(presentation_name + '.html')
    except TemplateNotFound:
        abort(404)
