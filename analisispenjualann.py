import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Load data
df = pd.read_csv('data_penjualan.csv')

# Bersihkan nama kolom (biar aman)
df.columns = df.columns.str.strip()

print(df.head())
print(df.info())
print(df.isnull().sum())

# ======================
# DATA CLEANING
# ======================

# Hapus harga negatif
df = df[df['Price_Per_Unit'] > 0]

# Ubah ke datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# ======================
# TREN PENJUALAN BULANAN
# ======================

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()

# ======================
# HEATMAP KORELASI
# ======================

correlation = df[['Total_Sales', 'Ad_Budget', 'Price_Per_Unit']].corr()

sns.heatmap(correlation, annot=True)
plt.title('Korelasi Data')
plt.show()

# ======================
# PRODUK UNDERPERFORMER
# ======================

avg_price = df['Price_Per_Unit'].mean()

underperform = df[df['Price_Per_Unit'] > avg_price]

plt.scatter(underperform['Price_Per_Unit'], underperform['Quantity'])
plt.xlabel('Price_Per_Unit')
plt.ylabel('Quantity')
plt.title('Produk Mahal tapi Jarang Laku')
plt.show()

# ======================
# RFM ANALYSIS
# ======================

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print(rfm.head())

# ======================
# EFISIENSI KATEGORI
# ======================

kategori = df.groupby('Product_Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
})

kategori['Efisiensi'] = kategori['Total_Sales'] / kategori['Ad_Budget']

kategori = kategori.sort_values(by='Efisiensi')

kategori.plot(kind='barh')
plt.title('Efisiensi Kategori')
plt.show()

# ======================
# UJI HIPOTESIS IKLAN
# ======================

median_ads = df['Ad_Budget'].median()

high_ads = df[df['Ad_Budget'] > median_ads]
low_ads = df[df['Ad_Budget'] <= median_ads]

print("Rata-rata penjualan iklan tinggi:", high_ads['Total_Sales'].mean())
print("Rata-rata penjualan iklan rendah:", low_ads['Total_Sales'].mean())