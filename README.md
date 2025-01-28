# Projeto Simples de Machine Learning

Este projeto implementa uma abordagem de aprendizado não supervisionado usando um conjunto de dados com várias características. O objetivo principal é analisar os dados, aplicar algoritmos de agrupamento e interpretar os resultados.

## Estrutura do Projeto

```
simple-ml-project
├── data
│   ├── clustered_data.csv    # Dados agrupados gerados pelo projeto
│   └── random_data.csv       # Dados aleatórios gerados para experimentos
├── src
│   ├── data_processing.py    # Funções para carregar, gerar e processar dados
│   ├── main.py               # Script principal para executar o projeto
│   ├── visualization.py      # Funções para visualizar os resultados
│   └── __init__.py           # Marca o diretório src como um pacote Python
├── requirements.txt          # Lista as bibliotecas Python necessárias
└── README.md                 # Documentação do projeto
```

## Instalação

Para configurar o projeto, clone o repositório e instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Uso

1. **Gerar Dados Aleatórios**: Execute `main.py` para gerar dados aleatórios e treinar o modelo.
2. **Treinar Modelo**: O modelo é treinado usando os dados de `parameters.csv`.
3. **Prever Taxas de Sobrevivência**: O script irá prever as taxas de sobrevivência para diferentes coordenadas e forças de bombas.
4. **Visualizar Clusters**: Os resultados serão visualizados, mostrando os clusters e as taxas de sobrevivência.

## Participantes

- Henry Goes Zanin
- Mateus Redivo
- Isaac Machado
