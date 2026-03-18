from flask import Flask, render_template, request
# Importar o Selenium aqui no futuro para buscar preços reais
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time 
app = Flask(__name__)

def calcular_viagem(distancia, consumo, preco):
    """Lógica básica de cálculo de consumo"""
    litros_necessarios = distancia / consumo
    custo_total = litros_necessarios * preco
    return round(custo_total, 2)

def buscar_preco_real():
    chrome_options = Options()
    chrome_options.add_argument("--headless") # para rodar sem abrir o navegador 
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        site_petrobras = "https://precos.petrobras.com.br/sele%C3%A7%C3%A3o-de-estados-gasolina"
        driver.get(site_petrobras)
        time.sleep(2) # caso o site seja lento 
        preco_final = driver.find_element(By.ID,"telafinal-precofinal")
        preco_final = preco_final.text
    except Exception as e: 
        print(f"Erro no scraping: {e}")
        preco_final = None # em caso de erro retorna None 
    finally:
        driver.quit() # para garantir que o navegador feche 
    return preco_final 

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    preco_final = buscar_preco_real()
    if request.method == 'POST':
        # Captura dados do formulário
        dist = float(request.form.get('distancia'))
        cons = float(request.form.get('consumo'))
        prec = float(request.form.get('preco'))
        
        resultado = calcular_viagem(dist, cons, prec)
    
    return render_template('index.html', resultado=resultado, preco_final=preco_final)

if __name__ == '__main__':
    app.run(debug=True)