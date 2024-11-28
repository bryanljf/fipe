import urllib.parse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from app.apps import DATASET
from app.services import model_predict
from app.services.graficos import distribuicao_preco_por_ano, distribuicao_preco_por_cambio, distribuicao_preco_por_combustivel, distribuicao_preco_por_marca, pizza_precos
import matplotlib.pyplot as plt
import pandas as pd
import io, base64, urllib




# Funcao para gerar o grafico
# Basta quando quiser colocar o tipo de grafico que deseja na função como está no home
def gerar_grafico(tipo):
    if tipo == 'preco_por_carros':
        return pizza_precos(DATASET)
    elif tipo == 'preco_por_marca':
        return distribuicao_preco_por_marca(DATASET)
    elif tipo == 'preco_por_ano':
        return distribuicao_preco_por_ano(DATASET)
    elif tipo == 'preco_por_combustivel':
        return distribuicao_preco_por_combustivel(DATASET)
    elif tipo == 'preco_por_cambio':
        return distribuicao_preco_por_cambio(DATASET)
    else:
        raise ValueError("Tipo de gráfico inválido")


def home(request): 
    all_brands = DATASET['marca'].unique().tolist()
    years = list(range(1985,2024))  

    if request.method == "POST":
        print(request.POST)
        selected_brand = request.POST.get('brand', '')
        selected_model = request.POST.get('model', '')  
        data = request.POST

        predicted_price = model_predict.predict_price(data)
        predict_key = 1

        # Gerar Grafico escolhendo a distribuicao
        grafico_uri = gerar_grafico('preco_por_marca')

        return render(request, 'home.html', {
            'marcas': all_brands, 
            'selected_brand': selected_brand,
            'selected_model': selected_model,
            'anos': years,
            'predict_key': predict_key,
            'predicted_price': predicted_price,
            'grafico_uri': grafico_uri
            })
    else:   
        predict_key = 0
        predicted_price = 0

        # Gerar Grafico
        grafico_uri = gerar_grafico('preco_por_marca')

        return render(request, 'home.html', {
            'marcas': all_brands,
            'anos': years,
            'predict_key': predict_key,
            'predicted_price': predicted_price,
            'grafico_uri': grafico_uri
            })
    
def get_models(request):
    # Rota para retornar os modelos baseado na marca
    selected_brand = request.GET.get('marca', '')
    if selected_brand:
        all_models = DATASET.loc[DATASET['marca'] == selected_brand, 'modelo'].unique().tolist()
    else:
        all_models = []

    return JsonResponse({'modelos': all_models})
