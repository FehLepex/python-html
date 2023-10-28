from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'your secret key'

messages = [{'name': 'Message One',
             'content': 'Message One Content'},
            {'limit': 'Message Two',
             'content': 'Message Two Content'}
            ]

cartoes = []



@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/cadastrocartao', methods=('GET', 'POST'))
def cadastrarCartao():
    messages.clear()
    print(request.method)
    if request.method == 'POST':
        name = request.form['txtNome']
        limit = request.form['txtLimite']
        if not name:
            flash('Nome é obrigatório!')
        elif not limit:
            flash('Limite do cartão é obrigatório')
            messages.append({'name': name, 'limit': limit})
        else:
            flash(name + ' cadastrado com sucesso')
            cartoes.append({'name': name, 'limit': limit})

        messages.append({'name': name, 'limit': limit})
        return render_template('cadastrocartao.html', lista = cartoes, tamanhoLista = len(cartoes))
    else:
        return render_template('cadastrocartao.html',  lista = cartoes, tamanhoLista = len(cartoes))


@app.route('/cadastracompras')
def cadastrarCompras():
    return render_template('cadastracompras.html')


@app.route('/listacartao')
def listacartao():
    return render_template('listacartao.html')


@app.route('/relatoriodegastos')
def relatoriodegastos():
    return render_template('relatorioDeGastos.html')


@app.route('/visualizarfatura')
def visualizarFatura():
    return render_template('visualizarFatura.html')


@app.route('/dashboardhome')
def dashboardHome():
    return render_template('dashboardhome.html')


@app.route('/alterarlimite')
def alterarlimite():
    return render_template('alterarLimite.html')


if __name__ == '__main__':
    app.run(debug=True)
