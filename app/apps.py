from django.apps import AppConfig
from app.services import data_loader
from app.services import ml_model


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
        
        print("Modelo de Machine Learning em treinamento [...]")
        try:
            ml_model.trainModel(DATASET)
            print("Treinamento do modelo realizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao fazer o treinamendo do modelo: {e}")
            return


