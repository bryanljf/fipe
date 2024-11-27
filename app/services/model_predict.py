from django.http import JsonResponse
import joblib
import pandas as pd

def predictPrice(request):
    if request.method == 'POST':
        model = joblib.load('../static/media/model_fipe.pkl')
        le = joblib.load('../static/media/label_encoder.pkl')
        data = request.POST

        marca = data['marca']
        modelo = data['modelo']
        anoModelo = int(data['anoModelo'])
        anoReferencia = int(data['anoReferencia'])

        # Transformar a marca usando o Label Encoder
        marca_ = le.transform([marca])[0]
        modelo_ = le.transform([modelo])[0]

        # Criar o dataframe com os dados recebidos
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
