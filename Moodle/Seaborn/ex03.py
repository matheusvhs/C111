import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('bi(2).csv')

# Define a ordem lógica dos níveis educacionais
education_order = ['High School', 'Diploma', 'Bachelor', 'Master', 'Doctorate']

# Filtra a ordem para incluir apenas níveis presentes nos dados
education_levels = [level for level in education_order if level in df['prevEducation'].unique()]

# Cria o boxplot
plt.figure(figsize=(12, 7))
sns.boxplot(x='prevEducation', y='Python', data=df, order=education_levels, palette='Pastel1')

# Adiciona título e rótulos
plt.title('Distribuição das Notas de Python por Nível de Educação Anterior', fontsize=16)
plt.xlabel('Nível de Educação Anterior', fontsize=12)
plt.ylabel('Nota de Python', fontsize=12)

# Rotação dos rótulos do eixo X
plt.xticks(rotation=30, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Salva a figura
plot_filename = 'boxplot_python_by_education.png'
plt.savefig(plot_filename, bbox_inches='tight')
plt.close()