import os
from django.http import JsonResponse
import joblib
import pandas as pd
from app.apps import DATASET
from fipe.settings import BASE_DIR
from app.services import data_loader

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
            'combustivel': [combustivel],
            'cambio': [cambio],
            'idade_veiculo': [idade_veiculo]
        })

        print(features)

        # Prever o preço utilizando o modelo treinado
        predicted_price = model.predict(features)[0]

        # Retornar a previsão 
        return predicted_price

def convert_strings(marca, modelo):
    # Criar um mapa das marcas e modelos (convertendo as strings em índices numéricos)
    brand_map = {marca: idx for idx, marca in enumerate(DATASET['marca'].unique().tolist())}
    model_map = {modelo: idx for idx, modelo in enumerate(DATASET['modelo'].unique().tolist())}

    # Verifica se a marca e o modelo fornecidos estão no conjunto de dados
    if marca not in brand_map:
        raise ValueError(f"Marca não encontrada no dataset: {marca}")
    if modelo not in model_map:
        raise ValueError(f"Modelo não encontrado no dataset: {modelo}")

    # Retorna os códigos numéricos para a marca e o modelo fornecidos
    return {
        'marca': brand_map[marca],  # Retorna o código da marca fornecida
        'modelo': model_map[modelo]  # Retorna o código do modelo fornecido
    }
