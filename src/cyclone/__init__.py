
from typing import Union

from flask import Flask, Response, jsonify, render_template
from sympy import latex

from .engine import AdditionProblem, IntegrationProblem


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index() -> Union[Response, str]:
    return render_template('index.html', problem=latex(IntegrationProblem().statement, mode='plain'))


@app.route('/category/<int:category_id>')
def category(category_id: int) -> Response:
    response = {
        'category_id': category_id,
        'code': 200,
        'message': 'OK'
    }
    return jsonify(response)


@app.route('/problem/<int:category_id>')
def problem(category_id: int) -> Response:
    response = {
        'category': category,
        'code': 200,
        'message': 'OK'
    }
    return jsonify(response)
