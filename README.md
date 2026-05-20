# 📊 Analisis Penjualan — Sales Analysis Project

Proyek ini melakukan analisis data penjualan menggunakan Python, mencakup tren bulanan, korelasi variabel, segmentasi pelanggan (RFM), serta efisiensi iklan per kategori produk.

---

## 📁 Struktur File

```
├── data_penjualan.csv       # Dataset utama penjualan
└── analisispenjualann.py    # Script analisis utama
```

---

## 🗃️ Dataset

File: `data_penjualan.csv`  
Jumlah baris: ~150 transaksi

| Kolom             | Tipe      | Keterangan                          |
|-------------------|-----------|-------------------------------------|
| `Order_ID`        | Integer   | ID unik per transaksi               |
| `CustomerID`      | Integer   | ID pelanggan                        |
| `Order_Date`      | Date      | Tanggal pemesanan                   |
| `Product_Category`| String    | Kategori produk (Books, Fashion, Electronics, Gadget, Home Decor) |
| `Quantity`        | Integer   | Jumlah unit yang dibeli             |
| `Price_Per_Unit`  | Float     | Harga per unit (Rupiah)             |
| `Ad_Budget`       | Float     | Anggaran iklan per transaksi        |
| `Total_Sales`     | Float     | Total penjualan (bisa kosong/null)  |

---

## ⚙️ Requirements

Pastikan sudah menginstall dependensi berikut:

```bash
pip install pandas matplotlib seaborn
```

Atau install sekaligus via:

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:
```
pandas
matplotlib
seaborn
```

---

## 🚀 Cara Menjalankan

```bash
python analisispenjualann.py
```

---

## 🔍 Analisis yang Dilakukan

### 1. Data Cleaning
- Menghapus baris dengan `Price_Per_Unit` negatif
- Konversi kolom `Order_Date` ke format datetime

### 2. Tren Penjualan Bulanan
Visualisasi line chart total `Total_Sales` per bulan sepanjang 2023 untuk melihat pola naik-turun penjualan.

### 3. Heatmap Korelasi
Menampilkan korelasi antar variabel numerik: `Total_Sales`, `Ad_Budget`, dan `Price_Per_Unit` menggunakan heatmap seaborn.

### 4. Produk Underperformer
Scatter plot untuk mengidentifikasi produk dengan harga di atas rata-rata namun volume penjualan (quantity) rendah — kandidat produk yang perlu dievaluasi.

### 5. RFM Analysis
Segmentasi pelanggan berdasarkan tiga dimensi:
- **Recency** — seberapa baru pelanggan melakukan transaksi
- **Frequency** — seberapa sering pelanggan bertransaksi
- **Monetary** — total nilai belanja pelanggan

### 6. Efisiensi Kategori
Mengukur efisiensi anggaran iklan per kategori produk dengan formula:

```
Efisiensi = Total_Sales / Ad_Budget
```

Kategori dengan nilai efisiensi tinggi menghasilkan penjualan lebih besar per rupiah iklan.

### 7. Uji Hipotesis Iklan
Membandingkan rata-rata `Total_Sales` antara transaksi dengan anggaran iklan tinggi (di atas median) vs rendah (di bawah/sama dengan median) untuk menguji apakah iklan berpengaruh signifikan terhadap penjualan.
