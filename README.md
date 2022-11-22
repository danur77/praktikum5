# Praktikum5
Nama : Danang Nurchayo

NIM : 312210004

Kelas : TI.22.A1
## DAFTAR ISI <br>
| No | Description | Link |
|-----|------|-----|
|1|Latihan|[Click Here](#latihan)|
|2|Praktikum 5|[Click Here](#praktikum-5)|

## Latihan
Buat sebuah list sebanyak 5 elemen dengan nilai bebas

#### Akses list :
- Tampilkan elemen ke 3
- Ambil nilai elemen ke 2 sampai elemen ke 4
- Ambil elemen terakhir
#### Ubah elemen list :
- Ubah elemen ke 4 dengan nilai lainnya
- Ubah elemen ke 4 sampai dengan elemen terakhir
#### Tambah elemen list :
- Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
- Tambah list B dengan nilai string
- Tambah list B dengan 3 nilai
- Gabungkan list B dengan list A

#### Langkah-langkah :
1. Buat programnya terlebih dahulu seperti gambar di bawah ini

![Screenshot (82)](https://user-images.githubusercontent.com/115677839/203316771-868922c0-be2b-4218-8c73-b45a64755a93.png)
![Screenshot (83)](https://user-images.githubusercontent.com/115677839/203316853-597f75ba-6820-448f-8b64-5af2fc7d48b3.png)

   # Latihan
    print("Nama : Danang Nurcahyo")
    print("NIM  : 312210004")

    print("Membuat List sebanyak 5 elemen dengan nilai bebas")
    # akses list
    a = [20, 40, 50, 60, 100]
    print(a) #Menampilkan semua elemen
    print(a[2]) #Menampilkan elemen ke 3
    print(a[1:3]) #Menampilkan elemen ke 2 sampai dengan ke 4
    print(a[4]) #Menampilkan elemen terakhir

    print("------------------------------------------")
    # ubah elemen list
    a[3] = 80 # Mengubah elemen ke 4 dengan nilai lainnya
    print(a[3]) # Menampilkan elemen ke 4 yang sudah diubah nilainya
    a[3:4] = 80, 90 # Mengubah elemen ke 4 sampai dengan elemen terakhir
    print(a[3:5]) # menampilkan elemen ke 4 sampai dengan elemen terakhir

    print("------------------------------------------")
    # tambah elemen list
    b = a[0:2] # Mengambil 2 bagian dari list pertama (a) dan jadikan list 
    kedua (b)
    print(b)
    b.append(45) # Menambah list dengan nilai string
    print(b)
    b.extend([85, 90, 95]) # Menambah list b dengan 3 nilai
    print(b)
    c = a+b # Menggabungkan list b dengan list a
    print(c)
    
2. Hasil Run

![Screenshot (84)](https://user-images.githubusercontent.com/115677839/203316968-081b9516-c19f-4a41-a3ab-9ff3b8491974.png)

 
## Praktikum 5
Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut :

- Program meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
- Tampilkan pertanyaan untuk menambah data (ya/tidak?), apabila jawaban   
"tidak", maka program akan menampilkan daftar datanya.
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
- Buat flowchart dan penjelasan programnya pada README.md.
- Commit dan push repository ke github.

#### Langkah-langkah :
1. Buat programnya terlebih dahulu seperti gambar di bawah ini

![Screenshot (86)](https://user-images.githubusercontent.com/115677839/203317039-49361d6d-e4b6-4c09-8481-de77bb7f65ba.png)


    # Membuat Tugas Praktikum
    data =[]
    while True :
        nama       = input    ("Nama        : ")
        nim        = input    ("NIM         : ")
        tugas      = int(input("Nilai Tugas : "))
        uts        = int(input("Nilai UTS   : "))
        uas        = int(input("Nilai UAS   : "))
        nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
        data.append([nama,nim,tugas,uts,uas,nilaiakhir])
        lagi= input("Tambah data (ya/tidak)? ")
        if lagi.lower() =="tidak":
            break


    print("=====================================================================================");
    print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
    print("=====================================================================================");
    i=0
    for x in data:
        i+=1
        print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
              .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
    print("=====================================================================================");
    
2. Hasil Run

![Screenshot (85)](https://user-images.githubusercontent.com/115677839/203317099-39e023aa-16be-46d7-afaa-2283f50c7c83.png)



### Penjelasan Program :
1. Buatlah list berupa Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS.
2. Lalu inputlah Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS.
3. Lalu mencari nilai akhir dengan perhitungan nilai tugas 30%, nilai uts 35% dan uas 35% , dengan perintah float
4. Gunakan perintah append pada Nama, NIM, Nilai tugas, Nilai UTS, Nilai UAS untuk menambahkan 1 item ke elemen terakhir.
5. Jika ingin menambah list data ketik "ya" dan jika tidak ingin menambahkan list data ketik "tidak". Dengan perintah while jawab =="ya" dan if jawab =="tidak". Jawab input("Tambah data (ya/tidak)").
6. Gunakanlah perulangan for, dengan perintah for i in range(len(Nama)):. Fungsi "len" ialah untuk mengembalikan panjang (jumlah anggota) dari suatu objek.
7. Lalu cetak dengan perintah print
8. Selesai

### Flowchart Praktikum 5

![WhatsApp Image 2022-11-20 at 23 03 46](https://user-images.githubusercontent.com/115677839/203317152-f2b52007-cb88-45c0-b76c-de998a0f49d8.jpg)

### Sekian, Terima kasih
## ALLHAMDULILLAH
