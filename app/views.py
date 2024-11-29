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
    
def gerar_todos_graficos():
    return [gerar_grafico('preco_por_carros'),
    gerar_grafico('preco_por_marca'),
    #gerar_grafico('preco_por_ano'),
    gerar_grafico('preco_por_combustivel'),
    gerar_grafico('preco_por_cambio')]



def home(request): 
    all_brands = DATASET['marca'].unique().tolist()
    years = [str(ano) for ano in range(1985, 2024)]

    if request.method == "POST":
        selected_brand = request.POST.get('brand', '')
        selected_model = request.POST.get('model', '')
        selected_combustivel = request.POST.get('combustivel', '')
        selected_cambio = request.POST.get('cambio', '')
        selected_ano = request.POST.get('ano', '')  
        selected_grafico = request.POST.get('grafico_tipo', 'preco_por_marca')
        data = request.POST

        # Obter os modelos com base na marca selecionada
        if selected_brand:
            all_models = DATASET.loc[DATASET['marca'] == selected_brand, 'modelo'].unique().tolist()
        else:
            all_models = []

        # Gera a previsão de preço com base nos atributos de entrada para o modelo de ML
        predicted_price = model_predict.predict_price(data)
        # Chave que indica para o HTML mostrar o resultado
        predict_key = 1

        # Gerar Grafico escolhendo a distribuicao
        grafico_uri = gerar_todos_graficos()

        # Se for uma requisição AJAX, retorna apenas o gráfico em formato JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Se for uma requisição AJAX, retorna apenas o gráfico em formato JSON
            return JsonResponse({'grafico_uri': grafico_uri})

        return render(request, 'home.html', {
            'marcas': all_brands, 
            'selected_brand': selected_brand,
            'selected_model': selected_model,
            'selected_combustivel': selected_combustivel,
            'selected_cambio': selected_cambio,
            'selected_grafico': selected_grafico,
            'anos': years,
            'selected_ano': selected_ano,
            'modelos': all_models, 
            'predict_key': predict_key,
            'predicted_price': predicted_price,
            'grafico_uri': grafico_uri
        })
    else:   
        predict_key = 0
        predicted_price = 0
        selected_grafico = 'preco_por_marca'

            # Gerar Grafico
        grafico_uri = gerar_todos_graficos()

        return render(request, 'home.html', {
            'marcas': all_brands,
            'anos': years,
            'predict_key': predict_key,
            'selected_grafico': selected_grafico,
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
