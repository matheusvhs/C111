import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('bi.csv')

# Define the bins (intervals of 10 from 0 to 100)
bins = list(range(0, 101, 10))

# Create the histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Python'], bins=bins, kde=False, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Distribuição das Notas de Python', fontsize=16)
plt.xlabel('Nota de Python', fontsize=12)
plt.ylabel('Frequência (Contagem)', fontsize=12)

# Ensure x-axis ticks align with bins
plt.xticks(bins, rotation=45)

# Add grid for better reading
plt.grid(axis='y', alpha=0.75)

# Save the figure
plot_filename = 'histograma_python.png'
plt.savefig(plot_filename)
plt.close()