# _UAS-PBO-YUMA-CHINDY_
NAMA KELOMPOK:
1. Yuma Juliana (G1F022003)
2. Chindy Feby Amara (G1F022045)
## 1. Mengedit gambar dengan Python: Perpustakaan Pencitraan Python menawarkan juru 	bahasa untuk mengedit gambar. Ini membantu untuk membuka, memotong, mengubah 	ukuran, mengambil ukuran dan menyimpan gambar.
 A. Instal pillow 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/5c2c9d9a-d830-4a4f-854d-26ac2402c3f2)
<h5 align="center"> Gambar 3.1 Install pillow </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
  Penjelasan :
  
   Pillow adalah library Python yang digunakan untuk pemrosesan gambar. Fungsi utama dari Pillow adalah memungkinkan Anda membuka, memanipulasi, dan menyimpan berbagai format file gambar. Beberapa tugas umum yang dapat dilakukan dengan menggunakan Pillow Membuka dan Menyimpan Gambar: Pillow mendukung berbagai format file gambar seperti JPEG, PNG, GIF, BMP, dan lainnya. Anda dapat menggunakan Pillow untuk membuka gambar dari file dan menyimpannya ke format yang berbeda.
>

B. Install matplotlib 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/fe17b5fd-5687-4971-8f7f-8bcb7e0a02db)

<h5 align="center"> Gambar 3.2 Install matplotlib </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
  Penjelasan :
	
  Untuk menajalankan program pengeditan gambar ini kita perlu menginstal matplotlib dan pillow dimana pada gambar di atas merupakan penginstallan matplotlib adalah salah satu perpustakaan (library) dalam bahasa pemrograman Python yang digunakan untuk membuat visualisasi grafik dan plot. Penginstalan Matplotlib umumnya dilakukan untuk keperluan visualisasi data, analisis data, dan representasi grafis dari hasil perhitungan atau eksplorasi data.>

 C.	Kode untuk membuka dan menampilkan gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/3cc04672-11a6-49a3-87da-3ecc7a2750fa)

<h5 align="center"> Gambar 3.3 Kode untuk membuka dan menampilkan gambar </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
 Penjelasan kode : 
	
  from PIL import Image import matplotlib.pyplot as plt Kode ini di gunakan untuk mengimpor dua pustaka: PIL (Pillow) untuk memanipulasi gambar dan Matplotlib untuk menampilkan gambar. Yaitu dengan cara menginstal pillow pada terminal yaitu dengan cara mengetik pip install pillow maka secara otomatis akan terinstal kemudian menginstal matplotlib di terminal dengan cara mengetik pip install matplotlib maka akan terinstall. Fungsi def open_image(path):  try: menerima path file sebagai argumen. Dalam blok try, ini akan mencoba membuka gambar pada path yang diberikan menggunakan Image.open dari PIL. Jika berhasil, gambar dibaca dan dikembalikan. Jika terjadi IOError ( jika file tidak ditemukan), pesan "File tidak ditemukan!" dicetak di konsol. 

D.	Kode untuk menampilkan gambar :
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/f7cba296-2644-43a1-8101-1230ed1e2b8d)


<h5 align="center"> Gambar 3.4 kode menampilkan gambar </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
	
  def show_image(image): Fungsi ini menerima satu parameter, yaitu image. Parameter ini seharusnya berisi objek gambar yang dapat ditangani oleh Matplotlib. if image: Pada bagian ini, dilakukan pengecekan apakah parameter image memiliki nilai yang tidak nol atau tidak kosong. Jika image memiliki nilai, maka blok berikutnya akan dieksekusi; jika tidak, fungsi akan keluar tanpa melakukan apa pun.  plt.imshow(image) plt.show() kode ini artinya jika image ada (nilai tidak nol), fungsi ini menggunakan Matplotlib untuk menampilkan gambar. plt.imshow(image) digunakan untuk menampilkan gambar, dan plt.show() digunakan untuk menampilkan plot grafik (gambar) ke layar.>

E.	Kode untuk memotong gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/eb8204db-bbdb-4168-9059-b3fee0a661a4)



<h5 align="center"> Gambar 3.5 kode memotong gambar  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
def crop_image(image, top, left, bottom, right):  Fungsi ini mengambil lima parameter: image: Objek gambar yang akan dipotong (harus dapat ditangani oleh metode crop dari PIL). top, left, bottom, right: ini di gunakan untuk menentukan batas koordinat untuk pemotongan gambar. Parameter ini menentukan area yang akan dipotong dari gambar yaitu dengan memasukkan memasukkan bastas atas, batas kiri, batas bawah dan batas kanan sesuai dengan ukuran yang kita inginkan maka gambarnya akan terpotong sesuai dengan instruksi yang telah kita masukkan. 

cropped_image = image.crop((left, top, right, bottom))  return cropped_image Fungsi kode ini adalah mencoba untuk melakukan pemotongan gambar menggunakan metode crop dari objek gambar (image). Batas koordinat dipass sebagai tupel (left, top, right, bottom) ke metode crop. Jika pemotongan berhasil, gambar hasil pemotongan (cropped_image) dikembalikan.
except ValueError: print("Batas koordinat tidak valid!") ika terjadi ValueError, yang mungkin terjadi jika batas koordinat tidak valid (misalnya, top lebih besar dari bottom atau left lebih besar dari right), maka pesan kesalahan "Batas koordinat tidak valid!" dicetak di konsol.>

F.	Kode untuk mengubah ukuran gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/605dc44c-3866-447a-a141-f7f7e753b722)

<h5 align="center"> Gambar 3.6 kode mengubah ukuran gambar  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
def resize_image(image, width, height): Fungsi kode ini adalah untuk mengambil tiga parameter: image: Objek gambar yang akan diubah ukurannya (harus dapat ditangani oleh metode resize dari PIL). Width Lebar baru yang diinginkan untuk gambar. height Tinggi baru yang diinginkan untuk gambar.

  try: resized_image = image.resize((width, height))  return resized_image Fungsi kode ini adalah untuk mengubah ukuran gambar menggunakan metode resize dari objek gambar (image). Parameter (width, height) adalah ukuran yang baru diinginkan. Jika pengubahan ukuran berhasil, gambar hasil diubah ukuran (resized_image) dikembalikan.
except ValueError: print("Ukuran tidak valid!") kode ini diguakan untuk Jika terjadi ValueError, yang mungkin terjadi jika ukuran yang dimasukkan tidak valid (misalnya, nilai negatif), maka pesan kesalahan "Ukuran tidak valid!" dicetak di konsol.>

G.	 Kode untuk menyimpan gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/1750319c-9937-4674-a892-97f0c24951b6)

<h5 align="center"> Gambar 3.7 Kode menyimpan gambar  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan :
  
def save_image(image, path): Kode ini di gunakan untuk  fungsi save_image yang mengambil dua parameter, yaitu image (gambar yang akan disimpan) dan path (lokasi tempat gambar akan disimpan). try: Ini adalah blok try, yang digunakan untuk mengeksekusi potongan kode di dalamnya. Dalam konteks ini, kode di dalam try adalah image.save(path).
image.save(path) Ini adalah metode dari objek gambar yang digunakan untuk menyimpan gambar ke lokasi yang ditentukan oleh path. Fungsi ini diguakan  untuk menyimpan gambar ke lokasi yang diberikan. except IOError: Jika terjadi kesalahan saat  menyimpan gambar, blok except akan menangkap kesalahan dengan tipe IOError. IOError umumnya terjadi ketika ada masalah dengan operasi input/output, seperti gagal membuka atau menulis ke file. print("Gagal menyimpan gambar!") kode ini di gunakan untuk jika terjadi kesalahan (IOError), maka pesan "Gagal menyimpan gambar!" akan dicetak ke konsol. Ini adalah cara memberikan informasi kepada pengguna bahwa ada masalah dalam menyimpan gambar.
>
H.	Daftar menu 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/b4177549-848b-415f-93ab-8b9b853f635c)

<h5 align="center"> Gambar 3.8 Dafrtar menu   </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan :

print("1. Buka gambar")  Kode ini di gunakan untuk  mencetak teks "1. Buka gambar" ke konsol. Ini adalah pilihan menu pertama yang menunjukkan opsi untuk membuka sebuah gambar. print("2. Potong gambar") Kode ini di gunakan untuk  mencetak teks "2. Potong gambar" ke konsol. Ini adalah pilihan menu kedua yang  menunjukkan opsi untuk melakukan operasi pemotongan pada gambar. print("3. Ubah ukuran gambar") Kode Ini di gunakan untuk  mencetak teks "3. Ubah ukuran gambar" ke konsol. Ini adalah pilihan menu ketiga yang  menunjukkan opsi untuk mengubah ukuran gambar. print("4. Simpan gambar") Kode ini di gunakan untuk  mencetak teks "4. Simpan gambar" ke konsol. Ini adalah pilihan menu keempat yang  menunjukkan opsi untuk menyimpan gambar. print("5. Keluar") Kode ini di gunakan untuk  mencetak teks "5. Keluar" ke konsol. Ini adalah pilihan menu kelima yang menunjukkan opsi untuk keluar dari program atau aplikasi.
Jadi, secara keseluruhan, kode ini adalah bagian dari antarmuka pengguna teks yang memberikan beberapa opsi kepada pengguna, seperti membuka gambar, melakukan operasi pemotongan, mengubah ukuran gambar, menyimpan gambar, dan keluar dari program.
>
I.	Membuka gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/5be78f3a-f54b-454b-ba0e-e41ee394ff6a)

<h5 align="center">Gambar 3.9 Membuka gambar  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
  
image = None: Inisialisasi variabel image dengan None. Ini menandakan bahwa pada awalnya tidak ada gambar yang dibuka. while True:: Membuat loop tak terbatas, yang berarti program akan terus berjalan sampai ada suatu kondisi untuk menghentikannya. pilihan = input("Pilih menu (1-5): "): Mengambil input dari pengguna berupa pilihan menu, yang disimpan dalam variabel pilihan. if pilihan == "1":: Menggunakan kondisi if untuk mengecek apakah pengguna memilih menu nomor 1, yaitu "Membuka gambar".
Di dalam blok if pilihan == "1":, terdapat kode untuk membaca path gambar dari pengguna (path = input("Masukkan path gambar: ")) dan kemudian memanggil fungsi open_image(path) untuk membuka gambar. Jika gambar berhasil dibuka (nilai yang tidak None), program mencetak pesan bahwa gambar telah dibuka dan memanggil fungsi show_image(image) untuk menampilkan gambar tersebut. Jika gambar tidak berhasil dibuka, program menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop, meminta pengguna untuk memilih menu kembali.
>
J.	 Kode memotong gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/50bd7c4d-1e4d-41ac-a722-792713ab5117)

<h5 align="center"> 3.10 Kode memotong gambar   </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
  
elif pilihan == "2":  Ini adalah bagian dari struktur pengkondisian yang mengecek apakah input pengguna (pilihan) sama dengan string "2". Jika ya, ini berarti pengguna memilih opsi untuk "Memotong gambar". # Memotong gambar: Ini adalah komentar yang memberikan deskripsi singkat tentang apa yang dilakukan oleh blok kode berikutnya. Dalam bahasa Inggris, artinya "Memotong gambar." if image: Kondisi ini memeriksa apakah variabel image telah diassign sebuah nilai selain None (yaitu, apakah suatu gambar telah dibuka atau dimuat). Jika image tidak None, ini berarti ada gambar untuk diproses, dan blok kode di dalam if akan dieksekusi.
Di dalam blok if image:, kode meminta pengguna untuk memasukkan empat nilai yang mewakili batas pemotongan:
top: Batas atas area pemotongan.
left: Batas kiri area pemotongan.
bottom: Batas bawah area pemotongan.
right: Batas kanan area pemotongan. 
Nilai-nilai ini diperoleh menggunakan input() dan diubah menjadi bilangan bulat menggunakan int(input(...)).>

K.	Kode untuk Verifikasi 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/eaafc1ad-c956-4b3d-9436-ba144da2bbe8)


<h5 align="center">Gambar 3.11 Kode verifikasi  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
  
if top < bottom and left < right and 0 <= top < image.height and 0 <= left < image.width: adalah kondisi yang memeriksa apakah batas koordinat yang dimasukkan oleh pengguna valid. Kondisi ini memastikan bahwa top kurang dari bottom, left kurang dari right, dan bahwa nilai top dan left berada dalam rentang yang valid sesuai dengan ukuran gambar (image.height dan image.width). Di dalam blok if, jika batas koordinat valid, maka dilakukan pemotongan gambar dengan memanggil fungsi crop_image(image, top, left, bottom, right). Hasilnya disimpan dalam variabel cropped_image.
if cropped_image: Kondisi ini memeriksa apakah operasi pemotongan gambar berhasil, yaitu cropped_image tidak None. Jika berhasil, program mencetak pesan "Gambar berhasil dipotong!", mengupdate variabel image dengan gambar yang telah dipotong, dan menampilkan gambar yang baru.
Jika operasi pemotongan gambar tidak berhasil (nilai cropped_image adalah None), maka program menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop.
Jika batas koordinat tidak valid, program mencetak pesan "Batas koordinat tidak valid!" dan menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop. Jika tidak ada gambar yang dibuka sebelumnya (image adalah None), program mencetak pesan "Buka gambar terlebih dahulu!" dan menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop.
>

L. Kode untuk mengubah gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/1a1839c4-c371-408a-b8fc-a12aa60556b9)


<h5 align="center">Gambar 3.12 Kode untuk mengubah gambar   </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan Kode :
  
elif pilihan == "3": Ini adalah bagian dari struktur pengkondisian yang mengecek apakah input pengguna (pilihan) sama dengan string "3". Jika ya, ini berarti pengguna memilih opsi untuk "Mengubah ukuran gambar". if image: Kondisi ini memeriksa apakah variabel image sudah di-assign nilai (yaitu, apakah gambar sudah dibuka atau dimuat). Jika ya, blok kode di dalamnya akan dieksekusi. Di dalam blok if image:, program meminta pengguna untuk memasukkan lebar dan tinggi baru untuk gambar, menggunakan input() untuk mengambil nilai lebar dan tinggi baru, dan mengonversinya menjadi bilangan bulat menggunakan int(input(...)).
resized_image = resize_image(image, width, height): Program memanggil fungsi resize_image dengan parameter gambar (image), lebar baru, dan tinggi baru. Hasilnya disimpan dalam variabel resized_image. if resized_image:: Kondisi ini memeriksa apakah operasi perubahan ukuran gambar berhasil, yaitu apakah resized_image tidak None. Jika berhasil, program mencetak pesan "Gambar berhasil diubah ukuran!", mengganti variabel image dengan gambar yang telah diubah ukurannya, dan menampilkan gambar yang baru. Jika operasi perubahan ukuran gambar tidak berhasil (nilai resized_image adalah None), program menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop. Jika tidak ada gambar yang dibuka sebelumnya (image adalah None), program mencetak pesan "Buka gambar terlebih dahulu!" dan menggunakan continue untuk melanjutkan ke iterasi berikutnya dari loop.>

M. Kode menyimpan gambar 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/14891e34-e144-4eb5-ae22-d6c554ba086a)

<h5 align="center">Gambar 3.13 Kode untuk menyimpan gambar    </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode :
elif pilihan == "4":: Ini adalah bagian dari struktur pengkondisian yang mengecek apakah input pengguna (pilihan) sama dengan string "4". Jika ya, ini berarti pengguna memilih opsi untuk "Menyimpan gambar". # Menyimpan gambar: Ini adalah komentar yang memberikan deskripsi singkat tentang apa yang dilakukan oleh blok kode berikutnya. Dalam bahasa Inggris, artinya "Save the image." if image:: Kondisi ini memeriksa apakah variabel image sudah di-assign nilai (yaitu, apakah gambar sudah dibuka atau dimuat). Jika ya, blok kode di dalamnya akan dieksekusi. Di dalam blok if image:, program meminta pengguna untuk memasukkan path (lokasi) untuk menyimpan gambar yang sedang diolah, menggunakan input() untuk mengambil nilai path.
save_image(image, path): Program memanggil fungsi save_image dengan parameter gambar (image) dan path untuk menyimpan (path). Fungsi ini mencoba menyimpan gambar ke lokasi yang ditentukan.Setelah menyimpan gambar, program mencetak pesan "Gambar berhasil disimpan!". Jika tidak ada gambar yang dibuka sebelumnya (image adalah None), program mencetak pesan "Buka gambar terlebih dahulu!"
>
N. Kode untuk pilihan 5 (keluar)
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/3c2f03b2-ce75-4d9c-9c26-5a3233b1c937)


<h5 align="center">Gambar 3.14 Kode untuk pilihan 5 (Keluar)   </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan kode: 
  
elif pilihan == "5":: Ini adalah bagian dari struktur pengkondisian yang mengecek apakah input pengguna (pilihan) sama dengan string "5". Jika ya, ini berarti pengguna memilih opsi untuk keluar dari program. Di dalam blok ini, program mencetak pesan "Terima kasih telah menggunakan program pengeditan gambar Kami!" untuk memberikan umpan balik kepada pengguna bahwa mereka telah keluar dari program. Selanjutnya, pernyataan break digunakan untuk menghentikan loop tak terbatas (while True) dan keluar dari program.
Jika pilihan pengguna tidak sama dengan "5", maka eksekusi akan masuk ke bagian else: Di bagian else, program mencetak pesan "Pilihan tidak valid!" untuk memberi tahu pengguna bahwa pilihan yang dimasukkan tidak sesuai dengan opsi yang valid. Setelah mencetak pesan ini, program akan kembali ke awal loop dan meminta pengguna untuk memilih kembali.
>
O. Output (luaran) dari Program 
<div align="center">

![image](https://github.com/chindyfebyamara/tugass/assets/145527919/132e5f67-4aee-4a00-9f24-2b32f6c8d85b)

<h5 align="center">Gambar 3.15 Output Program  </h5> 

<div align="justify">
<align="justify" style="font-weight: normal;">
Penjelasan :
  
Buka gambar (Menu 1): Pengguna dapat memilih opsi ini untuk membuka sebuah gambar. Setelah memilih opsi ini, program akan meminta pengguna untuk memasukkan path (lokasi) gambar yang ingin dibuka.
Potong gambar (Menu 2): Jika pengguna memilih opsi ini, program akan memeriksa apakah sudah ada gambar yang dibuka sebelumnya. Jika ya, program akan meminta pengguna untuk memasukkan batas-batas pemotongan gambar, seperti batas atas, kiri, bawah, dan kanan. Setelah itu, program akan memanggil fungsi crop_image (yang harus didefinisikan di dalam kode program) untuk melakukan pemotongan gambar sesuai dengan batas yang dimasukkan.
Ubah ukuran gambar (Menu 3): Opsi ini  pengguna mengubah ukuran gambar. Jika sudah ada gambar yang dibuka, program akan meminta pengguna untuk memasukkan lebar dan tinggi baru untuk gambar. Setelah itu, program akan memanggil fungsi resize_image (juga harus didefinisikan di dalam kode program) untuk mengubah ukuran gambar.
Simpan gambar (Menu 4): Jika pengguna memilih opsi ini, program akan memeriksa apakah sudah ada gambar yang dibuka. Jika ya, program akan meminta pengguna untuk memasukkan path (lokasi) di mana gambar akan disimpan. Kemudian, program akan memanggil fungsi save_image (harus didefinisikan) untuk menyimpan gambar ke lokasi yang dimasukkan.
Keluar (Menu 5): Jika pengguna memilih opsi ini, program akan mencetak pesan selamat tinggal dan keluar dari program.
>


| INPUT  | OUTPUT|
| :------------|:-|
| 1. Buka gambar | <img src="https://github.com/chindyfebyamara/tugass/assets/145527919/e8b4508f-30c4-4c76-8fb5-2d42821d4d97" alt="image" width="35%" />|
| 2. Potong gambar | <img src="https://github.com/chindyfebyamara/tugass/assets/145527919/55274426-d27c-4267-a2cc-92f5dfc9c8e8" alt="image" style="width: 35%;" />|
| 3. ubah ukuran gambar | <img src="https://github.com/chindyfebyamara/tugass/assets/145527919/2dddcc6f-39ef-4cd8-9601-dd2ac95739d9" alt="image" style="width: 35%;" />|
| 4. simpan gambar | <img src="https://github.com/chindyfebyamara/tugass/assets/145527919/f4c2dddf-fcb4-4b72-b1de-ba45a492c6dc" alt="image" style="width: 35%;" />|
| 5. keluar | <img src="https://github.com/chindyfebyamara/tugass/assets/145527919/2babf316-cb57-40b1-bf46-d342136cd01e" alt="image" style="width: 35%;" />|

