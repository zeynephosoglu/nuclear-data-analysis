import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Nuclear reactors by country (Approximate current data)
countries = ['ABD', 'Fransa', 'Çin', 'Rusya', 'Güney Kore', 'Hindistan', 'Kanada']
reactors = [94, 56, 56, 37, 26, 23, 19]

# Set style
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=reactors, y=countries, hue=countries, palette="viridis", legend=False)

# Add titles and labels
plt.title('Ülkelere Göre Operasyonel Nükleer Reaktör Sayısı', fontsize=16, fontweight='bold')
plt.xlabel('Reaktör Sayısı', fontsize=12)
plt.ylabel('Ülke', fontsize=12)

# Save the plot
plt.tight_layout()
plt.savefig('nukleer_grafik.png')