import pandas as pd

data = pd.read_csv('data.csv')
print("Data asli:")
print(data)
data_cleaned = data.dropna()
data_cleaned.to_csv('data_cleaned.csv', index=False)
print("Data berhasil dibersihkan dan disimpan ke 'data_cleaned.csv'.")
