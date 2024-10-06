import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data_absen.xlsx')
print(df.head(5))

df['Persentase Kehadiran'] = df['Hadir'].mean() * 100

rata_rata_jurusan = df.groupby('Jurusan')['Persentase Kehadiran'].mean()
print(rata_rata_jurusan)

rata_rata_jurusan.to_excel('hasil_absen.xlsx')

rata_rata_jurusan.plot(kind='bar')
plt.title('Persentase Kehadiran Berdasarkan Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Persentase Kehadiran (%)')
plt.show()

