nilai_data = {}

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

def input_data(nim=None):
    nim = nim or input("NIM: ")
    nama = input("Nama: ")
    tugas, uts, uas = (float(input(f"Nilai {y}: ")) for y in ["Tugas", "UTS", "UAS"])
    nilai_data[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "nilai_akhir": (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)}
    print("Data berhasil disimpan!")

def hapus_data():
    if not nilai_data: return print("Belum ada data.")
    nim = input("Masukkan NIM data yang ingin dihapus: ")
    if nim in nilai_data:
        del nilai_data[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")
    tampilkan_data()

def cari_data():
    if not nilai_data: return print("Belum ada data.")
    keyword = input("Masukkan nama atau NIM yang ingin dicari: ").lower()
    hasil = {nim: d for nim, d in nilai_data.items() if keyword in nim.lower() or keyword in d['nama'].lower()}
    tampilkan_data(hasil) if hasil else print("Data tidak ditemukan.")

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
