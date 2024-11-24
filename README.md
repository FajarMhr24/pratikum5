# Praktikum 5 - Dictionary

NAMA : FAJAR MAHER HABIBILLAH

NIM : 312410549

KELAS : TI.24.A5

## penjelasan alur kode program

### 1. Variable  global
```python
nilai_data = {}
```
`nilai_data` adalah dictionary kosong yang digunakan untuk menyimpan data mahasiswa.

### 2. Fungsi tampilkan_data

```python
def tampilkan_data(data=None):
    data = data or nilai_data
    if not data:
        print("=" * 64)
        print("No | Nama\t| NIM  | Tugas | UTS | UAS |  Nilai Akhir      |")
        print("=" * 64)
        print("   |                      Belum ada data                       |")
        print("=" * 64)
        return
    print("No | Nama\t|    NIM   | Tugas | UTS | UAS |  Nilai Akhir |")
    print("=" * 63)
    for i, (nim, d) in enumerate(data.items(), 1):
        print(f"{i}  | {d['nama']}\t| {nim}   | {d['tugas']}  | {d['uts']}| {d['uas']}| {d['nilai_akhir']:.2f}        |")
    print("=" * 63)
```
jika data kosong akan menampilan tabel yang berisi "belum ada data"

jika data terisi akan menampilkan

No: Nomor urut.

Nama: Nama mahasiswa.

NIM: Nomor Induk Mahasiswa.

Tugas, UTS, UAS: Nilai tugas, UTS, dan UAS.

Nilai Akhir: Nilai rata-rata yang dihitung dengan rumus:

nilai_akhir = (tugas x 0.3) + (uts x 0.35) + (uas x 0.3)

### 3. Fungsi input_data

```python
def input_data(nim=None):
    nim = nim or input("NIM: ")
    nama = input("Nama: ")
    tugas, uts, uas = (float(input(f"Nilai {y}: ")) for y in ["Tugas", "UTS", "UAS"])
    nilai_data[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "nilai_akhir": (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)}
    print("Data berhasil disimpan!")
```
Menambahkan atau memperbarui data mahasiswa.

### 4.  Fungsi hhapus_data
```python
def hapus_data():
    if not nilai_data: return print("Belum ada data.")
    nim = input("Masukkan NIM data yang ingin dihapus: ")
    if nim in nilai_data:
        del nilai_data[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")
    tampilkan_data()
```
Menghapus data mahasiswa berdasarkan NIM.

### 5. Fungsi cari_data
```python
def cari_data():
    if not nilai_data: return print("Belum ada data.")
    keyword = input("Masukkan nama atau NIM yang ingin dicari: ").lower()
    hasil = {nim: d for nim, d in nilai_data.items() if keyword in nim.lower() or keyword in d['nama'].lower()}
    tampilkan_data(hasil) if hasil else print("Data tidak ditemukan.")
```
Mencari data berdasarkan NIM atau nama.

### 6. Menu utama
```python
while True:
    print("\n|Program Input Nilai|")
    print("[(L)Lihat, (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (K)Keluar]")
    pilihan = input("Menu: ").lower()

    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        input_data()
    elif pilihan == 'u':
        nim = input("Masukkan NIM data yang ingin diubah: ")
        if nim in nilai_data:
            input_data(nim)
        else:
            print("Data tidak ditemukan.")
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")
```
Menyediakan menu interaktif untuk mengakses fungsi program.

Loop: Program terus berjalan hingga pengguna memilih `k` untuk keluar.

## flowchart
![foto](https://github.com/FajarMhr24/flochart/blob/9e504339bd79a73cc21b47f625746d38151300fa/Screenshot%202024-11-24%20145521.png)

## Output
![foto](https://github.com/FajarMhr24/foto/blob/50d981b35a6b523003c86018e6d044cea29b22e5/Screenshot%202024-11-24%20164109.png)

![foto](https://github.com/FajarMhr24/foto/blob/50d981b35a6b523003c86018e6d044cea29b22e5/Screenshot%202024-11-24%20164125.png)

![foto](https://github.com/FajarMhr24/foto/blob/50d981b35a6b523003c86018e6d044cea29b22e5/Screenshot%202024-11-24%20164136.png)

![foto](https://github.com/FajarMhr24/foto/blob/50d981b35a6b523003c86018e6d044cea29b22e5/Screenshot%202024-11-24%20164150.png)

![foto](https://github.com/FajarMhr24/foto/blob/50d981b35a6b523003c86018e6d044cea29b22e5/Screenshot%202024-11-24%20164257.png)
