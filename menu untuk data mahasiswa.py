nilai_data = {}

while True:
    print("\n|Program Input Nilai|")
    print("[(L)Lihat, (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (K)Keluar]")
    pilihan = input("Menu: ").lower()

    if pilihan == 'l':
        if not nilai_data:
            print("=" * 64, "\nNo | Nama\t| NIM  | Tugas | UTS | UAS |  Nilai Akhir      |")
            print("=" * 64, "\n   |                      Belum ada data                       |")
        else:
            print("No | Nama\t|    NIM   | Tugas | UTS | UAS |  Nilai Akhir |")
            print("=" * 63)
            for i, (nim, d) in enumerate(nilai_data.items(), 1):
                print(f"{i}  | {d['nama']}\t| {nim}   | {d['tugas']}  | {d['uts']}| {d['uas']}| {d['nilai_akhir']:.2f}        |")
        print("=" * 63)

    elif pilihan == 't':
        nim = input("NIM: ")
        nilai_data[nim] = {
            "nama": input("Nama: "),
            **{y: float(input(f"Nilai {y}: ")) for y in ["tugas", "uts", "uas"]}
        }
        nilai_data[nim]["nilai_akhir"] = sum(nilai_data[nim][x] * w for x, w in zip(["tugas", "uts", "uas"], [0.3, 0.35, 0.35]))
        print("Data berhasil disimpan!")

    elif pilihan == 'u':
        nim = input("Masukkan NIM data yang ingin diubah: ")
        if nim in nilai_data:
            nilai_data[nim] = {
                "nama": input("Nama: "),
                **{y: float(input(f"Nilai {y}: ")) for y in ["tugas", "uts", "uas"]}
            }
            nilai_data[nim]["nilai_akhir"] = sum(nilai_data[nim][x] * w for x, w in zip(["tugas", "uts", "uas"], [0.3, 0.35, 0.35]))
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'h':
        nim = input("Masukkan NIM data yang ingin dihapus: ")
        if nim in nilai_data:
            del nilai_data[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'c':
        keyword = input("Masukkan nama atau NIM yang ingin dicari: ").lower()
        hasil = {nim: d for nim, d in nilai_data.items() if keyword in nim.lower() or keyword in d['nama'].lower()}
        if hasil:
            print("No | Nama\t|    NIM   | Tugas | UTS | UAS |  Nilai Akhir |")
            print("=" * 63)
            for i, (nim, d) in enumerate(hasil.items(), 1):
                print(f"{i}  | {d['nama']}\t| {nim}   | {d['tugas']}  | {d['uts']}| {d['uas']}| {d['nilai_akhir']:.2f}        |")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'k':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid!")
