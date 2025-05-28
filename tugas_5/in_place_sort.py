repeat = True
while repeat:
    try:
        n = int(input("Masukkan jumlah elemen: "))
        if n <= 0:
            raise ValueError("Jumlah elemen harus positif.")
        repeat = False
    except ValueError as e:
        print(f"Input tidak valid: {e}")
    print("Masukkan elemen-elemen:  (gunakan spasi sebagai pemisah)")
    arr = input("Masukkan angka yang ingin diurutkan: ")
    if not arr.strip():
        print("Input tidak boleh kosong. Silakan coba lagi.")
        continue
    try:
        arr = list(map(int, arr.split()))
        if len(arr) != n:
            raise ValueError(f"Jumlah elemen yang dimasukkan ({len(arr)}) tidak sesuai dengan jumlah yang diminta ({n}).")
        if any(not isinstance(x, int) for x in arr):
            raise ValueError("Semua elemen harus berupa angka bulat.")
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        continue
    if len(arr) == 0:
        print("Tidak ada elemen yang dimasukkan. Silakan coba lagi.")
        continue
    print("Elemen yang dimasukkan:", arr)
    arr = list(map(int, arr.split()))
    def in_place_sort_descent(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Langkah {i}: {arr}")  # Menampilkan array setelah setiap pass
        return arr
    def in_place_sort_ascent(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j <= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Langkah {i}: {arr}")  # Menampilkan array setelah setiap pass
        return arr
    option = {
        1: 'Pengurutan Turun',
        2: 'Pengurutan Naik'
    }
    print("Pilih metode pengurutan:")
    for i, opt in option.items():
        print(f"{i}. {opt}")
    choice = input("Masukkan pilihan (1/2): ").strip()
    match choice:
        case '1':
            sorted_elements = in_place_sort_descent(arr)
        case '2':
            sorted_elements = in_place_sort_ascent(arr)
        case _:
            print("Pilihan tidak valid. Silakan coba lagi.")
            sorted_elements = arr  # Tetap tampilkan elemen asli jika pilihan tidak valid
    print("Elemen setelah diurutkan:", sorted_elements)
    choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
    if choose != 'y':
        repeat = False
print("Terima kasih telah menggunakan program ini!")

