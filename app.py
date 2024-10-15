from flask import Flask, request, jsonify
from funcoes_conversao import pegar_cotacao_por_data, pegar_ultima_cotacao, inserir_cotacao
from datetime import datetime

app  = Flask(__name__)

@app.route('/cotacao-atual', methods=['GET'])
def cotacao_atual():
    dados = pegar_ultima_cotacao()

    if 'Valor' in dados:  
        data_requisicao = datetime.now()  
        data_taxa = datetime.strptime(dados['data'], '%d/%m/%Y').date()
        valor_taxa = dados['Valor']

    inserir_cotacao(valor_taxa, data_requisicao, data_taxa)
    return jsonify(dados)

@app.route('/cotacao_por_data', methods=['GET'])
def cotacao_por_data():
    data_origem = request.args.get('data_inicial')
    data_destino = request.args.get('data_final')

    if not data_origem or not data_destino:
        return jsonify({"error": "As datas de origem e de destino são obrigatórias."})

    dados = pegar_cotacao_por_data(data_origem, data_destino)
    
    for cotacao in dados:
        data_requisicao = datetime.now()  
        data_taxa = datetime.strptime(cotacao['data'], '%Y-%m-%d %H:%M:%S').date() 
        valor_taxa = cotacao['bid'] 
        
        inserir_cotacao(valor_taxa, data_requisicao, data_taxa)

    return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=False)

