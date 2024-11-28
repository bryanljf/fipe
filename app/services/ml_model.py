import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from fipe.settings import BASE_DIR

pkl_path = os.path.join(BASE_DIR, 'app', 'static', 'media', 'model_fipe.pkl')

# Treinamento do modelo com base no dataset
def trainModel(df):
    # Definindo as variáveis independentes (X) removendo colunas não necessárias para a previsão
    x = df[['marca_code', 'modelo_code', 'combustivel', 'cambio', 'idade_veiculo']]

    # Definindo a variável dependente (y) que queremos prever
    y = df['preco_medio_FIPE']

    # Dividindo os dados em conjuntos de treinamento e teste (80% treino, 20% teste)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Instanciando o modelo de Regressão com Floresta Aleatória com 100 árvores
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Treinando o modelo com os dados de treinamento
    model.fit(x_train, y_train)
    
    # Salvando o modelo treinado em um arquivo .pkl usando joblib
    joblib.dump(model, pkl_path)

    return