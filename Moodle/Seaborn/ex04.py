import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('bi(3).csv')

# Select the numeric columns
numeric_cols = ['Age', 'entryEXAM', 'studyHOURS', 'Python', 'DB']
corr_df = df[numeric_cols]

# Calculate the correlation matrix
correlation_matrix = corr_df.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix,
            annot=True,       # Show correlation values on the heatmap
            fmt=".2f",        # Format to two decimal places
            cmap='coolwarm',  # Color map (coolwarm is good for showing positive/negative)
            linewidths=.5,    # Lines between cells
            linecolor='black',
            cbar_kws={'label': 'Coeficiente de Correlação de Pearson'})

# Add title
plt.title('Matriz de Correlação das Variáveis Numéricas', fontsize=16)

# Rotate labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Save the figure
plot_filename = 'heatmap_correlation_matrix.png'
plt.savefig(plot_filename, bbox_inches='tight')
plt.close()