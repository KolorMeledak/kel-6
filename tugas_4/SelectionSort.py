repeat = True
def ascending(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list
def descending(list):
    for i in range(len(list)):
        max_idx = i
        for j in range(i+1, len(list)):
            if list[j] > list[max_idx]:
                max_idx = j
        list[i], list[max_idx] = list[max_idx], list[i]
    return list
 
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
    choice = input("Masukkan pilihan (1/2): ").strip()
    print("Hasil pengurutan:", arr)
    match choice:
        case '1':
            ascending(arr)
        case '2':
            descending(arr)
        case _:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

    
    
    choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
    if choose != 'y':
        repeat = False