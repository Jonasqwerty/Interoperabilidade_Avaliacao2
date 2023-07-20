from flask import Flask, json, render_template, request, redirect, jsonify
import sqlite3
import requests

app = Flask(__name__, template_folder='.')

@app.route('/listar', methods=['GET'])
def listar ():
	
	tempgol = requests.get("http://localhost:8081/servico.php")
	tempgol = tempgol.content
	tempgol = json.loads(tempgol)


	templatam = requests.get("http://localhost:8082/servico.php")
	templatam = templatam.content
	templatam = json.loads(templatam)
	return render_template('listar.html',resultado=tempgol ,resultado2=templatam)


@app.route('/comprar', methods=['GET'])
def comprar ():
	return render_template('comprar.html')

@app.route('/confirmar', methods=['GET', 'POST'])
def confirmar ():
	return render_template('confirmar.html')

@app.route('/', methods=['GET', 'POST'])
def index():
	return redirect('/listar')
	

@app.route('/buscar', methods=['POST', 'GET'])
def busca ():
	if request.method == 'POST':
		origem = request.values.get('origem')
		destino = request.values.get('destino')
		data = request.values.get('data')
		obj = { "origem": origem, "destino":destino,"datahora":data}
		delta = json.dumps(obj)
		temp = requests.post("http://localhost:8081/servico.php",data=delta)
		temp=temp.content
		temp=json.loads(temp)

		temporario2 = requests.post("http://localhost:8082/servico.php",data=delta)
		temporario2=temporario2.content
		temporario2=json.loads(temporario2)
		
		return render_template("buscar.html",resultado=temp,resultado2=temporario2)
	elif request.method == 'GET':
		return render_template("buscar.html")
		

app.run(port=5001, use_reloader=True)
