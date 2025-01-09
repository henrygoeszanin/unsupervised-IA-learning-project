import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def load_data(file_path):
    # Carrega os dados a partir de um arquivo CSV
    data = pd.read_csv(file_path)
    return data

def apply_association_rules(data, min_support=0.2, min_threshold=0.5):
    # Cria uma tabela de transações
    basket = data.pivot_table(index='transaction_id', columns='item', aggfunc='size', fill_value=0)
    # Converte os dados para o tipo booleano
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    # Aplica o algoritmo Apriori
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    # Gera regras de associação
    num_itemsets = len(basket)
    rules = association_rules(frequent_itemsets, num_itemsets=num_itemsets, metric="confidence", min_threshold=min_threshold)
    return rules