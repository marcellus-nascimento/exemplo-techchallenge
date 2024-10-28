from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from scraper import VitiviniculturaScraper

# Inicializo a aplicação Flask
app = Flask(__name__)

# Configurações do JWT para autenticação
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Troque para uma chave secreta mais segura
jwt = JWTManager(app)

# Crio uma instância do scraper para ser usada nas rotas
scraper = VitiviniculturaScraper()

# Função para gerar um token JWT
@app.route('/token', methods=['POST'])
def login():
    access_token = create_access_token(identity='user')
    return jsonify(access_token=access_token), 200

# Rota principal da API para acessar os dados, protegida por autenticação JWT
@app.route('/api/<category>', methods=['GET'])
@jwt_required()  # Requer token para acessar
def get_data(category):
    start_year = request.args.get('start_year', default=1970, type=int)
    end_year = request.args.get('end_year', default=2023, type=int)
    
    # Subcategoria para as abas que possuem filtragem adicional
    subcategory = request.args.get('subcategory', default=None, type=str)
    
    # Verifico se a categoria solicitada está nas opções válidas
    if category not in scraper.BASE_URLS:
        return jsonify({"error": "Categoria inválida"}), 400

    # Verifico se a subcategoria é válida para a categoria escolhida
    if category in ['processamento', 'importacao', 'exportacao'] and subcategory not in scraper.SUBCATEGORIES[category]:
        return jsonify({"error": "Subcategoria inválida para a categoria selecionada"}), 400

    # Chamo o método de scraping passando os parâmetros recebidos
    data = scraper.scrape_data(start_year, end_year, category, subcategory)
    return jsonify(data)

# Função para solicitar o token de acesso
def request_access_token():
    import requests

    # URL do endpoint para gerar o token
    url = "http://127.0.0.1:5000/token"
    
    # Faz a requisição para obter o token
    response = requests.post(url)
    
    if response.status_code == 200:
        token = response.json().get("access_token")
        print(f"Token de acesso: {token}")
        return token
    else:
        print("Erro ao solicitar o token")
        return None

# Rota de menu para facilitar a navegação na API, com links e instruções
@app.route('/')
def home():
    return """
    <h1>Bem-vindo à API de Dados Vitivinícolas!</h1>
    <p>Use as rotas abaixo para acessar os dados:</p>
    <ul>
        <li><a href="/api/producao">/api/producao</a>: Dados de Produção.</li>
        <li><a href="/api/processamento?subcategory=viniferas">/api/processamento?subcategory=viniferas</a>: Dados de Viníferas.</li>
        <li><a href="/api/processamento?subcategory=americanas_hibridas">/api/processamento?subcategory=americanas_hibridas</a>: Dados de Americanas e Híbridas.</li>
        <li><a href="/api/processamento?subcategory=uvas_de_mesa">/api/processamento?subcategory=uvas_de_mesa</a>: Dados de Uvas de Mesa.</li>
        <li><a href="/api/processamento?subcategory=sem_classificacao">/api/processamento?subcategory=sem_classificacao</a>: Sem Classificação.</li>
        <li><a href="/api/comercializacao">/api/comercializacao</a>: Dados de Comercialização.</li>
        <li><a href="/api/importacao?subcategory=vinhos_de_mesa">/api/importacao?subcategory=vinhos_de_mesa</a>: Vinhos de Mesa (Importação).</li>
        <li><a href="/api/importacao?subcategory=espumantes">/api/importacao?subcategory=espumantes</a>: Espumantes (Importação).</li>
        <li><a href="/api/importacao?subcategory=uvas_frescas">/api/importacao?subcategory=uvas_frescas</a>: Uvas Frescas (Importação).</li>
        <li><a href="/api/importacao?subcategory=uvas_passas">/api/importacao?subcategory=uvas_passas</a>: Uvas Passas (Importação).</li>
        <li><a href="/api/importacao?subcategory=suco_de_uva">/api/importacao?subcategory=suco_de_uva</a>: Suco de Uva (Importação).</li>
        <li><a href="/api/exportacao?subcategory=vinhos_de_mesa">/api/exportacao?subcategory=vinhos_de_mesa</a>: Vinhos de Mesa (Exportação).</li>
        <li><a href="/api/exportacao?subcategory=espumantes">/api/exportacao?subcategory=espumantes</a>: Espumantes (Exportação).</li>
        <li><a href="/api/exportacao?subcategory=uvas_frescas">/api/exportacao?subcategory=uvas_frescas</a>: Uvas Frescas (Exportação).</li>
        <li><a href="/api/exportacao?subcategory=suco_de_uva">/api/exportacao?subcategory=suco_de_uva</a>: Suco de Uva (Exportação).</li>
    </ul>
    <p>Para cada rota, você pode adicionar parâmetros <code>start_year</code>, <code>end_year</code> e <code>subcategory</code> (quando aplicável) para filtrar os dados.</p>
    """

# Inicializo o servidor da API
if __name__ == '__main__':
    app.run(debug=True)
