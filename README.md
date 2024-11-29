# Dashboard Tabela FIPE

## Resumo do Projeto
Projeto de uma aplicação web para um dashboard interativo com dados retirados a partir de um dataset
de valores da Tabela FIPE. Possui funcionalidades como observação dinâmica de diversos gráficos em relação aos
dados do dataset e previsão de preços FIPE feitos com aprendizado de máquina.
Trabalho desenvolvido para a disciplina de "Tópicos Especiais em Software" da Universidade Positivo.

## Tecnologias
Projeto criado com:
* Python versão 3.12.4
* Django versão 5.1.1
* HTML5
* CSS

## Setup
Para rodar o projeto, execute os seguintes passos abaixo:
* No terminal ou prompt de comando, acesse a pasta do projeto
* Execute o seguinte comando para iniciar o servidor local:
```
python manage.py runsserver --noreload
```
* Acesse no navegador, o endereço mostrado no Terminal/Prompt

## Instruções/Funcionalidades
* Para iniciar, é necessário que o arquivo '.csv' do dataset esteja presente na pasta "static/data";
* Caso o localhost não tenha o modelo de aprendizado de máquina salvo, o sistema automaticamente iniciára o treinamento pré-estabelecido do modelo;
* O dashboard contém uma série de gráficos que podem ser observados dinâmicamente, apenas sendo necessário pressionar o botão correspondente;
* Com base nas informações do form é possível gerar uma previsão do valor FIPE do veículo, com base no treinamento do modelo feito anteriormente e a leitura dos dados do dataset base.

