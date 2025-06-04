def descending(arr):
    print("\nProses Bubble Sort: (descending)")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            print(f"Langkah {i}.{j}: {a}")
    print(f"Hasil akhir Bubble Sort: {a}")

def ascending(arr):
    print("\nProses Bubble Sort (ascending):")
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            print(f"Langkah {i}.{j}: {a}")
    print(f"Hasil akhir Bubble Sort: {a}")

repeat = True
while repeat:
    print("===========Bubble Sort===========")
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
