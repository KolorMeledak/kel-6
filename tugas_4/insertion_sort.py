def format_num(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)

def format_list(numbers):
    return f"[{', '.join([format_num(n) for n in numbers])}]"

def descending(arr):
    print("\nProses Insertion Sort (descending):")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        langkah = 1
        while j >= 0 and key > a[j]:
            a[j + 1] = a[j]
            print(f"Langkah {i}.{langkah}: {format_list(a)}")
            langkah += 1
            j -= 1
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {format_list(a)}")
    print(f"Hasil akhir Insertion Sort: {format_list(a)}")

def ascending(arr):
    print("\nProses Insertion Sort (ascending):")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        langkah = 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            print(f"Langkah {i}.{langkah}: {format_list(a)}")
            langkah += 1
            j -= 1
        a[j + 1] = key
        print(f"Setelah penyisipan {i}: {format_list(a)}")
    print(f"Hasil akhir Insertion Sort: {format_list(a)}")

repeat = True
while repeat:
    print("===========Insertion Sort===========")
    try:
        arr = input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ")
        arr = list(map(float, arr.split()))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
        continue
    
    option = {
        1: 'Pengurutan Naik',
        2: 'Pengurutan Turun',
        3: 'Dua - Duanya'
    }
    
    print("Pilih metode pengurutan:")
    for i, opt in option.items():
        print(f"{i}. {opt}")
    
    while True:
        choice = input("Masukkan pilihan (1/2/3): ").strip()
        print("Data sebelum diurutkan:", format_list(arr))
        match choice:
            case '1':
                ascending(arr)
                break
            case '2':
                descending(arr)
                break
            case '3':
                ascending(arr)
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
