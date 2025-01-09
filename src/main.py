from data_processing import load_data, apply_association_rules
from visualization import visualize_rules

def main():
    print("Projeto iniciado")
    
    # Carregar dados de cestas de mercado
    market_data = load_data('./data/market_basket.csv')
    
    # Aplicar regras de associação
    rules = apply_association_rules(market_data)
    
    # Visualizar regras
    visualize_rules(rules)
    
    print("Projeto finalizado")

if __name__ == "__main__":
    main()