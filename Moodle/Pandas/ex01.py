import pandas as pd
import numpy as np

df = pd.read_csv('../../datasets/linguagens.csv', delimiter=',')


ano1 = df['Valor'][0:3].sum()
ano2 = df['Valor'][3:6].sum()


print(teste)


print("Participação das linguagens:")
print(f"Ano 1: {ano1:.2f}")
print(f"Ano 2: {ano2:.2f}")