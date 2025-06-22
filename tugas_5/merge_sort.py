# Merge Sort Step-by-Step Visualization (like the image)
def print_arrays_with_arrows(A, B, C, i, j, k):
    # Print Array A
    print("Array A: ", end="")
    for val in A:
        print(f"{val:4}", end="")
    print()
    # Print arrow for A
    print("         ", end="")
    for idx in range(len(A)):
        if idx == i:
            print("  ↓ ", end="")
        else:
            print("    ", end="")
    print()
    # Print Array B
    print("Array B: ", end="")
    for val in B:
        print(f"{val:4}", end="")
    print()
    # Print arrow for B
    print("         ", end="")
    for idx in range(len(B)):
        if idx == j:
            print("  ↓ ", end="")
        else:
            print("    ", end="")
    print()
    # Print Array C
    print("Array C: ", end="")
    for val in C:
        if val is None:
            print(f"{'_':4}", end="")
        else:
            print(f"{val:4}", end="")
    print()
    # Print arrow for C
    print("         ", end="")
    for idx in range(len(C)):
        if idx == k:
            print("  ↓ ", end="")
        else:
            print("    ", end="")
    print()

def merge_step_by_step(A, B, ascending=True):
    C = [None] * (len(A) + len(B))
    i = j = k = 0
    print("(a) Keadaan awal:")
    print_arrays_with_arrows(A, B, C, i, j, k)
    print(f"IndeksA: {i}, IndeksB: {j}, IndeksC: {k}\n")
    
    step = 1
    while i < len(A) and j < len(B):
        print(f"Membandingkan A[{i}] dan B[{j}]: {A[i]} vs {B[j]}")
        if (A[i] <= B[j] and ascending) or (A[i] >= B[j] and not ascending):
            C[k] = A[i]
            print(f"({chr(97+step)}) Setelah pengisian data ke {k+1} ke C:")
            print_arrays_with_arrows(A, B, C, i+1, j, k+1)
            print(f"IndeksA: {i+1}, IndeksB: {j}, IndeksC: {k+1}\n")
            i += 1
        else:
            C[k] = B[j]
            print(f"({chr(97+step)}) Setelah pengisian data ke {k+1} ke C:")
            print_arrays_with_arrows(A, B, C, i, j+1, k+1)
            print(f"IndeksA: {i}, IndeksB: {j+1}, IndeksC: {k+1}\n")
            j += 1
        k += 1
        step += 1
    while i < len(A):
        C[k] = A[i]
        print(f"({chr(97+step)}) Setelah pengisian data ke {k+1} ke C:")
        print_arrays_with_arrows(A, B, C, i+1, j, k+1)
        print(f"IndeksA: {i+1}, IndeksB: {j}, IndeksC: {k+1}\n")
        i += 1
        k += 1
        step += 1
    while j < len(B):
        C[k] = B[j]
        print(f"({chr(97+step)}) Setelah pengisian data ke {k+1} ke C:")
        print_arrays_with_arrows(A, B, C, i, j+1, k+1)
        print(f"IndeksA: {i}, IndeksB: {j+1}, IndeksC: {k+1}\n")
        j += 1
        k += 1
        step += 1
    print(f"Hasil akhir Array C: {C}\n")
    return C

def input_sorted_array(name, ascending=True):
    n = int(input(f"Masukkan jumlah elemen Array {name}: "))
    arr = []
    for i in range(n):
        val = int(input(f"Masukkan elemen ke-{i+1} Array {name}: "))
        arr.append(val)
    # Validasi urutan
    if ascending:
        if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
            print(f"Array {name} tidak terurut menaik. Silakan input ulang.")
            return input_sorted_array(name, ascending)
    else:
        if any(arr[i] < arr[i+1] for i in range(len(arr)-1)):
            print(f"Array {name} tidak terurut menurun. Silakan input ulang.")
            return input_sorted_array(name, ascending)
    return arr

def main():
    print("=== Merge Sort Step-by-Step ===")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Pilih urutan (1/2): ")
    ascending = True if choice == '1' else False
    # Input data dinamis
    print("Input Array A (sudah terurut sesuai pilihan)")
    A = input_sorted_array('A', ascending)
    print("Input Array B (sudah terurut sesuai pilihan)")
    B = input_sorted_array('B', ascending)
    merge_step_by_step(A, B, ascending)

if __name__ == "__main__":
    main()
