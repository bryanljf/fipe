from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib

# Carregamento e tratamento dos dados do dataset

def loadData():
    df = pd.read_csv('../static/data/tabela-fipe-historico-precos.csv')
    le = LabelEncoder()

    df['marca_'] = le.fit_transform(df['marca'])
    df['modelo_'] = le.fit_transform(df['modelo'])

    df = df.drop(dcolumns=['marca'])
    df = df.drop(dcolumns=['modelo'])

    joblib.dump(le, '../static/media/label_encoder.pkl')

    return df

def loadBrands():
    df = pd.read_csv('../static/data/tabela-fipe-historico-precos.csv')

    all_brands = df['marca'].unique().tolist()

    return all_brands





