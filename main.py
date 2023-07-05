from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == "POST":
        numero = int(request.form.get('numero'))
        print(numero)
        for i in range(0,numero):
            if i * i == numero:
                resultado = i
                flash(f'O resultado da raiz do número {numero} é: {resultado}')
                return render_template('home.html', resultado = resultado)
            if i * i > numero:
                flash(f'Este número {numero} não possui raiz quadrada! ')
                return redirect(url_for('main'))
    return render_template('home.html')
    






if __name__ == "__main__":
    app.run(debug=True)