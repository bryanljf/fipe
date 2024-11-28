from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from app.apps import DATASET
from app.services import model_predict

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
        
        return render(request, 'home.html', {
            'marcas': all_brands, 
            'selected_brand': selected_brand,
            'selected_model': selected_model,
            'anos': years,
            'predict_key': predict_key,
            'predicted_price': predicted_price
            })
    else:   
        predict_key = 0
        predicted_price = 0
        return render(request, 'home.html', {
            'marcas': all_brands,
            'anos': years,
            'predict_key': predict_key,
            'predicted_price': predicted_price
            })
    
def get_models(request):
    # Rota para retornar os modelos baseado na marca
    selected_brand = request.GET.get('marca', '')
    if selected_brand:
        all_models = DATASET.loc[DATASET['marca'] == selected_brand, 'modelo'].unique().tolist()
    else:
        all_models = []

    return JsonResponse({'modelos': all_models})
