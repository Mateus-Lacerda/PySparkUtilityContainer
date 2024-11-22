# PySpark Container

![License](https://img.shields.io/github/license/Mateus-Lacerda/PySparkUtilityContainer)

## Descrição

O **PySpark Container** é uma aplicação web construída com **FastAPI** e **PySpark**, containerizada utilizando **Docker** e orquestrada com **Docker Compose**. Esta aplicação permite o upload de arquivos CSV, a criação de DataFrames temporários no Spark, a execução de consultas SQL e a visualização dos dados diretamente através de uma interface web intuitiva.

## Funcionalidades

- **Upload de Arquivos CSV:** Carregue arquivos CSV que são automaticamente convertidos em DataFrames do Spark.
- **Execução de Consultas SQL:** Execute consultas SQL sobre os DataFrames temporários criados.
- **Visualização de Dados:** Visualize os resultados das consultas diretamente no navegador.
- **Verificação de Saúde da Aplicação:** Endpoint para monitorar o status da aplicação.
- **Interface Web Intuitiva:** Páginas HTML para facilitar a interação com a aplicação.

## Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI**
- **PySpark 3.2.0**
- **Docker**
- **Docker Compose**
- **HTML, CSS, JavaScript**

## Estrutura do Projeto

```
pyspark_container/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── src/
│   ├── app/
│   │   ├── app.py
│   │   └── spark.py
│   ├── entrypoint.py
│   └── static/
│       ├── index.html
│       ├── upload.html
│       ├── visualize.html
│       ├── query.html
│       ├── styles.css
│       └── scripts.js
```

## Instalação

### Pré-requisitos

- **Docker:** [Instale o Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Instale o Docker Compose](https://docs.docker.com/compose/install/)

### Passos para Configuração

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/Mateus-Lacerda/PySparkUtilityContainer.git
   cd PySparkUtilityContainer
   ```

2. **Construir e Iniciar os Serviços com Docker Compose**

   ```bash
   docker-compose up --build
   ```

   Este comando irá construir a imagem Docker e iniciar os containers definidos no 

docker-compose.yml

.

3. **Acessar a Aplicação**

   Abra o seu navegador e navegue até: [http://localhost:8000](http://localhost:8000)

## Uso

### Endpoints Disponíveis

- **Verificação de Saúde**

  - **URL:** `/health`
  - **Método:** `GET`
  - **Descrição:** Retorna o status da aplicação.
  - **Exemplo de Resposta:**
    ```json
    {
      "status": "ok"
    }
    ```

- **Upload de Arquivo CSV**

  - **URL:** `/upload_file`
  - **Método:** `POST`
  - **Descrição:** Faz o upload de um arquivo CSV e cria um DataFrame temporário no Spark.
  - **Parâmetros:**
    - `file`: Arquivo CSV a ser enviado.

- **Execução de Consulta SQL**

  - **URL:** `/api/v1/query`
  - **Método:** `GET`
  - **Descrição:** Executa uma consulta SQL sobre os DataFrames temporários.
  - **Parâmetros de Consulta:**
    - `q`: A consulta SQL a ser executada (exemplo: `SELECT * FROM sua_tabela LIMIT 100`).

- **Criação de DataFrame a partir de Dicionário**

  - **URL:** `/api/v1/create_dataframe`
  - **Método:** `PUT`
  - **Descrição:** Cria um DataFrame a partir de um dicionário ou lista com um esquema especificado.
  - **Corpo da Requisição:**
    ```json
    {
      "data": [/* sua lista ou dicionário */],
      "schema": "nome_do_schema"
    }
    ```

- **Criação de View Temporária**

  - **URL:** `/api/v1/create_temp_view`
  - **Método:** `PUT`
  - **Descrição:** Cria uma view temporária a partir de um DataFrame existente.
  - **Corpo da Requisição:**
    ```json
    {
      "df": "nome_do_dataframe",
      "name": "nome_da_view"
    }
    ```

### Interface Web

- **Página Inicial**

  - **URL:** `/`
  - **Descrição:** Página inicial da aplicação.

- **Upload de Arquivo**

  - **URL:** `/upload`
  - **Descrição:** Interface para upload de arquivos CSV.

- **Visualizar Dados**

  - **URL:** `/visualize`
  - **Descrição:** Interface para visualizar os dados das consultas.

- **Consultar Dados**

  - **URL:** `/query`
  - **Descrição:** Interface para executar consultas SQL.

## Frontend

O frontend é composto por arquivos HTML, CSS e JavaScript localizados na pasta 

static

. O arquivo `scripts.js` gerencia as interações com a API, como upload de arquivos e execução de consultas.

## Desenvolvimento

### Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para desenvolvimento:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Documentação da API

A **FastAPI** fornece documentação automática e interativa disponível em:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Nota:** Certifique-se de substituir `yourdockerhubusername`, `seuusuario`, e outros placeholders com suas informações reais.

Se tiver dúvidas ou precisar de assistência adicional, sinta-se à vontade para entrar em contato!