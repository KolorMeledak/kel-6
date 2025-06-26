# KHAIRUL AKMAL
# 1313624017

def format_num(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)

def format_list(numbers, kosong_index=None):
    result = []
    for i, num in enumerate(numbers):
        if i == kosong_index:
            result.append("....")
        else:
            result.append(format_num(num))
    return f"[{', '.join(result)}]"

def descending(arr):
    print("\n---------Proses Insertion Sort (descending):---------")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        langkah = 1
        pergeseran = False
        while j >= 0:
            kondisi = "lebih besar" if key > a[j] else "tidak lebih besar"
            print(f"Bandingkan key={format_num(key)} dengan a[{j}]={format_num(a[j])} → {kondisi}")
            if key > a[j]:
                a[j + 1] = a[j]
                print(f"Langkah {i}.{langkah}: {format_list(a, j)}")
                langkah += 1
                j -= 1
                pergeseran = True
            else:
                break
        a[j + 1] = key
        if pergeseran:
            print(f".... diganti {format_num(key)}")
        else:
            print(f"Key langsung ditempatkan tanpa pergeseran.")
        print(f"Setelah penyisipan {i}: {format_list(a)}\n")
    print(f"Hasil akhir Insertion Sort: {format_list(a)}")

def ascending(arr):
    print("\n---------Proses Insertion Sort (ascending):---------")
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        langkah = 1
        pergeseran = False
        while j >= 0:
            kondisi = "lebih kecil" if key < a[j] else "tidak lebih kecil"
            print(f"Bandingkan key={format_num(key)} dengan a[{j}]={format_num(a[j])} → {kondisi}")
            if key < a[j]:
                a[j + 1] = a[j]
                print(f"Langkah {i}.{langkah}: {format_list(a, j)}")
                langkah += 1
                j -= 1
                pergeseran = True
            else:
                break
        a[j + 1] = key
        if pergeseran:
            print(f".... diganti {format_num(key)}")
        else:
            print(f"Key langsung ditempatkan tanpa pergeseran.")
        print(f"Setelah penyisipan {i}: {format_list(a)}\n")
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
