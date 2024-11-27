from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib

def loadData():
    df = pd.read_csv('../static/data/tabela-fipe-historico-precos.csv')
    le = LabelEncoder()

    df['marca_'] = le.fit_transform(df['marca'])
    df['modelo_'] = le.fit_transform(df['modelo'])

    df = df.drop(dcolumns=['marca'])
    df = df.drop(dcolumns=['modelo'])

    joblib.dump(le, '../static/media/label_encoder.pkl')

    return df




