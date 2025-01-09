import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd

def predict_credit():
    try:
        idade = int(entry_idade.get())
        salario = float(entry_salario.get())
        score_cpf = int(entry_score_cpf.get())
        divida_cpf = float(entry_divida_cpf.get())
        
        # Carregar o modelo treinado
        model = joblib.load('model/credit_model.pkl')
        
        # Criar o DataFrame com os dados de entrada
        input_data = pd.DataFrame([[idade, salario, score_cpf, divida_cpf]], columns=['idade', 'salario', 'score_cpf', 'divida_cpf'])
        
        # Fazer a previsão
        predicted_credit = model.predict(input_data)[0]
        
        # Exibir o resultado
        messagebox.showinfo("Resultado", f"Crédito previsto: {predicted_credit:.2f}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def start_app():
    # Configurar a interface gráfica
    root = tk.Tk()
    root.title("Análise de Crédito")

    tk.Label(root, text="Idade:").grid(row=0)
    tk.Label(root, text="Salário:").grid(row=1)
    tk.Label(root, text="Score CPF:").grid(row=2)
    tk.Label(root, text="Dívida CPF:").grid(row=3)

    global entry_idade, entry_salario, entry_score_cpf, entry_divida_cpf
    entry_idade = tk.Entry(root)
    entry_salario = tk.Entry(root)
    entry_score_cpf = tk.Entry(root)
    entry_divida_cpf = tk.Entry(root)

    entry_idade.grid(row=0, column=1)
    entry_salario.grid(row=1, column=1)
    entry_score_cpf.grid(row=2, column=1)
    entry_divida_cpf.grid(row=3, column=1)

    tk.Button(root, text="Prever Crédito", command=predict_credit).grid(row=4, column=1)

    root.mainloop()