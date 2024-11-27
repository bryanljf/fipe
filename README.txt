
O dataframe esta mapeado da seguinte forma:

ano_de_referencia - numerico
mes_de_referencia - numerico
marca             - categorico
marca_code        - numerico
modelo            - numerico -----------------necessario rever --------
combustivel       - categorico
combustivel_code  - numerico
cambio            - categorico
cambio_code       - numerico
potencia_do_motor - numerico
ano_modelo        - numerico
preco_medio_FIPE  - numerico
idade_veiculo     - numerico

os categoricos estao em string e os numericos em seu respectivo tipo e a função load_data() em services/dataLoader.py
ja retorna o dataframe formatado, para uso em modelos de machine learning utilizar somente dados numericos deixando de
fora os dados categoricos que serao utilizados para analise exploratoria



