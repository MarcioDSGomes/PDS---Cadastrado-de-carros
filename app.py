from flask import Flask
from flask import render_template
from flask import request
import csv

app = Flask(__name__)
registros = []
lista = []


@app.route('/', methods = ['GET'])                      #--Rota da página de BEM VINDO--# 
def principal():                   
    return render_template('bemvindo.html')             #--Renderização do HTML BEM VINDO--#


@app.route ('/cadastramento', methods=['GET'])          #--Rota da página de CADASTRO--# 
def secundario():
    return render_template('cadastro.html')             #--Renderização do HTML CADASTRO--#


@app.route ('/contato', methods=['GET'])                #--Rota da página de CONTATO--# 
def ultimo():
    return render_template('contato.html')              #--Renderização do HTML CONTATO--#


@app.route('/cadastro', methods = ['GET', 'POST'])      #--Rota da página de CADASTRO RECEBIDO--# 
def cadastro():
    if request.method == 'POST':
        registros.append(request.form.get('modelo'))  
        registros.append(request.form.get('marca'))  
        registros.append(request.form.get('placa'))  
        registros.append(request.form.get('nomeProprietario'))
        registros.append(request.form.get('anoFabricacao')) 
        registros.append(request.form.get('telefone'))
        registros.append(request.form.get('endereco'))
        registros.append(request.form.get('cidade'))
        registros.append(request.form.get('estadoUf'))
        registros.append(request.form.get('imagem')) 
        print(registros)     #--O sistema fara a coleta dos dados acima (de 'modelo' até 'imagem') e ira anexar ao documento 'cadastro.csv'--# 
        with open('cadastro.csv', 'a', newline='\n') as insere_linha:
            arquivo = csv.writer(insere_linha)
            arquivo.writerow(registros)        
            insere_linha.close()
        registros.clear()
    return render_template('cad_recebido.html')    #--Renderização do HTML CADASTRO RECEBIDO--#


@app.route ('/lista_cadastro', methods = ['GET', 'POST'])  #--Rota da página de CARROS CADASTRADOS--# 
def lista_cadastro():
    lista.clear()
    with open('cadastro.csv') as listagem:    #--Ira abrir o arquivo 'cadastro.csv'--#
        csv_reader = csv.reader(listagem, delimiter=',')
        for row in csv_reader:
            print(row)
            lista.append(row)
    return str(lista)    #--Ira mostrar na tela os dados que estão armazandos no documento '.csv'--#






@app.route('/contato', methods = ['GET', 'POST'])  #--Rota da página de CONTATO--# 
def contato():
    if request.method == 'POST':
        registros.append(request.form.get('nome'))  
        registros.append(request.form.get('email'))  
        registros.append(request.form.get('mensagem'))  
        print(registros)  #--O sistema fara a coleta dos dados acima (de 'nome' até 'mensagem') e ira anexar ao documento 'contato.csv'--# 
        with open('contato.csv', 'a', newline='\n') as insere_linha:
            arquivo = csv.writer(insere_linha)
            arquivo.writerow(registros)        
            insere_linha.close()
        registros.clear()
    return render_template('mens_recebida.html')  #--Renderização do HTML MENSAGEM RECEBIDA--#


@app.route ('/mensagens_recebidas', methods = ['GET', 'POST'])   #--Rota da página de MENSAGENS RECEBIDAS--# 
def mensagens_recebidas():                                     
    lista.clear()
    with open('contato.csv') as listagem:  #--Ira abrir o arquivo 'contato.csv'--#
        csv_reader = csv.reader(listagem, delimiter=',')
        for row in csv_reader:
            print(row)
            lista.append(row)
    return str(lista)  #--Ira mostrar na tela os dados que estão armazandos no documento '.csv'--#


app.run(debug = True)
