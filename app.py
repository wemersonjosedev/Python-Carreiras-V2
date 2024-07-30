from flask import Flask, jsonify, render_template

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Desenvolvedor Web',
    'localidade': 'Rio de Janeiro',
    'salario': 'R$ 5.000'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Python',
    'localidade': 'São Paulo',
    'salario': 'R$ 6.000'
}, {
    'id': 3,
    'titulo': 'Analista de Dados',
    'localidade': 'Maranhão',
    'salario': 'R$ 2.500'
}, {
    'id': 4,
    'titulo': 'Analista de Marketing',
    'localidade': 'Rio Grande do Sul',
    'salario': 'R$ 1.000'
}, {
    'id': 5,
    'titulo': 'Analista de Suporte',
    'localidade': 'Goiás',
    'salario': '50.000'
}]
@app.route("/")
def hello():
    return render_template("home.html", vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
