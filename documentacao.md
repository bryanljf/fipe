
# TEMA:
Previsão de Valores de Carros com base na tabela FIPE


# CRONOGRAMA
01/11/2024 - 07/11/2024
- Planejamento do projeto
- Definição do escopo
- Definição da equipe
- criação do cronograma
- divisão de tarefas

08/11/2024 - 14/11/2024
- configuração do ambiente de desenvolvimento
- limpeza e preparação dos dados
- design e estrutura das Views e templetes

15/11/2024 - 21/11/2024
- implementação algoritimo de machine learning
- integração da predição Django
- adição dos graficos

22/11/2024 - 29/11/2024
- testes e ajustes finais
- finalização da documentação


## Tecnologias Utilizadas

- **Django:** Framework de desenvolvimento web em Python, utilizado para construir o backend do projeto.
- **HTML/CSS:** Utilizados para o frontend, proporcionando uma interface de usuário simples e funcional.
- **SQLite:** Banco de dados padrão utilizado pelo Django para armazenamento de dados, mas pode ser substituído por outros sistemas de gerenciamento de banco de dados (MySQL, PostgreSQL, etc.).
- **Pandas:** Biblioteca de manipulação e análise de dados.
- **Matplotlib:** Biblioteca de visualização de dados em Python.
- **Scikit-learn:** Biblioteca de aprendizado de máquina em Python.
- **JavaScript:** Linguagem de programação utilizada para adicionar interatividade à interface do usuário.

# Divisão de tarefas

- Alysson: Desenvolvimento da aplicação web (Django/Flask).
- Vinicius: Manipulação de dados, EDA, e criação de gráficos (Pandas, Seaborn, Matplotlib).
- Bryan: Modelagem de machine learning e integração do modelo (Scikit-learn).
- Lucas: Documentação, elaboração do README e preparação da apresentação.

# Funcionalidades

- **Seleção de Graficos:** o usuario seleciona o grafico dentre as seguintes opcoes
-   - Grafico de Preço por marca
-   - Grafico de Preço por faixas
-   - Grafico de Preço por tipo de cambio
-   - Grafico de Preço por tipo de combustivel
- **Previsão de Preço:** o usuario insere os dados do veiculo e o sistema retorna a previsão do preço do veiculo


fipe/
├── manage.py               
├── fipe/                   
│   ├── __init__.py         
│   ├── settings.py             
│   ├── urls.py             
│   ├── wsgi.py
│   ├── asgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── app/
│   │   │   ├── home.html
│   ├── static/
│   │   ├── app/
│   │   │   ├── css/
│   │   │   │   ├── base.css
│   │   │   ├── media/
│   │   │   │   ├── model_fipe.pkl
│   │   │   ├── data/
│   │   │   │   ├── fipe_2022.csv
│   │   │   │   ├── fipe_2022_processed.csv
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── graficos.py
│   │   ├── model_predict.py
│   │   ├── ml_model.py
│   │   ├── util.py
├── db.slite3
├── documentacao.md
├── README.md
