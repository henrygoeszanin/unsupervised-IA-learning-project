import random
import numpy as np
from data_processing import load_data, generate_random_data, train_model, predict_survival_rate, apply_clustering
from visualization import visualize_clusters, evaluate_clustering

def main():
    print("Projeto iniciado")
    
    # Passo 1: Gerar novos dados aleatórios
    generate_random_data('./data/random_data.csv')
    
    # Passo 2: Carregar dados de treinamento
    training_data = load_data('./data/parameters.csv')
    
    # Adicionar coluna de força da bomba aos dados de treinamento
    training_data['bomb_strength'] = np.random.uniform(1, 10, len(training_data))  # Exemplo: força da bomba entre 1 e 10 megatons
    
    # Passo 3: Treinar modelo
    survival_rate_model = train_model(training_data)
    
    # Passo 4: Carregar dados do experimento
    experiment_data = load_data('./data/random_data.csv')
    
    # Passo 5: Prever taxas de sobrevivência para os dados do experimento
    initial_bomb_coords = (0, 0)  # Coordenadas fictícias para cálculo inicial
    initial_bomb_strength = 1  # Força fictícia para cálculo inicial
    experiment_data = predict_survival_rate(survival_rate_model, experiment_data, initial_bomb_coords, initial_bomb_strength)
    
    # Passo 6: Aplicar agrupamento
    clustered_data, clustering_model = apply_clustering(experiment_data)
    
    # Passo 7: Prever taxas de sobrevivência para diferentes coordenadas de bombas
    random.seed(30)  # Garantir reprodutibilidade
    worst_survival_rate = float('inf')
    worst_bomb_coords = (0, 0)
    worst_bomb_strength = 0
    print("Calculando taxas de sobrevivência para diferentes coordenadas de bombas:")
    for i in range(500):  # Gerar 500 coordenadas de bombas aleatórias
        random_bomb_coords = (
            np.random.uniform(experiment_data['latitude'].min(), experiment_data['latitude'].max()), 
            np.random.uniform(experiment_data['longitude'].min(), experiment_data['longitude'].max())
        )
        random_bomb_strength = np.random.uniform(1, 10)  # Exemplo: força da bomba entre 1 e 10 megatons
        clustered_data = predict_survival_rate(survival_rate_model, clustered_data, random_bomb_coords, random_bomb_strength)
        average_survival_rate = clustered_data['survival_rate'].mean()
        print(f"{i+1}. Bomba em {random_bomb_coords} com força {random_bomb_strength:.2f} megatons -> Taxa de Sobrevivência: {average_survival_rate:.2f}")
        if average_survival_rate < worst_survival_rate:
            worst_survival_rate = average_survival_rate
            worst_bomb_coords = random_bomb_coords
            worst_bomb_strength = random_bomb_strength
    
    print(f"\nPiores coordenadas de bomba para a menor taxa de sobrevivência: {worst_bomb_coords} com taxa de sobrevivência: {worst_survival_rate:.2f}")
    
    # Visualizar clusters com as coordenadas da pior bomba
    clustered_data = predict_survival_rate(survival_rate_model, clustered_data, worst_bomb_coords, worst_bomb_strength)
    visualize_clusters(clustered_data, worst_bomb_coords, worst_survival_rate, worst_bomb_strength)
    evaluate_clustering(clustered_data, clustered_data['cluster'])
    
    print("Projeto finalizado")

if __name__ == "__main__":
    main()