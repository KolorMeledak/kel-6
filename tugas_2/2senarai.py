from lib.linked import LinkedList

ll = LinkedList()
ll.insert("AMN", "Aminudin")
ll.insert("ZAS","Zaskia")
ll.insert("RIN", "Rina Melati")
ll.insert("FAR", "Farhan")
ll.insert("AGN", "Agnes Monica")

def program():

    def assign():
        inputan = str(input("Masukkan kode dan nama sesuai dengan ketentuannya (Ex. AF, Aminudin Fikri) = "))
        try:
            inisial, nama = list(map(lambda name: name.strip(), inputan.split(','))) 
            inisial = inisial.upper()
            
            ll.insert(inisial, nama)
            print(f"Data {inisial}, {nama} berhasil ditambahkan.")
        except ValueError:
            print("Format salah! Gunakan format: INISIAL, Nama Panjang (Ex. AF, Aminudin Fikri)")
    
    def remove():
        inputan = input("Masukkan kode atau nama yang perlu dihapus: ")
        inputan = inputan.upper()
        ll.delete(f"{inputan}")
    
    def search():
        inputan = str(input("Masukkan kode atau nama yang ingin dicari = "))
        inputan = inputan.upper()
        ll.search(f"{inputan}")
        
    ll.display()

    retry = True
    while retry:
        pilihan = {
        1: 'Tambah Data',
        2: 'Hapus Data',
        3: 'Pencarian Data',
        4: 'Tampilkan Data',
        5: 'Selesai'
        }
        
        
        print("Menu:")
        for i, data in pilihan.items():
            print(f'{i}. {data}')
        
        option = int(input("Pilih salah satu dari pilihan tersedia (1/2/3/4/5) "))
        
        match option :
            case 1:
                print(pilihan[option], end='. \n')
                assign()
            case 2:
                print(pilihan[option], end='. \n')
                remove()
            case 3:
                print(pilihan[option], end='. \n')
                search()
            case 4:
                ll.display()
            case 5:
                retry = False
                
if __name__ == "__main__":
    program()
    