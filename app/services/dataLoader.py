"""services/dataLoader.py
serve para carregar os dados do arquivo csv e fazer o tratamento dos dados
"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib


def load_data():
    df = pd.read_csv('static/data/tabela-fipe-historico-precos.csv')

    df.dropna(axis=0, inplace=True)  # Remove linhas com valores nulos

    df.drop_duplicates(inplace=True)  # remove as duplicatas de dados

    # removendo as colunas do codigo e da autenticação pois não serão necessarias
    df.drop(columns=['authentication', 'fipe_code'], inplace=True)

    # renomeando as colunas para portugues
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

    df = data_maps(df)

    return df


def loadBrands():
    df = pd.read_csv('../static/data/tabela-fipe-historico-precos.csv')

    all_brands = df['marca'].unique().tolist()

    return all_brands


# Função para mapear os dados categoricos e tranfosmar em numericos
def data_maps(df: pd.DataFrame) -> pd.DataFrame:

    # o mapeamento abaixo coloca numero para cada marca, tipo de combustivel, tipo de cambio e mes
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
    marcas_map = {marca: idx for idx, marca in enumerate(marcas)} # numeração automatica das marcas

    tipos_combustivel = {'Gasoline': 0, 'Diesel': 1, 'Alcohol': 2}
    tipos_cambio = {'manual': 0, 'automatic': 1}
    mapeamento_mes = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
        'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
        'November': 11, 'December': 12
    }

    # label enconder transforma em numeros os modelos
    le = LabelEncoder()
    df['modelo'] = le.fit_transform(df['modelo'])

    # fazendo novas colunas com as numerações respectivas do mapeamento
    df['mes_de_referencia'] = df['mes_de_referencia'].map(mapeamento_mes)
    df['marca_Code'] = df['marca'].map(marcas_map)
    df['combustivel_Code'] = df['combustivel'].map(tipos_combustivel)
    df['cambio_Code'] = df['cambio'].map(tipos_cambio)

    return df
