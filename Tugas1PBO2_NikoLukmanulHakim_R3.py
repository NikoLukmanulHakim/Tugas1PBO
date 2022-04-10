import psycopg2 as psy
#Connect Database
db = psy.connect(
         host="localhost",
         database="universitas",
         user="niko",
         password="123")

#Menyimpan Data Baru
def insert_data(db):
   idmhs = int(input("Masukan ID Mahasiswa: "))
   nim = input("Masukan NIM Mahasiswa: ")
   nama = input("Masukan Nama Mahasiswa: ")
   idfakultas = int(input("Masukan ID Fakultas Mahasiswa: "))
   idprodi = int(input("Masukan ID Prodi: "))
   val = (idmhs,nim,nama,idfakultas,idprodi)
   sql = "INSERT INTO mahasiswa (idmhs, nim, nama, idfakultas, idprodi) VALUES (%s, %s, %s, %s, %s)"
   curs = db.cursor()
   curs.execute(sql, val)
   db.commit()
   print("==================================")
   print("{} Data Berhasil Disimpan".format(curs.rowcount))

#Menampilkan Data
def show_data(db):
   curs = db.cursor()
   sql = "SELECT * FROM mahasiswa"
   curs.execute(sql)
   result = curs.fetchall()

   if curs.rowcount < 0:
      print("==================================")
      print("DATA TIDAK ADA ATAU BELUM TERISI")
   else:
      print("==================================")
      print("{} DATA BERHASIL DITEMUKAN".format(curs.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(db):
   curs = db.cursor()
   show_data(db)
   idmhs = input("Pilih ID Mahasiswa: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   nama = input("Masukan Nama Mahasiswa Yang Baru: ")
   idfakultas = int(input("Masukan Id Fakultas yang Baru: "))
   idprodi = int(input("Masukan Id Prodi Yang Baru: "))
   sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE idmhs=%s"
   val = (nim, nama, idfakultas, idprodi, idmhs)
   curs.execute(sql, val)
   db.commit()
   print("==================================")
   print("{} Data Berhasil Diupdate".format(curs.rowcount))

#Menghapus Data
def delete_data(db):
   curs = db.cursor()
   show_data(db)
   idmhs = str(input("Pilih ID Mahasiswa Yang Akan Dihapus: "))
   slc = "SELECT * FROM mahasiswa WHERE idmhs= %s"
   val = (idmhs)
   curs.execute(slc, val)
   con = curs.rowcount
   if (con == 1):
      inp = input("Apakah Anda Yakin Ingin Menghapus Data Tersebut? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
         val = (idmhs)
         curs.execute(sql, val)
         db.commit()
         print("==================================")
         print("{} DATA BERHASIL DIHAPUS".format(curs.rowcount))
      else:
         print("DATA BATAL DIHAPUS")
   else:
      print("TIDAK ADA ID YANG DIMAKSUD")

#Mencari Data
def search_data(db):
   curs = db.cursor()
   keyword = input("MASUKAN NIM ATAU NAMA DATA YANG DICARI: ")
   sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   curs.execute(sql, val)
   result = curs.fetchall()

   if curs.rowcount <= 0:
      print("==================================")
      print("TIDAK ADA DATA YANG DITEMUKAN")
   else:
      print("==================================")
      print("{} DATA BERHASIL DITEMUKAN".format(curs.rowcount))
      for data in result:
         print(data)

#Menampilkan Menu
def show_menu(db):
   print("============================================")
   print("==== TUGAS 1 PEMBUATAN CRUD MELALUI CLI ====")
   print("== DIBUAT OLEH NIKO LUKMANUL HAKIM ==")
   print("== DARI KELAS R3 ==")
   print("============================================")
   print("1. Tambah Data")
   print("2. Menampilkan Data")
   print("3. Update Data")  
   print("4. Menghapus Data")
   print("5. Mencari Data")
   print("0. Keluar")
   print("------------------")
   pilihan = input("Pilih Menu: ")

   if pilihan == "1":
      insert_data(db)
   elif pilihan == "2":
      show_data(db)
   elif pilihan == "3":
      update_data(db)
   elif pilihan == "4":
      delete_data(db)
   elif pilihan == "5":
      search_data(db)
   elif pilihan == "0":
      exit()
   else:
      print("Menu salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(db)

#Niko Lukmanul Hakim
#200511120
#R3