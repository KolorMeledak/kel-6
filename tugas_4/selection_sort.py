
def format_num(num):
    """Mengubah angka menjadi string, tanpa '.0' jika itu bilangan bulat."""
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)

def format_list(numbers):
    """Mengubah seluruh list menjadi string yang sudah diformat dengan baik."""
    return f"[{', '.join([format_num(n) for n in numbers])}]"
# ---------------------------------------------


def selection_sort(data_list, mode):
    n = len(data_list)
    
    # Menentukan tipe elemen yang dicari berdasarkan mode
    if mode == 'ascending':
        tipe_elemen = "terkecil"
    elif mode == 'descending':
        tipe_elemen = "terbesar"

    # Menggunakan fungsi format_list untuk tampilan awal
    print(f"List Awal: {format_list(data_list)}\n")

    # Loop utama untuk setiap posisi dalam list
    for i in range(n - 1):
        print(f"--- Iterasi ke-{i + 1} ---")
        print(f"Tujuan: Mencari elemen {tipe_elemen} untuk ditempatkan di indeks {i}")
        
        indeks_min_max_relatif = 0 
        bagian_list = data_list[i:]
        
        print(f"(Mencari di dalam: {format_list(bagian_list)})")
        print(f"(Saat ini, elemen {tipe_elemen} sementara ada di indeks {i}, nilai: {format_num(bagian_list[indeks_min_max_relatif])})")
        print("Mulai membandingkan dengan sisa elemen:")

        # Loop untuk membandingkan dan mencari elemen terkecil/terbesar
        for j in range(1, len(bagian_list)):
            perlu_update = False
            if mode == 'ascending' and bagian_list[j] < bagian_list[indeks_min_max_relatif]:
                perlu_update = True
            elif mode == 'descending' and bagian_list[j] > bagian_list[indeks_min_max_relatif]:
                perlu_update = True

            if perlu_update:
                indeks_min_max_relatif = j
                
                print(f"     => Ditemukan elemen {tipe_elemen} baru di indeks {i + j} (nilai: {format_num(bagian_list[j])}).")

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

    print("--- Proses sorting selesai ---")
    
    print(f"Hasil Akhir: {format_list(data_list)}")
    return data_list

# --- Contoh Penggunaan ---
repeat = True
while repeat:
    print("===========Selection Sort Shifting===========")
    
    try:
        data_input = input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ")
        data = list(map(float, data_input.split()))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
        continue
    
    option = {
        1: 'Pengurutan Naik', 
        2: 'Pengurutan Turun', 
        3: 'Dua - Duanya'
    }
    while True:
        print("Pilih metode pengurutan:")
        for i, opt in option.items():
            print(f"{i}. {opt}")

        pilihan = input("Masukkan pilihan (1/2/3): ")
        mode = None
        if pilihan == '1':
            mode = 'ascending'
        elif pilihan == '2':
            mode = 'descending'
        elif pilihan == '3':
            print("Pengurutan Naik:")
            selection_sort(data.copy(), 'ascending')
            print("\nPengurutan Turun:")
            selection_sort(data.copy(), 'descending')
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        if mode:
            print("Data sebelum diurutkan:", format_list(data))
            print(f"Memulai Selection Sort dengan mode {mode}...")
            print("\n\n")
            selection_sort(data.copy(), mode)

        cek_lagi = input("Apakah ingin mencoba cek lagi? (y/n): ").strip().lower()
        if cek_lagi != 'y':
            break
    
    while True:
        choose = input("Apakah anda ingin mengulang program kembali? (y/n): ").strip().lower()
        if choose == 'y':
            repeat = True
            break
        elif choose == 'n':
            repeat = False
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")