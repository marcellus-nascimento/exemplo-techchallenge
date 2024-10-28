# API de Dados Vitivinicultura - Embrapa 🍇

## 🎯Objetivo do Projeto
Este projeto é corresponde ao Tech Challenge da Pos Tech em Machine Learning Engineer da FIAP. Ele consiste em desenvolver uma API para acessar e processar dados de vitivinicultura do site da Embrapa, facilitando a extração de algumas informações de categorias como a produção, processamento, comercialização, importação e exportação de produtos vitivinícolas no Brasil. 

Algumas categorias possuem subcategorias próprias, como por exemplo em processamento, conseguimos ver a quantidade dos tipos de uvas produzidas, que são viníferas, americas e híbridas, uvas de mesa e até mesmo sem classificação. Com os dados obtidos via API, é possível realizar a análise exploratória de dados com geração de insigths e até mesmo modelos de ML.

## ➡️Plano de Deploy


## 💻Tecnologias Usadas
- **Python**: Linguagem principal do projeto
- **Flask**: Framework web para construção da API
- **Requests**: Biblioteca para requisições HTTP
- **BeautifulSoup**: Biblioteca para web scraping

## ⚙️Estrutura do Código

- **VitiviniculturaScraper**: Classe principal para a extração de dados. Define URLs para categorias específicas (produção, processamento, comercialização, importação e exportação) e contém métodos para raspagem e parseamento dos dados.
  - `scrape_data`: Extrai dados de acordo com o ano e a categoria/subcategoria selecionada.
  - `parse_html`: Converte dados HTML para formato estruturado.
- **Rotas da API**:
  - `/api/<category>`: Rota principal para acesso a dados de categorias específicas.
  - `/`: Página inicial com formulário para inserir o token de acesso.
  - `/submit_token`: Verificação do token de acesso e exibição do menu de navegação das rotas da API.

## 📝Instruções de Uso da API
1. **Clonar o Repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a API**:
   ```bash
   python app.py
   ```

4. **Acessar Rotas da API**:
   - Navegue até [http://localhost:5000](http://localhost:5000) para a página inicial.
   - Utilize o token `senhateste2024` para acessar o menu.

  **Menu da API de Dados Vitivinícolas**
  
  Escolha uma categoria e subcategoria para acessar os dados:
  
  1. **Dados de Produção**
     ```
     GET /api/producao
     ```
  
  2. **Dados de Processamento**
     - **Viníferas**
       ```
       GET /api/processamento?subcategory=viniferas
       ```
     - **Americanas e Híbridas**
       ```
       GET /api/processamento?subcategory=americanas_hibridas
       ```
     - **Uvas de Mesa**
       ```
       GET /api/processamento?subcategory=uvas_de_mesa
       ```
     - **Sem Classificação**
       ```
       GET /api/processamento?subcategory=sem_classificacao
       ```
  
  3. **Dados de Comercialização**
     ```
     GET /api/comercializacao
     ```
  
  4. **Dados de Importação**
     - **Vinhos de Mesa**
       ```
       GET /api/importacao?subcategory=vinhos_de_mesa
       ```
     - **Espumantes**
       ```
       GET /api/importacao?subcategory=espumantes
       ```
     - **Uvas Frescas**
       ```
       GET /api/importacao?subcategory=uvas_frescas
       ```
     - **Uvas Passas**
       ```
       GET /api/importacao?subcategory=uvas_passas
       ```
     - **Suco de Uva**
       ```
       GET /api/importacao?subcategory=suco_de_uva
       ```
  
  5. **Dados de Exportação**
     - **Vinhos de Mesa**
       ```
       GET /api/exportacao?subcategory=vinhos_de_mesa
       ```
     - **Espumantes**
       ```
       GET /api/exportacao?subcategory=espumantes
       ```
     - **Uvas Frescas**
       ```
       GET /api/exportacao?subcategory=uvas_frescas
       ```
     - **Suco de Uva**
       ```
       GET /api/exportacao?subcategory=suco_de_uva
       ```
  
  **Filtrando os Dados**
  
  Para cada rota, você pode adicionar os parâmetros `start_year` e `end_year` para filtrar os dados. A resposta obtida será no formato `JSON`. 
  
  **Exemplo de chamada de API:**
  ```http
  GET /api/producao?start_year=2010&end_year=2020
  ```


## 🔗Links Importantes
- [Documentação da API](https://flask.palletsprojects.com/)
- [Vídeo Explicativo do Youtube](https://requests.readthedocs.io/)
- [Site da Embrapa](https://www.crummy.com/software/BeautifulSoup/)

## 👥 Membros do Grupo
- 1
- 2
- 3
- 
