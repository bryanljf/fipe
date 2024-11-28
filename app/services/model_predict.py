from django.http import JsonResponse
import joblib
import pandas as pd

# Previsão de preço, com base nas informações de entrada através do aprendizado de máquina

# ------------------------REVER nomenclatura-------------------------
def predictPrice(request):
    if request.method == 'POST':
        # Carregar o modelo treinado
        model = joblib.load('../static/media/model_fipe.pkl')
        # Carregar o codificador de rótulos para transformar marcas e modelos
        le = joblib.load('../static/media/label_encoder.pkl')
        data = request.POST
        
        # Extrair informações do POST request
        marca = data['marca']
        modelo = data['modelo']
        anoModelo = int(data['anoModelo'])
        anoReferencia = int(data['anoReferencia'])

        # Transformar marca e modelo para valores numéricos
        marca_ = le.transform([marca])[0]
        modelo_ = le.transform([modelo])[0]

        # Criar um DataFrame com as características para previsão
        features = pd.DataFrame({
            'marca': [marca_],
            'modelo': [modelo_],
            'anoModelo': [anoModelo],
            'anoReferencia': [anoReferencia]
        })

        # Prever o preço utilizando o modelo treinado
        predicted_price = model.predict(features)[0]

        # Retornar a previsão em formato JSON
        return JsonResponse({'predicted_price': predicted_price})

    return JsonResponse({'error': 'Método POST requerido'}, status=400)
