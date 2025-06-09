def descending(arr):
    print("\nProses Bubble Sort: (descending)")
    a = arr.copy()
    n = len(a)
    for i in range(n-1):
        print(f"Iterasi ke {i}")
        for j in range(0, n - i - 1):
            print("=====================================")
            print(f"Langkah {i}.{j}: Pengecekan antara {a[j]} dengan {a[j+1]}")
            if a[j] < a[j + 1]:
                print(f"{a[j]} lebih kecil dari {a[j+1]}, terjadi penukaran")
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                print("Urutan sudah sesuai, Tidak ada penukaran")
            print(f"Array sekarang: {[int(x) if x.is_integer() else x for x in a]}")
            print("\r")
    print("Hasil akhir Bubble Sort:", [int(x) if x.is_integer() else x for x in a])

def ascending(arr):
    print("\nProses Bubble Sort (ascending):")
    a = arr.copy()
    n = len(a)
    for i in range(n-1):
        print(f"Iterasi ke {i}")
        for j in range(0, n - i - 1):
            print("=====================================")
            print(f"Langkah {i}.{j}: Pengecekan antara {a[j]} dengan {a[j+1]}")
            if a[j] > a[j + 1]:
                print(f"{a[j]} lebih besar dari {a[j+1]}, terjadi penukaran")
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                print("Urutan sudah sesuai, Tidak ada penukaran")
            print(f"Array sekarang: {[int(x) if x.is_integer() else x for x in a]}")
        print("\r")
    print(f"Hasil akhir Bubble Sort: {[int(x) if x.is_integer() else x for x in a]}")

repeat = True
while repeat:
    print("===========Bubble Sort===========")
    try:
        arr = input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ")
        arr = list(map(float, arr.split()))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
        continue
    
    option = {
        1: 'Pengurutan Naik',
        2: 'Pengurutan Turun',
        3: 'Pengurutan Naik dan Turun'
    }
    
    print("Pilih metode pengurutan:")
    for i, opt in option.items():
        print(f"{i}. {opt}")
    
    while True:
        choice = input("Masukkan pilihan (1/2/3): ").strip()
        print("Data sebelum diurutkan:", arr)
        match choice:
            case '1':
                ascending(arr)
                break
            case '2':
                descending(arr)
                break
            case '3':
                print("PENGURUTAN NAIK")
                ascending(arr)
                print('\n')
                print("PENGURUTAN TURUN")
                descending(arr)
                break
            case _:
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
    if choose != 'y':
        print("Terima Kasih!, Program Dihentikan.")
        repeat = False
