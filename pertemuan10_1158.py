import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# as = mengubah library menjadi object
# dokumentasi
data = {'Mahasiswa': ['Aldi', 'Bagus', 'Bedul', 'Dwi', 'Endo'],
        'nilai': [20, 50, 40, 85, 90],}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))  # Atur ukuran gambar 
sns.barplot(x='Mahasiswa', y='nilai', data=data,color="purple")
plt.title('Grafik Data')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai')
plt.show()


plt.figure(figsize=(10, 6))  # Atur ukuran gambar
plt.pie(df["nilai"],labels=df["Mahasiswa"],autopct="%1.1f%%") 
plt.title('Grafik Data')
plt.show()