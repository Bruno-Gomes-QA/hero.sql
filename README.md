<p align="center">
<b></b>
</p>
<div>
  <h2 id="Introdução">Introdução 🎯</h2>
Olá, seja bem-vindo! Hero.SQL é uma iniciativa para ensinar os fundamentos de SQL (Structured Query Language) de uma maneira envolvente. O jogo se passa em um cenário medieval onde os jogadores assumem o papel de um assistente do Rei Queryon. O objetivo do jogo é ajudar o rei a organizar seu reino criando e manipulando bancos de dados.

</div>
<b></b>
<div align="center">
  <img src="https://github.com/user-attachments/assets/d0bb0cbe-7a42-4d6a-b8b5-4f1ec341e72a" width="30%">
  <img src="https://github.com/user-attachments/assets/b3356ad7-e0bf-42da-bff3-58ce9a32a185" width="30%">
  <img src="https://github.com/user-attachments/assets/098abe48-c214-43fe-b865-a07450cc7809" width="30%">
</div>

<div>
  <h2 id="Estrutura">Estrutura 🛠️</h2>

Hero.SQL foi desenvolvido utilizando uma estrutura de pastas modulares com o objetivo de separar as funcionalidades/responsabilidades de forma organizada e concissa. 

### ./

- **pyproject.toml**: Arquivo de configuração do Poetry, que especifica as dependências do projeto e outras configurações.
- **poetry.lock**: Arquivo gerado pelo Poetry para garantir que todas as dependências sejam instaladas na versão correta.
- **.streamlit**: Pasta que armazena as configurações da aplicação streamlit.
- **app.py**: Ponto de entrada para aplicação, inicializa todos os states e conexões.

### database/

Responsável por cuidar da conexão com o banco de dados, executar querys e gerenciar conexões

### functions/

Módulo responsável pelas funções presentes na aplicação.

### pages/

Com objetivo de gerenciar as páginas, /pages armazera e gerencia a nagevação do app.

### assets/

Armazena todos os assets do app, como imagens, áudio e frames.
</div>

<h2 id="Running">Executando o projeto 🏃</h2>

Para rodar o projeto localmente devemos seguir as seguintes etapas:

Pré-Requisitos

- Python ^3.9.16
- MySQL

Em seu terminal clone o projeto:

```bash
git clone https://github.com/Bruno-Gomes-QA/Reeduc.git
```

Agora instale o poetry
```bash
pip install poetry
```
Deixe que o proetry cuide das dependências
```bash
poetry install
poetry shell
```

Crie um arquivo .env na raiz do projeto com os seguintes valores:
```bash
MYSQL_USER=seu_user_root
MYSQL_PASSWORD=sua_senha
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=hero_sql
CASTELO_USER=sir_schema
CASTELO_PASSWORD=queryon
```

Rode o script para configuração inicial do banco de dados:

```bash
python create_app.py
```

Pronto agora basta rodar:
```bash
streamlit run app.py
```

E acessar http://localhost:8501

<h2 id="Contribuição">Contribuição 🚀</h2>

Para contribuir com o projeto pode seguir as seguintes etapas:

```bash
git clone https://github.com/Bruno-Gomes-QA/Reeduc.git
```

```bash
git checkout -b feat/feature-name
```
Importante seguir o padrão para commits:

| Tipo | Descrição |
|---|---|
| feat | Nova funcionalidade |
| fix | Correção de bug |
| docs | Mudanças na documentação |
| style | Formatação, pontos e vírgulas ausentes, etc. |
| refactor | Refatoração do código de produção, por exemplo, renomeação de uma variável |
| test | Adicionando testes ausentes, refatorando testes |

[Como criar um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) |
[Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

<h2 id="license">License 📃 </h2>

Este projeto utiliza licença [MIT](./LICENSE) 



