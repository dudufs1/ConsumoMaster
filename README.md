# 🚗 ConsumoMaster

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
</p>

> **ConsumoMaster** é um ecossistema inteligente para motoristas que desejam otimizar seus gastos com combustível através de simulações precisas e dados em tempo real.

---

## ✨ Funcionalidades

* **📈 Simulação de Custos:** Calcule o custo exato de viagens com base na distância, consumo do veículo e preço do combustível.
* **🤖 Automação com Selenium:** Busca automática do preço médio nacional (ANP/Google) para facilitar o preenchimento dos dados.
* **📱 Interface Responsiva:** Design moderno construído com Bootstrap 5, adaptável para PC e Smartphones.
* **📊 Análise de Viabilidade:** Lógica integrada para decidir entre Etanol ou Gasolina (em desenvolvimento).

---

## 🛠️ Tecnologias Utilizadas

O projeto utiliza uma stack focada em performance e automação:

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
* **Web Scraping:** [Selenium Webdriver](https://www.selenium.dev/)
* **Frontend:** HTML5, CSS3 e [Bootstrap 5](https://getbootstrap.com/)
* **Gestão de Drivers:** [Webdriver Manager](https://pypi.org/project/webdriver-manager/)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/dudufs1/ConsumoMaster.git](https://github.com/dudufs1/ConsumoMaster.git)
   cd ConsumoMaster
2. **Crie e ative seu ambiente virtual:**
	```bash
 	python -m venv .venv
 
	# Windows
	.venv\Scripts\activate
	# Linux/Mac
	source .venv/bin/activate
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Inicie o servidor:**
   ```bash
   python app.py
Acesse em seu navegador: http://127.0.0.1:5000
 
