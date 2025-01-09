import matplotlib.pyplot as plt

def visualize_rules(rules):
    # Visualiza as regras de associação
    plt.figure(figsize=(100, 66))
    
    # Scatter plot com cores baseadas na lift
    scatter = plt.scatter(rules['support'], rules['confidence'], c=rules['lift'], cmap='viridis', alpha=0.5)
    
    # Adiciona título e rótulos aos eixos
    plt.title('Regras de Associação')
    plt.xlabel('Suporte (frequencia)')
    plt.ylabel('Confiança (probabilidade)')
    
    # Adiciona uma grade
    plt.grid(True)
    
    # Adiciona uma barra de cores
    cbar = plt.colorbar(scatter)
    cbar.set_label('Lift')
    
    # Adiciona legendas
    for i, rule in rules.iterrows():
        plt.annotate(f"{rule['antecedents']} -> {rule['consequents']}", 
                     (rule['support'], rule['confidence']), 
                     textcoords="offset points", 
                     xytext=(0,10), 
                     ha='center', fontsize=8)
    
    # Mostra o gráfico
    plt.show()