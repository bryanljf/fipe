import os
from django.apps import AppConfig
from app.services import data_loader
from app.services import ml_model
from fipe.settings import BASE_DIR

pkl_path = os.path.join(BASE_DIR, 'app', 'static', 'media', 'model_fipe.pkl')

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    # Método para fazer a leitura do dataset e treinamento do modelo ML logo ao iniciar o servidor
    def ready(self):
        print("Fazendo a leitura do dataset [...]")
        try:
            global DATASET
            DATASET = data_loader.load_data()
            print("Dataset carregado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao fazer a leitura do dataset: {e}")
            return
        
        if os.path.exists(pkl_path):
            print(f"O modelo já existe em {pkl_path}. Não será necessário realizar o treinamento")
            return  # O arquivo existe, então não faz o treinamento
        else:
            print("O modelo não existe, portanto o treinamento será realizado")

        print("Modelo de Machine Learning em treinamento [...]")
        try:
            ml_model.train_model(DATASET)
            print("Treinamento do modelo realizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao fazer o treinamento do modelo: {e}")
            return
