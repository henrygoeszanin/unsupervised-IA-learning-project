import csv
import random
from datetime import datetime

# Função para gerar dados
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        idade = random.randint(18, 90)  # Idades entre 18 e 90
        salario = int((idade - 18) / (90 - 18) * (30000 - 1000) + 1000)  # Salário proporcional à idade
        score_cpf = random.randint(300, 900)  # Score CPF entre 300 e 900
        
        # Ajustar a dívida com base na idade e no salário
        if idade > 60 and salario < 15000:
            divida_cpf = random.randint(10000, 20000)  # Dívida maior para idade avançada e salário baixo
        else:
            divida_cpf = random.randint(0, 10000)  # Dívida menor para outras condições
        
        credito = int((idade - 18) / (90 - 18) * (20000 - 0) + 0)  # Crédito proporcional à idade
        data.append([idade, salario, score_cpf, divida_cpf, credito])
    return data

# Função para escrever dados no CSV
def write_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['idade', 'salario', 'score_cpf', 'divida_cpf', 'credito'])
        writer.writerows(data)

# Caminho do arquivo CSV com timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
file_path = f'./data/training_data_{timestamp}.csv'

# Definir o número de registros a serem gerados
num_records = 5000000  # Por exemplo, 100 registros

# Gerar novos dados
new_data = generate_data(num_records)

# Escrever novos dados no CSV
write_csv(file_path, new_data)

print(f"Novos dados gerados e salvos no CSV: {file_path}")