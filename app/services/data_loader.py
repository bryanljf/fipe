import os
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib
from fipe.settings import BASE_DIR

csv_path = os.path.join(BASE_DIR, 'app', 'static', 'data', 'fipe_2022.csv')
pd.set_option('display.max_rows', 200)

output_path = os.path.join(BASE_DIR, 'app', 'static', 'data', 'fipe_2022_processed.csv')

def load_data():
    # Carregando o arquivo CSV
    df = pd.read_csv(csv_path)

    # Remove linhas com valores nulos
    df.dropna(axis=0, inplace=True) 

    # Remove as duplicatas de dados
    df.drop_duplicates(inplace=True)

    # Removendo as colunas desnecessárias
    df.drop(columns=['authentication', 'fipe_code'], inplace=True)

    # Renomeando as colunas para português
    df.rename(columns={
        'brand': 'marca',    
        'model': 'modelo',
        'fuel': 'combustivel',
        'gear': 'cambio',
        'avg_price_brl': 'preco_medio_FIPE',
        'age_years': 'idade_veiculo'
    }, inplace=True)

    # Remove outliers (valores discrepantes) da coluna 'preco_medio_FIPE'
    df = remove_outliers(df)

    # Mapear variáveis categóricas para números
    df = data_maps(df)

    df.to_csv(output_path, index=False)
    
    return df

# Função para mapear dados categóricos e transformar em numéricos
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def data_maps(df: pd.DataFrame) -> pd.DataFrame:
    # Dicionários de mapeamento para variáveis categóricas
    tipos_combustivel = {'Gasoline': 0, 'Diesel': 1, 'Alcohol': 2}
    tipos_cambio = {'manual': 0, 'automatic': 1}

    # Transformando as colunas 'marca' e 'modelo' em valores numéricos com LabelEncoder
    le_marca = LabelEncoder()
    le_modelo = LabelEncoder()

    df['marca_code'] = le_marca.fit_transform(df['marca'])
    df['modelo_code'] = le_modelo.fit_transform(df['modelo'])

    # Aplicando o mapeamento manual para as outras colunas categóricas
    df['combustivel_code'] = df['combustivel'].map(tipos_combustivel)
    df['cambio_code'] = df['cambio'].map(tipos_cambio)

    # Mantendo apenas as colunas relevantes
    columns_to_keep = ['modelo', 'marca', 'preco_medio_FIPE', 'modelo_code', 'combustivel_code', 'cambio_code', 'marca_code', 'idade_veiculo', 'year_model']
    df = df.drop(columns=[col for col in df.columns if col not in columns_to_keep]) # Mantém apenas as colunas especificadas  
  

    # Renomeando as colunas para refletir o código mapeado
    df.rename(columns={
        'combustivel_code': 'combustivel',
        'cambio_code': 'cambio'
    }, inplace=True)

    return df

# Função para remover outliers da coluna 'preco_medio_FIPE'
def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    # Garantir que não existam valores nulos na coluna 'preco_medio_FIPE'
    df = df[df['preco_medio_FIPE'].notnull()]

    # Calculando o primeiro e o terceiro quartis
    q1 = df['preco_medio_FIPE'].quantile(0.25)
    q3 = df['preco_medio_FIPE'].quantile(0.75)
    
    # Calculando o intervalo interquartil (IQR)
    iqr = q3 - q1
    
    # Filtrando o DataFrame para remover os outliers (valores fora de 1.5 * IQR)
    df = df[(df['preco_medio_FIPE'] >= (q1 - 1.5 * iqr)) & (df['preco_medio_FIPE'] <= (q3 + 1.5 * iqr))]

    return df
