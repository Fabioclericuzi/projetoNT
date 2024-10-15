import time
import requests
from datetime import datetime
import mysql.connector



def format_data_ult_cotacao(data):
    data_format = datetime.fromtimestamp(data).strftime('%d/%m/%Y')
    return data_format

def pegar_ultima_cotacao():
    link = "https://economia.awesomeapi.com.br/json/last/BRL-USD"
    resposta = requests.get(link).json()
    data = int(resposta['BRLUSD']['timestamp'])
    valor = float(resposta['BRLUSD']['bid'])

    data_format = format_data_ult_cotacao(data)

    return {'data': data_format, 'Valor': valor}

def formatar_cotacoes_por_data(cotacoes):
    lista_formatada = []

    for cotacao in cotacoes:
        timestamp = int(cotacao["timestamp"])
        data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        lista_formatada.append({"data": data, "bid": cotacao.get("bid")})

    return lista_formatada

def formatar_cotacoes_por_data(cotacoes):
    lista_formatada = []

    for cotacao in cotacoes:
        timestamp = int(cotacao["timestamp"])
        data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        lista_formatada.append({"data": data, "bid": cotacao.get("bid")})

    return lista_formatada


def pegar_cotacao_por_data(data_inicial, data_final):
    data_inicio_formatada = datetime.strptime(data_inicial, '%d/%m/%Y').strftime('%Y%m%d')
    data_final_formatada = datetime.strptime(data_final, '%d/%m/%Y').strftime('%Y%m%d')

    url = (
        f"https://economia.awesomeapi.com.br/json/daily/BRL-USD/1000"
        f"?start_date={data_inicio_formatada}&end_date={data_final_formatada}"
    )
    resposta = requests.get(url)
    dados = resposta.json()

    if isinstance(dados, list):
        return formatar_cotacoes_por_data(dados)
    else:
        print("A resposta da API não é uma lista.")
        return []


def conector_mysql():
    while True:
        conexao = mysql.connector.connect(
            host='mysql_db',  
            user='neuro',
            password='neurotech',
            database='db_conversao'
        )
        if conexao.is_connected():
            return conexao
        else:
            print("Tentando conectar no banco")
            time.sleep(5)  


def criar_tabela_cotacoes():
    conexao = conector_mysql()
    cursor = conexao.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS cotacoes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        valor DECIMAL(10, 4),
        data_requisicao DATETIME,
        data_taxa DATE
    );
    """
    
    cursor.execute(create_table_query)
    
    cursor.close()
    conexao.close()

criar_tabela_cotacoes()


def inserir_cotacao(valor, data_requisicao, data_taxa):
    conexao = conector_mysql()
    cursor = conexao.cursor()

    sql = "INSERT INTO cotacoes (valor, data_requisicao, data_taxa) VALUES (%s, %s, %s)"
    cursor.execute(sql, (valor, data_requisicao, data_taxa))

    conexao.commit()
    cursor.close()
    conexao.close()



