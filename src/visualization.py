import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

def visualize_clusters(data, worst_bomb_coordinates, worst_survival_rate, bomb_strength):
    # Visualiza os clusters e as taxas de sobrevivência
    _figure, axis = plt.subplots(figsize=(12, 8))
    scatter_plot = axis.scatter(
        data['latitude'], 
        data['longitude'], 
        c=data['cluster'], 
        cmap='tab10', 
        s=data['survival_rate'] * 10, 
        alpha=0.6, 
        edgecolors='w', 
        linewidth=0.5
    )
    
    # Adicionar a legenda dos clusters
    legend1 = axis.legend(*scatter_plot.legend_elements(), title="Clusters")
    axis.add_artist(legend1)
    
    # Adicionar rótulos aos pontos
    for index in range(len(data)):
        axis.text(
            data['latitude'][index], 
            data['longitude'][index], 
            f"{data['name'][index]} ({data['survival_rate'][index]:.2f})", 
            fontsize=9, 
            ha='right'
        )
    
    # Adicionar a pior bomba
    plt.scatter(
        *worst_bomb_coordinates, 
        color='red', 
        s=200, 
        marker='x', 
        label=f'Pior Bomba ({worst_survival_rate:.2f})'
    )
    
    # Melhorar a legenda
    plt.legend(loc='upper right')
    
    # Adicionar barra de cores
    plt.colorbar(scatter_plot, label='Cluster')
    
    # Adicionar rótulos de eixos
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    
    # Adicionar título e subtítulo
    plt.title(
        f'Agrupamento de Taxa de Sobrevivência\n'
        f'Info Bomba: {worst_bomb_coordinates} ({worst_survival_rate:.2f})\n'
        f'Força da Bomba: {bomb_strength:.2f} megatons'
    )
    
    # Adicionar grade
    plt.grid(True)
    
    # Adicionar texto explicativo
    plt.figtext(0.5, 0.01, "As porcentagens são baseadas na pior bomba", ha="center", fontsize=10)
    
    # Mostrar o gráfico
    plt.show()

def evaluate_clustering(data, labels):
    # Avalia o agrupamento usando a pontuação de silhueta
    silhouette_average = silhouette_score(data[['latitude', 'longitude', 'altitude', 'buildings']], labels)
    print(f'Pontuação de Silhueta: {silhouette_average:.2f}')
    return silhouette_average