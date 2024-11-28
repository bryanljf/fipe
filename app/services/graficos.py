import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

# Gráfico de pizza para faixas de preços, % de carros por valor
def pizza_precos(dataset):
    plt.figure()
    # Definindo as faixas de preço manualmente
    faixas = [1000, 10000, 50000, 100000, 200000, 500000, 1000000]  # Ajuste as faixas conforme necessário
    labels = [f'Carros de {faixas[i]}Reais até {faixas[i+1]}Reais' for i in range(len(faixas) - 1)]  # Gera rótulos das faixas

    # Criando categorias com base nas faixas de preço
    categorias = pd.cut(dataset['preco_medio_FIPE'], bins=faixas, labels=labels, include_lowest=True)

    # Contagem de ocorrências em cada faixa
    proporcoes = categorias.value_counts().sort_index()  # Ordena para exibir na ordem das faixas

    # Gerar o gráfico de pizza
    proporcoes.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='viridis')  # Colormap para cores automáticas
    plt.title('Distribuição de Preços por Faixas')
    plt.ylabel('')  # Remove o rótulo do eixo Y
    
    return salvar_grafico_em_base64()

# Gráfico de Distribuição de Preço por Marca
def distribuicao_preco_por_marca(dataset):
    plt.figure(figsize=(10, 6))
    avg_price_by_brand = dataset.groupby('marca')['preco_medio_FIPE'].mean().sort_values(ascending=False)
    avg_price_by_brand.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribuição de Preço Médio por Marca')
    plt.xlabel('Marca')
    plt.ylabel('Preço Médio (BRL)')
    plt.xticks(rotation=90)  # Rotaciona os nomes das marcas para ficar legível
    
    return salvar_grafico_em_base64()

# Gráfico de Distribuição de Preço por Ano
def distribuicao_preco_por_ano(dataset):
    plt.figure(figsize=(10, 6))
    avg_price_by_year = dataset.groupby('year_model')['preco_medio_FIPE'].mean()
    avg_price_by_year.plot(kind='line', color='orange', marker='o')
    plt.title('Distribuição de Preço Médio por Ano do Modelo')
    plt.xlabel('Ano do Modelo')
    plt.ylabel('Preço Médio (BRL)')
    
    return salvar_grafico_em_base64()

# Gráfico de Distribuição de Preço por Combustível
def distribuicao_preco_por_combustivel(dataset):
    plt.figure(figsize=(10, 6))
    avg_price_by_fuel = dataset.groupby('combustivel')['preco_medio_FIPE'].mean()
    avg_price_by_fuel.plot(kind='bar', color='lightcoral', edgecolor='black')
    plt.title('Distribuição de Preço Médio por Tipo de Combustível')
    plt.xlabel('Tipo de Combustível')
    plt.ylabel('Preço Médio (BRL)')
    plt.xticks(rotation=0)  # Deixa os rótulos legíveis
    
    return salvar_grafico_em_base64()

# Gráfico de Distribuição de Preço por Câmbio (Manual/Automático)
def distribuicao_preco_por_cambio(dataset):
    plt.figure(figsize=(10, 6))
    avg_price_by_gear = dataset.groupby('cambio')['preco_medio_FIPE'].mean()
    avg_price_by_gear.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Distribuição de Preço Médio por Tipo de Câmbio')
    plt.xlabel('Tipo de Câmbio')
    plt.ylabel('Preço Médio (BRL)')
    plt.xticks(rotation=0)  # Deixa os rótulos legíveis
    
    return salvar_grafico_em_base64()

# Função para salvar o gráfico gerado em Base64
def salvar_grafico_em_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return 'data:image/png;base64,' + string
