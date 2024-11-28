from django.http import JsonResponse
import joblib
import pandas as pd

# Previsão de preço, com base nas informações de entrada através do aprendizado de máquina

# ------------------------REVER nomenclatura-------------------------
def predictPrice(request):
    if request.method == 'POST':
        model = joblib.load('../static/media/model_fipe.pkl')
        le = joblib.load('../static/media/label_encoder.pkl')
        data = request.POST

        marca = data['marca']
        modelo = data['modelo']
        anoModelo = int(data['anoModelo'])
        anoReferencia = int(data['anoReferencia'])

        marca_ = le.transform([marca])[0]
        modelo_ = le.transform([modelo])[0]

        features = pd.DataFrame({
            'marca': [marca_],
            'modelo': [modelo_],
            'anoModelo': [anoModelo],
            'anoReferencia': [anoReferencia]
        })

        # Prever o preço
        predicted_price = model.predict(features)[0]

        return JsonResponse({'predicted_price': predicted_price})

    return JsonResponse({'error': 'Método POST requerido'}, status=400)
