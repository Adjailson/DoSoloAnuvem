import requests
import json
class TesteApi:

    url = "https://apigirassol.roboticasuassuna.com.br/apiClima/salvarDados"
    def __init__(self):

        self.response = requests.get(self.url)
        self.data = []
        self.temperatura = []
        self.umidade = []
        self.hora = []
        self.operacao = 0
        self.params = None
        self.dados = self.response.json()
    
    def PuxarApi(self):
        url = "https://apigirassol.roboticasuassuna.com.br/apiClima/getListarDados"
        response = requests.get(url)
        data = response.json()
        print(json.dumps(data, indent=2))


    def Hora(self, horas):
        if horas <= 24:
            for i in range (int(horas)):
                lista = []
                dado = horas + self.hora
                lista.append(dado)
            return lista
    
    def InserirUmidade(self, inicio, fim):
        for i in range(int(inicio), int(fim), 1):
            self.umidade.append(i)
        return self.umidade
    
    def InserirTemperatura(self, inicio, fim):
        for i in range(int(inicio), int(fim)):
            self.temperatura.append(i)
        return self.temperatura
    
    def PeriodoData(self, inicio, fim):
        for i in range(int(inicio), int(fim), 1):
            data = f"2025-10-{i}"
            self.data.append(data)
            hora = f'{i}:00:00'
            self.hora.append(hora)
        return self.data and self.hora
    
    def PostarDados(self, inicio):
        ## self.response == "200":
            
            for i in range (0,int(inicio)):
                self.params = {
                    'temperatura': float(self.temperatura[i]),
                    'umidade': float(self.umidade[i]),
                    'operacao': self.operacao,
                    'data': f"{self.data[i]} {self.hora[i]}"
                }   
                response = requests.post(self.url, data=self.params)
                resultado = response.json()
                print(json.dumps(resultado, indent=2))

teste = TesteApi()
teste.PuxarApi()
'''
teste.PeriodoData(10, 16)
teste.InserirTemperatura(20, 26) 
teste.InserirUmidade(80, 86)
teste.PostarDados(6) '''
