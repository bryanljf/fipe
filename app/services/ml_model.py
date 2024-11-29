import os
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from fipe.settings import BASE_DIR

pkl_path = os.path.join(BASE_DIR, 'app', 'static', 'media', 'model_fipe.pkl')

# Treinamento do modelo com base no dataset
def train_model(df):
    # Definindo as variáveis independentes (X), removendo colunas não necessárias para a previsão
    X = df[['marca_code', 'modelo_code', 'combustivel_code', 'cambio_code', 'idade_veiculo']]
    
    # Definindo a variável dependente (y) que queremos prever
    y = df['preco_medio_FIPE']

    # Dividindo os dados em conjuntos de treinamento e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instanciando o modelo de Regressão com Floresta Aleatória com 100 árvores
    model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1, max_depth=20, max_features='log2')

    # Treinando o modelo com os dados de treinamento
    model.fit(X_train, y_train)
    
    # Prevendo os preços no conjunto de teste
    y_pred = model.predict(X_test)
    
    # Calculando o R² (coeficiente de determinação) e MAE (Erro Absoluto Médio)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    # Realizando validação cruzada (5 folds)
    cv_r2_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    cv_mae_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')  # MAE negativo porque o sklearn maximiza as métricas

    # Exibindo as métricas
    print(f'R² (Coeficiente de Determinação) no conjunto de teste: {r2}')
    print(f'MAE (Erro Absoluto Médio) no conjunto de teste: {mae}')
    
    print(f'R² Médio na Validação Cruzada: {cv_r2_scores.mean()} ± {cv_r2_scores.std()}')
    print(f'MAE Médio na Validação Cruzada: {-cv_mae_scores.mean()} ± {-cv_mae_scores.std()}')  # Tornando MAE positivo

    # Salvando o modelo treinado em um arquivo .pkl usando joblib
    joblib.dump(model, pkl_path)