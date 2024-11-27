from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Treinamento do modelo com base no dataset

def trainModel(df):
    x = df.drop(columns=['preco_medio_FIPE'])
    y = df['preco_medio_FIPE']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    joblib.dump(model, '../static/media/model_fipe.pkl')

    return