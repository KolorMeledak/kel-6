def descending(arr):
    print("\nProses Insertion Sort (descending):")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key > a[j]:
            a[j + 1] = a[j]
            j -= 1
            print(f"Langkah {i}.{j + 1}: {a}")
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {a}")
    print(f"Hasil akhir Insertion Sort: {a}")

def ascending(arr):
    print("\nProses Insertion Sort (ascending):")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            print(f"Langkah {i}.{j + 1}: {a}")
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {a}")
    print(f"Hasil akhir Insertion Sort: {a}")

repeat = True
while repeat:
    print("===========Insertion Sort===========")
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
    
    choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
    if choose != 'y':
        repeat = False
