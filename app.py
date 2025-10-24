from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# URL base da API
API_BASE_URL = "https://apigirassol.roboticasuassuna.com.br/apiClima"

def buscar_dados_api(data_inicio, data_fim):
    endpoint = f"{API_BASE_URL}/getListarDados/{data_inicio}D{data_fim}"
    
    response = requests.get(endpoint, timeout=30)
    
    if response.status_code == 200:
        dados = response.json()
        
        if dados.get('status') == 'sucesso':
            return dados
        else:
            print(f"API retornou status de erro: {dados.get('status')}")
            return None
    else:
        print(f"Erro HTTP {response.status_code} na requisição")
        return None
            
 

def processar_dados_para_graficos(dados_brutos):

    if not dados_brutos or 'dados' not in dados_brutos:
        return {'datas': [], 'temperaturas': [], 'umidades': []}
    
    # Dicionário para agrupar dados por data
    dados_por_data = {}
    
    for registro in dados_brutos['dados']:
        # Extrai apenas a data (remove o horário)
        data_completa = registro['data']
        data = data_completa.split(' ')[0]  # Pega apenas "YYYY-MM-DD"
        
        # Se é a primeira vez que vemos esta data, inicializa as listas
        if data not in dados_por_data:
            dados_por_data[data] = {
                'temperaturas': [],
                'umidades': []
            }
        
        # Adiciona os valores às listas correspondentes
        dados_por_data[data]['temperaturas'].append(registro['temperatura'])
        dados_por_data[data]['umidades'].append(registro['umidade'])
    
    # Listas para os gráficos
    datas = []
    temperaturas_medias = []
    umidades_medias = []
    
    # Ordena as datas para manter a ordem cronológica
    datas_ordenadas = sorted(dados_por_data.keys())
    
    for data in datas_ordenadas:
        valores = dados_por_data[data]
        
        # Calcula a média de temperatura para o dia
        temp_media = sum(valores['temperaturas']) / len(valores['temperaturas'])
        
        # Calcula a média de umidade para o dia
        umid_media = sum(valores['umidades']) / len(valores['umidades'])
        
        # Adiciona aos arrays finais
        datas.append(data)
        temperaturas_medias.append(round(temp_media, 2))
        umidades_medias.append(round(umid_media, 2))
    
    return {
        'datas': datas,
        'temperaturas': temperaturas_medias,
        'umidades': umidades_medias
    }

@app.route('/')
def index():
    return render_template('grafico_ut.html')

@app.route('/buscar-dados', methods=['POST'])
def buscar_dados():
    try:
        # Obtém os dados do formulário
        dados_form = request.get_json()
        data_inicio = dados_form.get('data_inicio')
        data_fim = dados_form.get('data_fim')
        
        # Validação das datas
        if not data_inicio or not data_fim:
            return jsonify({'erro': 'Datas de início e fim são obrigatórias'}), 400
        
        # Converte para objetos datetime para validação
        data_inicio_obj = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_fim_obj = datetime.strptime(data_fim, '%Y-%m-%d')
        
        if data_inicio_obj > data_fim_obj:
            return jsonify({'erro': 'Data de início não pode ser posterior à data de fim'}), 400
        
        # Busca dados da API externa
        dados_api = buscar_dados_api(data_inicio, data_fim)
        
        if not dados_api:
            return jsonify({'erro': 'Não foi possível obter dados da API para o período selecionado'}), 500
        
        # Processa os dados para os gráficos
        dados_processados = processar_dados_para_graficos(dados_api)
        
        # Retorna os dados processados
        return jsonify({
            'sucesso': True,
            'dados': dados_processados,
            'periodo': {
                'inicio': data_inicio,
                'fim': data_fim
            }
        })
        
    except ValueError as e:
        return jsonify({'erro': 'Formato de data inválido. Use YYYY-MM-DD'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro interno do servidor: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)