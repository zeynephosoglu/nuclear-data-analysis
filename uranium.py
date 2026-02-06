import matplotlib.pyplot as plt
import seaborn as sns
#veri setimiz (ton cinsinden rezervler)
ulkeler = ['Avustralya', 'Kazakistan', 'Kanada', 'Rusya', 'Namibya']
rezervler = [1687000,815000, 588000, 480000, 470000]
#görsel stil ayarları
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10,6))
#grafik oluşturma
palette="YlOrRd" #renk paleti
uran_plot = sns.barplot(x=ulkeler, y=rezervler, palette=palette, legend=False)
# Başlıklar
plt.title('Dünya Uranyum Rezervleri (Ton)', fontsize=15, color='darkred')
plt.ylabel('Rezerv Miktarı (Ton)')
plt.xlabel('Ülkeler')

# Değerleri çubukların üzerine ekleyelim
uran_plot.bar_label(uran_plot.containers[0], padding=3)

# Kaydet ve Göster
plt.tight_layout()
plt.savefig('uranyum_rezerv_analizi.png')
plt.show()