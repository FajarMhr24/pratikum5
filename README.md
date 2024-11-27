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

### 2. Perulangan utama
```python
while True:
    print("\n|Program Input Nilai|")
    print("[(L)Lihat, (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (K)Keluar]")
    pilihan = input("Menu: ").lower()
```
Menu ditampilkan setiap iterasi untuk memberi pengguna opsi seperti melihat, menambah, mengubah, menghapus, mencari data, atau keluar dari program. Input pengguna (`pilihan`) diubah menjadi huruf kecil (.`lower`()) untuk mempermudah perbandingan.

### 3. input L(LIHAT)

```python
if pilihan == 'l':
    if not nilai_data:

```
`not nilai_data`: Mengecek apakah `nilai_data` kosong. Jika iya, tampilkan pesan bahwa belum ada data.
Jika ada data, loop melalui setiap item dalam `nilai_data` untuk ditampilkan dalam tabel, dengan perhitungan nilai akhir (`nilai_akhir`).


### 4. input T(TAMBAH)
```python
elif pilihan == 't':
    nim = input("NIM: ")

```
Meminta pengguna memasukkan NIM sebagai kunci data.

Memasukkan nama dan nilai (tugas, UTS, UAS) sebagai nilai pada dictionary `nilai_data[nim]`.

Nilai akhir dihitung menggunakan rumus:
```python
sum(nilai_data[nim][x] * w for x, w in zip(["tugas", "uts", "uas"], [0.3, 0.35, 0.35]))
```


### 5. input U(UBAH)
```python
elif pilihan == 'u':
    nim = input("Masukkan NIM data yang ingin diubah: ")

```
Meminta pengguna memasukkan NIM data yang akan diubah.

Jika NIM ditemukan, data lama akan digantikan dengan data baru yang dimasukkan pengguna.

Nilai akhir diperbarui menggunakan logika yang sama dengan menambah data.

Jika NIM tidak ditemukan, tampilkan pesan kesalahan.


### 6. input H(HAPUS)
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

### 7. input C(CARI)
```python
elif pilihan == 'c':
    keyword = input("Masukkan nama atau NIM yang ingin dicari: ").lower()
```
Meminta pengguna memasukkan kata kunci (`keyword`) untuk mencari data berdasarkan `NIM` atau `nama`.

hasil adalah dictionary baru yang menyimpan data yang cocok dengan kata kunci.

Meminta pengguna memasukkan NIM data yang akan dihapus.

Jika NIM ditemukan, data dihapus menggunakan `del nilai_data[nim]`.

Jika tidak ditemukan, tampilkan pesan kesalahan.

Menyediakan menu interaktif untuk mengakses fungsi program.

Loop: Program terus berjalan hingga pengguna memilih `k` untuk keluar.

## flowchart
![foto](https://github.com/FajarMhr24/flochart/blob/9e504339bd79a73cc21b47f625746d38151300fa/Screenshot%202024-11-24%20145521.png)

## Output
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-11-24%20164109.png)

![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-11-24%20164125.png)

![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-11-24%20164136.png)

![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-11-24%20164150.png)

![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-11-24%20181158.png)
