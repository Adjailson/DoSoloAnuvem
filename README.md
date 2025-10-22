# 🌻 Do Solo à Nuvem: Agricultura Digital com IoT, Imagens e Energia Solar

## Visão Geral do Projeto

Esta plataforma web é o componente digital da proposta **"Do Solo à Nuvem: Agricultura Digital com IoT, Imagens e Energia Solar"**.

O sistema tem como objetivo principal o **monitoramento remoto e em tempo real** de culturas (como girassóis), integrando dados de **sensores** e **imagens** capturadas por módulos embarcados (**ESP32-CAM**).

A plataforma utiliza tecnologias de **Internet das Coisas (IoT)** e **Visão Computacional** para fornecer uma ferramenta robusta e acessível à comunidade acadêmica (alunos e professores) para documentar, analisar e tomar decisões informadas sobre o desenvolvimento das plantas, impulsionando a **Agricultura Digital** na **ETE Ariano Vilar Suassuna**.

---

## 🚀 Tecnologias e Desafios

### Backend & API
* **Python (Flask)**: Framework principal para a construção das visualizações e rotas front-end.
* **Python (FastAPI)**: Utilizado para a criação de uma **REST API** robusta e de alta performance para a recepção e entrega dos dados dos sensores e imagens.
* **OpenCV**: Biblioteca essencial para a implementação da **Visão Computacional** (contagem de folhas).
* **Tecnologias de Futuro Envolvidas:** **Internet das Coisas (IoT)**, **Computação em Nuvem**, **Dispositivos Sensores** e **Visão Computacional**.

### Banco de Dados
* **MySQL**: Sistema de gerenciamento de banco de dados relacional principal para dados persistentes.
* **SQLite**: Opção de banco de dados leve, utilizada para desenvolvimento, testes ou para dados específicos/locais.

### Frontend & Estilo
* **Bootstrap**: Framework CSS utilizado para garantir um design moderno, **responsivo** e acessível.

### Desafio
* **Tema Principal:** Agronegócio.

---

## ✨ Funcionalidades Principais

| Funcionalidade | Tecnologia Envolvida | Descrição |
| :--- | :--- | :--- |
| **Dashboard de Monitoramento** | Dispositivos Web/Mobile | Exibição em **tempo real** de gráficos interativos com dados de temperatura, umidade do ar, umidade do solo e altura média da planta. |
| **Galeria de Imagens** | IoT, Computação em Nuvem | Interface para visualização das imagens capturadas periodicamente pelo ESP32-CAM, com registro de data e horário. |
| **Análise com Visão Computacional** | OpenCV | Implementação para a **contagem automatizada de folhas** das plantas, fornecendo indicadores de saúde e crescimento. |
| **Sistema de Alertas** | Dispositivos Sensores | Geração de alertas visuais e **notificações por e-mail** quando os parâmetros ultrapassam limites críticos configurados. |
| **Relatórios Automatizados** | - | Geração de relatórios em **PDF** contendo o histórico de dados, gráficos e imagens para documentação do progresso. |
| **Área de Acesso Restrito** | - | Sistema de **login** com controle de permissões para professores e bolsistas. |

---

## 🏛️ Informações Institucionais

| Item | Detalhe |
| :--- | :--- |
| **Instituição Executora** | ETE Ariano Vilar Suassuna, Garanhuns/PE |
| **Professor(a) Integrador(a)** | Ana Marcela Ferreira Barros |
| **Parceiro Técnico** | **Clube de Robótica Suassuna** (https://roboticasuassuna.com.br) |
| **Parceiro 1 (Hospedagem/Equipamento)** | **MiRoute** – Soluções em Automação e Monitoramento (CNPJ: 60.225.444/0001-57) |
| **Parceiro 2 (Pesquisa/Suporte)** | Universidade Federal de Santa Maria (UFSM/RS) - Projeto Flores para Todos - PhenoGlad (CNPJ: 95.591.764/0001-05) |
| **Link do Repositório** | `https://github.com/Adjailson/DoSoloAnuvem.git` |

---

## 🛠️ Instalação e Execução (Em Breve)

Detalhes sobre como configurar o ambiente de desenvolvimento, instalar as dependências (`pip install -r requirements.txt`) e iniciar os servidores Flask/FastAPI serão adicionados em breve.

* **Requisitos:** Python 3.x, MySQL.
* **Setup:**
    1.  Clone o repositório: `git clone https://github.com/Adjailson/DoSoloAnuvem.git`
    2.  Navegue até o diretório: `cd DoSoloAnuvem`
    3.  Instale as dependências: `pip install -r requirements.txt`
    4.  Configure o banco de dados e as variáveis de ambiente.
    5.  Execute a aplicação: `python run.py` (ou comando apropriado para Flask/FastAPI)

---

## 📧 Contato

Para mais informações sobre o projeto ou parcerias:

* **Instituição Executora:** ETE Ariano Vilar Suassuna
* **Professor(a) Integrador(a):** Ana Marcela Ferreira Barros
