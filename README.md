
O dataframe esta mapeado da seguinte forma:

ano_de_referencia - numerico
mes_de_referencia - numerico
marca             - categorico
marca_code        - numerico
modelo            - categorico
modelo_code       - numerico
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

----------------------------------------------------------------------------------------------------------
na criaçao de funçoes se possivel padronizar no modelo de escrita de funçoes do python(snake_case), exemplo:
def nova_funcao()
e para variaveis:
variavel_nova = 0

------------------------------------------------------------------------------------------------------------
tambem comentar a funcionalidade de cada funçao e variavel para facilitar a leitura do codigo
caso necessario tambem comentar a linha se ela nao for clara


