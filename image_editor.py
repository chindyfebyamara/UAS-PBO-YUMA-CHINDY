from PIL import Image
import matplotlib.pyplot as plt

# Fungsi untuk membuka dan menampilkan gambar
def open_image(path):
  try:
    image = Image.open(path)
    return image
  except IOError:
    print("File tidak ditemukan!")

# Fungsi untuk menampilkan gambar
def show_image(image):
  if image:
    plt.imshow(image)
    plt.show()

# Fungsi untuk memotong gambar
def crop_image(image, top, left, bottom, right):
  try:
    cropped_image = image.crop((left, top, right, bottom)) 
    return cropped_image
  except ValueError:
    print("Batas koordinat tidak valid!")

# Fungsi untuk mengubah ukuran gambar
def resize_image(image, width, height):
  try:
    resized_image = image.resize((width, height))
    return resized_image
  except ValueError:
    print("Ukuran tidak valid!")

# Fungsi untuk menyimpan gambar
def save_image(image, path):
  try:
    image.save(path)
  except IOError:
    print("Gagal menyimpan gambar!")

# Menu utama
print("Selamat datang di program pengeditan gambar!")
print("1. Buka gambar")
print("2. Potong gambar")
print("3. Ubah ukuran gambar")
print("4. Simpan gambar")
print("5. Keluar")

# Deklarasi variabel image di luar loop
image = None

# Di dalam loop, setelah membuka atau mengedit gambar, tambahkan pemanggilan fungsi show_image
while True:
  pilihan = input("Pilih menu (1-5): ")

  if pilihan == "1":
    # Membuka gambar
    path = input("Masukkan path gambar: ")
    image = open_image(path)
    if image:
      print(f"Gambar dibuka: {path}")
      show_image(image)
    else:
      continue

  elif pilihan == "2":
    # Memotong gambar
    if image:
      top = int(input("Masukkan batas atas: "))
      left = int(input("Masukkan batas kiri: "))
      bottom = int(input("Masukkan batas bawah: "))
      right = int(input("Masukkan batas kanan: "))
      
      # Verifikasi batas-batas yang valid
      if top < bottom and left < right and 0 <= top < image.height and 0 <= left < image.width:
        cropped_image = crop_image(image, top, left, bottom, right)
        if cropped_image:
          print("Gambar berhasil dipotong!")
          image = cropped_image
          show_image(image)
        else:
          continue
      else:
        print("Batas koordinat tidak valid!")
        continue
    else:
      print("Buka gambar terlebih dahulu!")

  elif pilihan == "3":
    # Mengubah ukuran gambar
    if image:
      width = int(input("Masukkan lebar baru: "))
      height = int(input("Masukkan tinggi baru: "))
      resized_image = resize_image(image, width, height)
      if resized_image:
        print("Gambar berhasil diubah ukuran!")
        image = resized_image
        show_image(image)
      else:
        continue
    else:
      print("Buka gambar terlebih dahulu!")

  elif pilihan == "4":
    # Menyimpan gambar
    if image:
      path = input("Masukkan path untuk menyimpan: ")
      save_image(image, path)
      print("Gambar berhasil disimpan!")
    else:
      print("Buka gambar terlebih dahulu!")

  elif pilihan == "5":
    print("Terima kasih telah menggunakan program pengeditan gambar Kami!")
    break

  else:
    print("Pilihan tidak valid!")
