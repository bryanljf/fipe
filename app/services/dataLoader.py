"""
services/dataLoader.py
serve para carregar os dados do arquivo csv e fazer o tratamento dos dados
"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib


def load_data():
    # Carregando o arquivo CSV
    df = pd.read_csv('static/data/tabela-fipe-historico-precos.csv')

    df.dropna(axis=0, inplace=True)  # Remove linhas com valores nulos

    df.drop_duplicates(inplace=True)  # Remove as duplicatas de dados

    # Removendo as colunas desnecessárias
    df.drop(columns=['authentication', 'fipe_code'], inplace=True)

    # Renomeando as colunas para portugues
    df.rename(columns={'year_of_reference': 'ano_de_referencia',
                       'month_of_reference': 'mes_de_referencia',
                       'brand': 'marca',
                       'model': 'modelo',
                       'fuel': 'combustivel',
                       'gear': 'cambio',
                       'engine_size': 'potencia_do_motor',
                       'year_model': 'ano_modelo',
                       'avg_price_brl': 'preco_medio_FIPE',
                       'age_years': 'idade_veiculo'
                       },
              inplace=True)

    df = remove_outliers(df)  # Remove dados discrepantes (outliers)

    df = data_maps(df) # Converte dados categóricos para numeros

    return df


def loadBrands():
    # Carregando o arquivo CSV
    df = pd.read_csv('../static/data/tabela-fipe-historico-precos.csv')

    #Extraindo todas as marcas únicas
    all_brands = df['marca'].unique().tolist()

    return all_brands


# Função para mapear os dados categoricos e tranfosmar em numericos
def data_maps(df: pd.DataFrame) -> pd.DataFrame:

    # Lista de marcas para mapeamento
    marcas = ['Acura', 'Agrale', 'Alfa Romeo', 'AM Gen', 'Asia Motors', 'ASTON MARTIN',
              'Audi', 'Baby', 'BMW', 'BRM', 'CAB Motors', 'Cadillac', 'CBT Jipe', 'CHANA',
              'CHANGAN', 'Caoa Chery', 'GM - Chevrolet', 'Chrysler', 'Citroën',
              'Cross Lander', 'Daewoo', 'Daihatsu', 'Dodge', 'EFFA', 'Engesa', 'Envemo',
              'Ferrari', 'Fiat', 'Fibravan', 'Ford', 'FOTON', 'Fyber', 'GEELY', 'GREAT WALL',
              'HAFEI', 'Honda', 'Hyundai', 'Isuzu', 'IVECO', 'JAC', 'Jaguar', 'Jeep', 'JINBEI',
              'JPX', 'Kia Motors', 'Lada', 'Land Rover', 'Lexus', 'LIFAN', 'LOBINI', 'Lotus',
              'Mahindra', 'Maserati', 'Matra', 'Mazda', 'Mclaren', 'Mercedes-Benz', 'Mercury',
              'MG', 'MINI', 'Mitsubishi', 'Nissan', 'Peugeot', 'Plymouth', 'Pontiac',
              'Porsche', 'RAM', 'RELY', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Saturn',
              'Seat', 'SHINERAY', 'smart', 'SSANGYONG', 'Subaru', 'Suzuki', 'TAC', 'Toyota',
              'Troller', 'VW - VolksWagen', 'Volvo', 'Wake', 'Walk']
    # Criando um cicionário de mapeamento de marcas
    marcas_map = {marca: idx for idx, marca in enumerate(marcas)} 
    # Dicionario de mapeamento para tipos de combustível
    tipos_combustivel = {'Gasoline': 0, 'Diesel': 1, 'Alcohol': 2}
    # Dicionario de mapeamento para tipos de cambio
    tipos_cambio = {'manual': 0, 'automatic': 1}
    # Dicionario de mapeamento para meses
    mapeamento_mes = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
        'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
        'November': 11, 'December': 12
    }

    # Transformando modelos em valores númericos
    le = LabelEncoder()
    df['modelo_Code'] = le.fit_transform(df['modelo'])

    # Aplicando os mapeamentos ás colunas do DataFrame
    df['mes_de_referencia'] = df['mes_de_referencia'].map(mapeamento_mes)
    df['marca_code'] = df['marca'].map(marcas_map)
    df['combustivel_code'] = df['combustivel'].map(tipos_combustivel)
    df['cambio_code'] = df['cambio'].map(tipos_cambio)

    return df


# Essa funcão faz uma correção nos preços pois tem uma variancia muito desproporcional entre o maior e menor valor
def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    # Calculando o primeiro quartil
    q1 = df['preco_medio_FIPE'].quantile(0.25)  
    # Calculando o terceiro quartil
    q3 = df['preco_medio_FIPE'].quantile(0.75)  # terceiro quartil
    # Calculando o intervalo interquartil (IQR)
    iqr = q3 - q1  
    # Filtrando o DataFrame para remover outliers
    df = df[(df['preco_medio_FIPE'] >= (q1 - 1.5 * iqr)) & (df['preco_medio_FIPE'] <= (q3 + 1.5 * iqr))]

    return df
