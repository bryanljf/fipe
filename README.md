
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

------------------------------------------------------------------------------------------------------------
Bryan:

>>PRECISA SALVAR O .csv DENTRO DA PASTA STATIC/DATA PQ NÃO TEM COMO COMMITAR JUNTO NO GIT
>>NÃO ESQUECE DE EXCLUIR O CSV E O .PKL DA PASTA STATIC/MEDIA ANTES DO COMMIT PQ SÃO PESADOS E DÃO B.O NO GIT
>>O .PKL É GERADO TODA VEZ QUE O SERVIDOR RODA (PODE SER DESATIVADO NO APPS.PY -> ready())

POST do html já está funcionando e retornando um preço previsto(bem errado >>PRECISA AJUSTAR A PREVISÃO DO ML<<)

. apps.py -> ready() faz com que o dataset seja carregado e o modelo treinado logo quando o servidor é iniciado (Modelo demora um pouco se quiser que pare por momento comenta o código que chama o treinamento)

.HTML -> Por mais que esteja funcional, quando volta para a tela, apenas a marca que foi selecionada antes está ficando gravada, provavelmente precisa ajustar alguma coisa ali do script de js para ele não voltar para "Selecionar Modeo" e fazer a gravação das outras infos: combustivel,cambio e ano

.ML -> Já está lendo as colunas convertidas em números, ao fazer o POST do html já é feito uma conversão das strings de marca e modelo (e as outras info tbm) para numeral

-Basicamente precisa deixar o modelo mais preciso para treinamento (talvez fazer algo mais parecido com oq ta la no projeto do dataset no kaggle), fazer a parte dos gráficos(não precisa mexer no ML nessa parte), fazer o front e dar uma ajeitada melhor ae

qualquer duvida sobre o meu codigo pode me chamar no zap



