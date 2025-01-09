import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
import os

def train_model():
    # Caminho da pasta de dados
    data_folder = 'data'
    
    # Lista para armazenar os DataFrames
    data_frames = []
    
    # Iterar sobre todos os arquivos na pasta de dados
    for file_name in os.listdir(data_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(data_folder, file_name)
            data_frames.append(pd.read_csv(file_path))
    
    # Combinar todos os DataFrames em um único DataFrame
    data = pd.concat(data_frames, ignore_index=True)
    
    # Separar as features e o target
    X = data[['idade', 'salario', 'score_cpf', 'divida_cpf']]
    y = data['credito']
    
    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Criar e treinar o modelo
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Salvar o modelo treinado
    joblib.dump(model, 'model/credit_model.pkl')
    
    print("Modelo treinado e salvo com sucesso.")

if __name__ == "__main__":
    train_model()