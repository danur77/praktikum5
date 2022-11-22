#latihan
print("Nama : Danang Nurcahyo")
print("Nim  : 312210004")

print ("Membuat list sebanyak 5 elemen dengan nilai bebas")
# akses list
a = [30, 70, 80, 60, 100]
print(a) #menampilkan semua elemen
print(a[2]) #menampilkan elemen ke 3
print(a[1:3]) #menentukan elemen ke 2 sampai elemen ke 4
print(a[4]) #menampilkan elemen terakhir

print("==============================================")
# ubah elemen list
a[3] = 80 #mengubah elemen ke 4 dengan elemen lainya
print(a[3]) #menentukan elemen ke 4 yang sudah diubah elemennya
a[3:4] = 80, 90, #mengubah elemen ke 4 sampai dengan elemen terakhir
print(a[3:5]) #menampilkan elemnen ke 4 sampai dengan elemen ke terakhir

print("===============================================")
# tambah elemen list
b = a[0:2] #Mengambil 2 bagian dari list pertama (a) dan jadikan list kedua (b)
print(b)
b.append(45) #Menambahkan list dengan nilai string
print(b)
b.extend([35, 700, 55]) #Menambahkan list b dengan 3 nilai
print(b)
c = a+b # Menggabungkan list b denganlist a