import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Variável global para o tamanho da área
AREA_RADIUS = 100  # Em quilômetros

def load_data(file_path):
    # Carrega os dados a partir de um arquivo CSV
    data = pd.read_csv(file_path)
    return data

def generate_random_data(file_path, num_samples=1000):
    # Gera novos dados aleatórios e salva no arquivo CSV
    names = [f'P_{i}' for i in range(num_samples)]
    latitudes = np.random.uniform(-AREA_RADIUS, AREA_RADIUS, num_samples)
    longitudes = np.random.uniform(-AREA_RADIUS, AREA_RADIUS, num_samples)
    altitudes = np.random.uniform(-100, 100, num_samples)
    buildings = np.random.randint(0, 200, num_samples)
    
    data = pd.DataFrame({
        'name': names,
        'latitude': latitudes,
        'longitude': longitudes,
        'altitude': altitudes,
        'buildings': buildings
    })
    
    data.to_csv(file_path, index=False)

def train_model(data):
    # Treina um modelo de regressão linear para prever a taxa de sobrevivência
    features = data[['latitude', 'longitude', 'altitude', 'buildings', 'distance_to_bomb', 'bomb_strength']]
    target = data['survival_rate']
    model = LinearRegression()
    model.fit(features, target)
    return model

def predict_survival_rate(model, data, bomb_coordinates, bomb_strength):
    # Calcula a distância até a bomba
    data['distance_to_bomb'] = np.sqrt((data['latitude'] - bomb_coordinates[0])**2 + (data['longitude'] - bomb_coordinates[1])**2)
    # Adiciona a força da bomba
    data['bomb_strength'] = bomb_strength
    # Prediz a taxa de sobrevivência usando o modelo treinado
    features = data[['latitude', 'longitude', 'altitude', 'buildings', 'distance_to_bomb', 'bomb_strength']]
    data['survival_rate'] = model.predict(features)
    return data

def apply_clustering(data, num_clusters=5):
    # Aplica o algoritmo KMeans para agrupar os dados com base na taxa de sobrevivência
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['survival_rate']])
    return data, kmeans