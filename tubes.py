def create(data):
    print("\n=== TAMBAH DATA TIM ===")

    try:
        nama = input("Masukkan nama tim: ").strip()

        if nama == "":
            print("Nama tim tidak boleh kosong!")
            input("Tekan ENTER untuk kembali...")
            return data

        menang = int(input("Masukkan jumlah menang: "))
        kalah = int(input("Masukkan jumlah kalah: "))

        if menang < 0 or kalah < 0:
            print("Jumlah menang/kalah tidak boleh negatif!")
            input("Tekan ENTER untuk kembali...")
            return data

        # Perhitungan poin
        poin = menang * 2

        data.append([nama, menang, kalah, poin])

        print("\nData tim berhasil ditambahkan!")

    except ValueError:
        print("\nInput jumlah menang dan kalah harus berupa angka!")

    input("Tekan ENTER untuk kembali...")
    return data



def read(data):
    if len(data) == 0:
        print("\nBelum ada data tim.")
        input("Tekan ENTER untuk kembali...")
        return

    print("\n=== DATA PERINGKAT MPL ID ML ===")
    print("-" * 65)
    print(f"{'No':<5}{'Tim':<20}{'Menang':<10}{'Kalah':<10}{'Poin':<10}")
    print("-" * 65)

    for i, tim in enumerate(data):
        print(f"{i+1:<5}{tim[0]:<20}{tim[1]:<10}{tim[2]:<10}{tim[3]:<10}")

    print("-" * 65)

    print("\n1. Urutkan berdasarkan poin")
    print("2. Cari tim")
    print("3. Kembali")

    try:
        pilihan = int(input("Pilih menu [1-3]: "))

        if pilihan == 1:
            sortData(data)

        elif pilihan == 2:
            searchData(data)

        elif pilihan == 3:
            return

        else:
            print("Pilihan hanya 1 sampai 3.")

    except ValueError:
        print("Input harus berupa angka.")

    input("Tekan ENTER untuk kembali...")


def update(data):
    if len(data) == 0:
        print("\nBelum ada data tim.")
        input("Tekan ENTER untuk kembali...")
        return data

    print("\n=== DATA TIM ===")

    for i, tim in enumerate(data):
        print(f"{i+1}. {tim[0]} | Menang: {tim[1]} | "
              f"Kalah: {tim[2]} | Poin: {tim[3]}")

    try:
        nomor = int(input("\nMasukkan nomor tim yang ingin diubah: "))

        if nomor < 1 or nomor > len(data):
            print("Nomor tim tidak ditemukan!")
            input("Tekan ENTER untuk kembali...")
            return data

        index = nomor - 1

        nama = input("Masukkan nama tim baru: ").strip()

        if nama == "":
            print("Nama tim tidak boleh kosong!")
            input("Tekan ENTER untuk kembali...")
            return data

        menang = int(input("Masukkan jumlah menang baru: "))
        kalah = int(input("Masukkan jumlah kalah baru: "))

        if menang < 0 or kalah < 0:
            print("Jumlah menang/kalah tidak boleh negatif!")
            input("Tekan ENTER untuk kembali...")
            return data

        poin = menang * 2

        data[index] = [nama, menang, kalah, poin]

        print("\nData berhasil diperbarui!")

    except ValueError:
        print("\nInput harus berupa angka!")

    input("Tekan ENTER untuk kembali...")
    return data


def delete(data):
    if len(data) == 0:
        print("\nBelum ada data tim.")
        input("Tekan ENTER untuk kembali...")
        return data

    print("\n=== DATA TIM ===")

    for i, tim in enumerate(data):
        print(f"{i+1}. {tim[0]}")

    try:
        nomor = int(input("\nMasukkan nomor tim yang ingin dihapus: "))

        if nomor < 1 or nomor > len(data):
            print("Nomor tim tidak ditemukan!")
            input("Tekan ENTER untuk kembali...")
            return data

        index = nomor - 1

        tim_dihapus = data.pop(index)

        print(f"Tim {tim_dihapus[0]} berhasil dihapus!")

    except ValueError:
        print("Input harus berupa angka!")

    input("Tekan ENTER untuk kembali...")
    return data


def sortData(data):
    if len(data) == 0:
        print("Belum ada data untuk diurutkan.")
        return

    # Urut berdasarkan poin terbesar
    data.sort(key=lambda x: x[3], reverse=True)

    print("\n=== PERINGKAT TIM ===")
    print("-" * 65)
    print(f"{'Rank':<5}{'Tim':<20}{'Menang':<10}{'Kalah':<10}{'Poin':<10}")
    print("-" * 65)

    for i, tim in enumerate(data):
        print(f"{i+1:<5}{tim[0]:<20}{tim[1]:<10}{tim[2]:<10}{tim[3]:<10}")

    print("-" * 65)



def searchData(data):
    if len(data) == 0:
        print("Belum ada data untuk dicari.")
        return

    keyword = input("Masukkan nama tim yang ingin dicari: ").strip().lower()

    ditemukan = False

    print("\n=== HASIL PENCARIAN ===")

    for tim in data:
        if keyword in tim[0].lower():
            print(f"Tim    : {tim[0]}")
            print(f"Menang : {tim[1]}")
            print(f"Kalah  : {tim[2]}")
            print(f"Poin   : {tim[3]}")
            print("-" * 30)

            ditemukan = True

    if not ditemukan:
        print("Tim tidak ditemukan.")



def pilihPemenang(tim1, tim2):
    print(f"\n1. {tim1}")
    print(f"2. {tim2}")

    while True:
        try:
            pilihan = int(input("Pilih pemenang [1-2]: "))

            if pilihan == 1:
                return tim1

            elif pilihan == 2:
                return tim2

            else:
                print("Pilihan hanya 1 atau 2.")

        except ValueError:
            print("Input harus berupa angka 1 atau 2.")



def playoffBracket(data):

    if len(data) < 4:
        print("\nMinimal harus ada 4 tim untuk membuat bracket playoff!")
        input("Tekan ENTER untuk kembali...")
        return

    # Salin data agar sorting bracket tidak mengubah urutan data utama
    ranking = sorted(data, key=lambda x: x[3], reverse=True)

    print("\n========================================")
    print("       BRACKET PLAYOFF MPL ID ML")
    print("========================================")

    print("\nTIM YANG LOLOS PLAYOFF:")

    for i in range(4):
        print(
            f"{i+1}. {ranking[i][0]} "
            f"(Menang: {ranking[i][1]}, "
            f"Poin: {ranking[i][3]})"
        )


    print("\n========================================")
    print("              SEMIFINAL")
    print("========================================")

    # Juara 1 melawan peringkat 4
    timA = ranking[0][0]
    timB = ranking[3][0]

    print(f"\nSEMIFINAL 1")
    print(f"{timA} VS {timB}")

    pemenang1 = pilihPemenang(timA, timB)

    # Peringkat 2 melawan peringkat 3
    timC = ranking[1][0]
    timD = ranking[2][0]

    print(f"\nSEMIFINAL 2")
    print(f"{timC} VS {timD}")

    pemenang2 = pilihPemenang(timC, timD)


    print("\n========================================")
    print("             GRAND FINAL")
    print("========================================")

    print(f"\n{pemenang1} VS {pemenang2}")

    juara = pilihPemenang(pemenang1, pemenang2)

    print("\n========================================")
    print("               HASIL AKHIR")
    print("========================================")
    print(f"JUARA MPL ID ML: {juara}")
    print("========================================")

    input("Tekan ENTER untuk kembali...")


def menuUtama():

    print("\n========================================")
    print("     APLIKASI DATA PERINGKAT MPL ID ML")
    print("     BY:Edwin Kurniawan Eka J , 11251082")
    print("========================================")
    print("1. Tambah Data Tim")
    print("2. Lihat Data Tim")
    print("3. Edit Data Tim")
    print("4. Hapus Data Tim")
    print("5. Simulasi Bracket Playoff")
    print("6. Keluar")
    print("========================================")

    try:
        pilihan = int(input("Masukkan pilihan [1-6]: "))

        if pilihan < 1 or pilihan > 6:
            print("Pilihan hanya antara 1 sampai 6.")
            return 0

        return pilihan

    except ValueError:
        print("Input harus berupa angka!")
        return 0


data = []

pilihan = 0

while pilihan != 6:

    pilihan = menuUtama()

    if pilihan == 1:
        data = create(data)

    elif pilihan == 2:
        read(data)

    elif pilihan == 3:
        data = update(data)

    elif pilihan == 4:
        data = delete(data)

    elif pilihan == 5:
        playoffBracket(data)

    elif pilihan == 6:
        print("\nTerima kasih telah menggunakan program!")