import os
from django.http import JsonResponse
import joblib
import pandas as pd
from app.apps import DATASET
from fipe.settings import BASE_DIR

# Previsão de preço, com base nas informações de entrada através do aprendizado de máquina
pkl_path = os.path.join(BASE_DIR, 'app', 'static', 'media', 'model_fipe.pkl')

def predict_price(data):
        # Carregar o modelo treinado
        model = joblib.load(pkl_path)
        
        # Extrair informações do request
        marca_string = data['brand']
        modelo_string = data['model']
        combustivel_string = data['combustivel']
        cambio_string = data['cambio']

        conversion = convert_strings(marca_string, modelo_string)

        marca = conversion['marca'] # Recupera o código numérico da marca
        modelo = conversion['modelo']  # Recupera o código numérico do modelo

        # Recupera o código numérico do tipo de combustivel
        if (combustivel_string == "Gasoline"):
            combustivel = 0
        elif (combustivel_string == "Diesel"):
            combustivel = 1
        elif (combustivel_string == "Alcohol"):
            combustivel = 2

        # Recupera o código numérico do tipo de cambio
        if (cambio_string == "manual"):
            cambio = 0
        else:
            cambio = 1

        # Calcula a idade do veículo, com base nas informações de entrada
        # Considerado ano 2023, pois a coleta de dados do dataset foi feita nesse ano
        idade_veiculo = 2023 - int(data['ano'])

        # Criar um DataFrame com as características para previsão
        features = pd.DataFrame({
            'marca_code': [marca],
            'modelo_code': [modelo],
            'combustivel_code': [combustivel],
            'cambio_code': [cambio],
            'idade_veiculo': [idade_veiculo]
        })

        # Prever o preço utilizando o modelo treinado
        predicted_price = model.predict(features)[0]

        # Arredondar o valor para o múltiplo de 500 mais próximo
        rounded_price = round(predicted_price / 500) * 500

        # Arredondar para inteiro
        rounded_price_int = int(rounded_price)

        # Formatar o valor como R$ e incluir pontos nos milhares
        formatted_price = f"R$ {rounded_price_int:,}".replace(",", ".")

        # Retornar o preço formatado
        return formatted_price


def convert_strings(marca, modelo):
    # Buscar os códigos da marca e do modelo no dataset
    marca_code = DATASET.loc[DATASET['marca'] == marca, 'marca_code']
    modelo_code = DATASET.loc[DATASET['modelo'] == modelo, 'modelo_code']

    # Verificar se encontrou exatamente um código para cada, se não, gerar erro
    if marca_code.empty:
        raise ValueError(f"Marca '{marca}' não encontrada.")
    if modelo_code.empty:
        raise ValueError(f"Modelo '{modelo}' não encontrado.")
    
    return {
        'marca': marca_code.iloc[0],  # Retorna o primeiro código encontrado
        'modelo': modelo_code.iloc[0] 
    }
