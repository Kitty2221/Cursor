from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def greetings():
    return render_template("greetings.html")


@app.route("/calc/<int:x>/<int:y>/<string:operator>", methods=["GET", "POST"])
def calc(x, y, operator):
    if operator == "sum" or operator == "+":
        return render_template("calc.html", x=x, y=y, operator="+", result=x + y)
    elif operator == "sub" or operator == "-":
        return render_template("calc.html", x=x, y=y, operator="-", result=x + y)
    elif operator == 'div' or operator == '/':
        if y == 0:
            return 'Divide by zero'
        else:
            return render_template('calc.html', x=x, y=y, operator='/', result=x / y)
    elif operator == 'mult' or operator == '*':
        return render_template('calc.html', x=x, y=y, operator='*', result=x * y)
    else:
        return 'Please choose a correct operation!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
