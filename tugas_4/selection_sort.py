from fractions import Fraction

# --- Helper Function untuk Formatting Output ---
def format_num(num):
    """Mengubah angka/pecahan menjadi string, tanpa '.0' jika itu bilangan bulat."""
    # Tambahkan pengecekan untuk tipe data Fraction
    if isinstance(num, Fraction):
        return str(num)
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)

def format_list(numbers):
    """Mengubah seluruh list menjadi string yang sudah diformat dengan baik."""
    return f"[{', '.join([format_num(n) for n in numbers])}]"
# ---------------------------------------------


def selection_sort(data_list, mode, direction='left-to-right'):
    """
    data_list: list data yang akan diurutkan
    mode: 'ascending' atau 'descending'
    direction: 'left-to-right' (default) atau 'right-to-left'
    """
    n = len(data_list)
    if mode == 'ascending':
        tipe_elemen = "terkecil"
    elif mode == 'descending':
        tipe_elemen = "terbesar"

    arah_teks = "kiri ke kanan" if direction == 'left-to-right' else "kanan ke kiri"
    print(f"List Awal: {format_list(data_list)} (proses {arah_teks})\n")

    if direction == 'left-to-right':
        # Proses seperti biasa (pivot di kiri, geser ke kanan)
        for i in range(n - 1):
            print(f"--- Iterasi ke-{i + 1} ---")
            print(f"Tujuan: Mencari elemen {tipe_elemen} untuk ditempatkan di indeks {i}")

            indeks_min_max_relatif = 0
            bagian_list = data_list[i:]

            print(f"(Mencari di dalam: {format_list(bagian_list)})")
            print(f"(Saat ini, elemen {tipe_elemen} sementara ada di indeks {i}, nilai: {format_num(bagian_list[indeks_min_max_relatif])})")
            print("Mulai membandingkan dengan sisa elemen:")

            for j in range(1, len(bagian_list)):
                perlu_update = False
                if mode == 'ascending' and bagian_list[j] < bagian_list[indeks_min_max_relatif]:
                    perlu_update = True
                elif mode == 'descending' and bagian_list[j] > bagian_list[indeks_min_max_relatif]:
                    perlu_update = True

                if perlu_update:
                    indeks_min_max_relatif = j
                    print(f"=> Ditemukan elemen {tipe_elemen} baru di indeks {i + j} (nilai: {format_num(bagian_list[j])}).")

            indeks_min_max_absolut = i + indeks_min_max_relatif

            print(f"\nHasil Iterasi {i + 1}: Elemen {tipe_elemen} ditemukan di indeks {indeks_min_max_absolut} (nilai: {format_num(data_list[indeks_min_max_absolut])}).")

            if indeks_min_max_absolut != i:
                print(f"Melakukan pergeseran: Menghapus elemen dari indeks {indeks_min_max_absolut} dan menyisipkannya di indeks {i}.")

                elemen_dipindah = data_list.pop(indeks_min_max_absolut)
                data_list.insert(i, elemen_dipindah)

                print(f"  -> List setelah elemen '{format_num(elemen_dipindah)}' disisipkan di indeks {i}: {format_list(data_list)}")
            else:
                print(f"Elemen {tipe_elemen} sudah berada di posisi yang benar. Tidak ada pergeseran.")

            print(f"List setelah iterasi {i + 1}: {format_list(data_list)}\n")
    else:
        # Proses dari kanan ke kiri (pivot di kanan, geser ke kiri)
        for i in range(n - 1, 0, -1):
            iterasi_ke = n - i
            print(f"--- Iterasi ke-{iterasi_ke} ---")
            print(f"Tujuan: Mencari elemen {tipe_elemen} untuk ditempatkan di indeks {i}")

            bagian_list = data_list[:i+1]
            indeks_min_max_relatif = 0

            print(f"(Mencari di dalam: {format_list(bagian_list)})")
            print(f"(Saat ini, elemen {tipe_elemen} sementara ada di indeks 0, nilai: {format_num(bagian_list[indeks_min_max_relatif])})")
            print("Mulai membandingkan dengan sisa elemen:")

            for j in range(1, len(bagian_list)):
                perlu_update = False
                if mode == 'ascending' and bagian_list[j] > bagian_list[indeks_min_max_relatif]:
                    perlu_update = True
                elif mode == 'descending' and bagian_list[j] < bagian_list[indeks_min_max_relatif]:
                    perlu_update = True

                if perlu_update:
                    indeks_min_max_relatif = j
                    print(f"=> Ditemukan elemen {tipe_elemen} baru di indeks {j} (nilai: {format_num(bagian_list[j])}).")

            indeks_min_max_absolut = indeks_min_max_relatif

            print(f"\nHasil Iterasi {iterasi_ke}: Elemen {tipe_elemen} ditemukan di indeks {indeks_min_max_absolut} (nilai: {format_num(data_list[indeks_min_max_absolut])}).")

            if indeks_min_max_absolut != i:
                print(f"Melakukan pergeseran: Menghapus elemen dari indeks {indeks_min_max_absolut} dan menyisipkannya di indeks {i}.")

                elemen_dipindah = data_list.pop(indeks_min_max_absolut)
                data_list.insert(i, elemen_dipindah)

                print(f"  -> List setelah elemen '{format_num(elemen_dipindah)}' disisipkan di indeks {i}: {format_list(data_list)}")
            else:
                print(f"Elemen {tipe_elemen} sudah berada di posisi yang benar. Tidak ada pergeseran.")

            print(f"List setelah iterasi {iterasi_ke}: {format_list(data_list)}\n")

    print("--- Proses sorting selesai ---")
    print(f"Hasil Akhir: {format_list(data_list)}")
    return data_list

# --- Contoh Penggunaan ---
repeat = True
while repeat:
    print("===========Selection Sort Shifting===========")
    
    # --- BLOK INPUT YANG DIMODIFIKASI ---
    try:
        data_input = input("Masukkan angka (termasuk desimal/pecahan, pisahkan spasi): ")
        data = []
        for item_str in data_input.split():
            # Jika input mengandung '/', anggap sebagai pecahan
            if '/' in item_str:
                data.append(Fraction(item_str))
            # Jika tidak, anggap sebagai float (untuk desimal dan integer)
            else:
                data.append(float(item_str))
    except (ValueError, ZeroDivisionError):
        print("Input tidak valid. Pastikan semua angka dan pecahan (format a/b) benar.")
        continue
    # ------------------------------------
    
    option = {
        1: 'Pengurutan Naik', 
        2: 'Pengurutan Turun', 
        3: 'Dua - Duanya'
    }
    def pivot_pilihan(pilihan_pivot):
        pivot_option = {
            1: 'Kiri ke Kanan',
            2: 'Kanan ke Kiri'
        }
        print("\nPilih letak pivot untuk dimulai pertama kali pengurutan:")
        for i, opt in pivot_option.items():
            print(f"{i}. {opt}")
        masukan = input("Masukkan pilihan untuk pivot dimulai sortingan (1/2): ")
        match masukan:
            case '1':
                return 'left-to-right'
            case '2':
                return 'right-to-left'
            case _:
                print("Pilihan tidak valid. Menggunakan default 'left-to-right'.")
                return 'left-to-right'
        pivot = pivot_pilihan(option)      
        return pivot         
        
    while True:
        print("\nPilih metode pengurutan:")
        for i, opt in option.items():
            print(f"{i}. {opt}")

        pilihan = input("Masukkan pilihan (1/2/3): ")
        mode = None
        if pilihan == '1':
            mode = 'ascending'
            selection_sort(data.copy(), mode, pivot_pilihan(option))
        elif pilihan == '2':
            mode = 'descending'
            selection_sort(data.copy(), mode, pivot_pilihan(option))
        elif pilihan == '3':
            pivot = pivot_pilihan(option)
            print("\n--- Pengurutan Naik ---")
            selection_sort(data.copy(), 'ascending', pivot)
            print("\n--- Pengurutan Turun ---")
            selection_sort(data.copy(), 'descending', pivot)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        cek_lagi = input("\nApakah ingin mencoba metode urut lain dengan data yang sama? (y/n): ").strip().lower()
        if cek_lagi != 'y':
            break
    
    while True:
        choose = input("\nApakah anda ingin mengulang program dengan data baru? (y/n): ").strip().lower()
        if choose == 'y':
            repeat = True
            break
        elif choose == 'n':
            repeat = False
            print("\nDAH MAS. DAH SELESAI PROGRAMNYA. TERIMA KASih! 😘😘")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")