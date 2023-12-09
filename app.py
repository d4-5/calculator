from flask import Flask, render_template, request
from sympy import sympify
from type1 import type1
from type2 import type2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equation')
def equation():
    equation_type = request.args.get('equation_type')
    return render_template('form.html', equation_type=equation_type)

@app.route('/solve')
def solve_equation():
    equation_type = request.args.get('equation_type')
    try :
        a = sympify(request.args.get('a'))
        phi = sympify(request.args.get('phi'))
        psi = sympify(request.args.get('psi'))
        mu = sympify(request.args.get('mu'))
        f = sympify(request.args.get('f'))

        if equation_type == "type1":
            calculated_equation = type1(a, phi, psi, mu, f)
        else :
            calculated_equation = type2(a, phi, psi, mu, f)

        return render_template('show_equation.html', calculated_equation=calculated_equation)
    except Exception as e:
        return render_template('form.html', equation_type=equation_type, error=str(e))


if __name__ == '__main__':
    app.run()
