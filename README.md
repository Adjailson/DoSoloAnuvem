# README.md

# Phenoglad Flask App

Este é um projeto de aplicação web desenvolvido com Flask, que permite o registro e login de usuários. A aplicação armazena informações de usuários, como nome, email e senha, em um banco de dados SQLite.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios:

```
phenoglad-flask-app
├── app.py                # Ponto de entrada da aplicação Flask
├── models.py             # Modelos de dados para o banco de dados
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
├── templates             # Templates HTML
│   ├── index.html       # Página inicial
│   ├── login.html       # Página de login
│   └── registro.html     # Página de registro
├── static               # Arquivos estáticos
│   └── registro.css      # Estilos para a página de registro
└── instance             # Banco de dados
    └── phenoglad.sqlite  # Banco de dados SQLite
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd phenoglad-flask-app
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute a aplicação:
   ```
   python app.py
   ```

2. Acesse a aplicação no navegador em `http://127.0.0.1:5000`.

## Funcionalidades

- Registro de usuários com nome, email e senha.
- Armazenamento seguro de senhas.
- Interface de usuário simples e responsiva.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.