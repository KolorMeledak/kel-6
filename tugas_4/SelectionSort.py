def descending(arr):
    print("\nProses Selection Sort (descending):")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] < a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Langkah {i}: {a}")
    print(f"Hasil akhir Selection Sort: {a}")

def ascending(arr):
    print("\nProses Selection Sort (ascending):")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Langkah {i}: {a}")
    print(f"Hasil akhir Selection Sort: {a}")

repeat = True
while repeat:
    print("===========Selection Sort===========")
    try:
        arr = input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ")
        arr = list(map(int, arr.split()))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
        continue
    
    option = {
        1: 'Pengurutan Naik',
        2: 'Pengurutan Turun'
    }
    
    print("Pilih metode pengurutan:")
    for i, opt in option.items():
        print(f"{i}. {opt}")
    
    while True:
        choice = input("Masukkan pilihan (1/2): ").strip()
        print("Data sebelum diurutkan:", arr)
        match choice:
            case '1':
                ascending(arr)
                break
            case '2':
                descending(arr)
                break
            case _:
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    while True:
        choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
        if choose == 'y':
            break
        elif choose == 'n':
            repeat = False
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
