import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('bi(1).csv')

# Calculate the correlation coefficient
correlation = df['studyHOURS'].corr(df['entryEXAM'])

# Create the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='studyHOURS', y='entryEXAM', hue='gender', data=df, s=100, alpha=0.7)

# Add title and labels
plt.title('Horas de Estudo vs. Nota do Exame de Entrada', fontsize=14)
plt.xlabel('Horas de Estudo (studyHOURS)', fontsize=12)
plt.ylabel('Nota do Exame de Entrada (entryEXAM)', fontsize=12)
plt.legend(title='Gênero')
plt.grid(True, linestyle='--', alpha=0.6)

# Save the figure
plot_filename = 'scatterplot_studyHOURS_entryEXAM_concise.png'
plt.savefig(plot_filename)
plt.close()