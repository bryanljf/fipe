from django.shortcuts import render
from app.services import dataLoader

def home(request): 
    if request.method == "POST":
        selected_brand = request.POST.get('brand', '')  
        all_brands = dataLoader.loadBrands()  
        return render(request, 'home.html', {'marcas': all_brands, 'selected_brand': selected_brand})
     
    else:    
        all_brands = dataLoader.loadBrands()
        return render(request, 'home.html', {'marcas': all_brands})
