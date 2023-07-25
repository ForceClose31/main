import pandas as pd
import csv
import os
import requests

            
def daftar() :
    global username
    global status
    global datalogin
    os.system('cls')
    print(50*'=')
    print("DAFTAR AKUN".center(50))
    print(50*'=')
    nama =(input("Masukkan Nama : "))
    username = (input("Masukkan Username : "))
    password=(input("Masukkan Password: "))
    status="user"
    datalogin=username
    re_pass=(input("Masukkan Kembali Password: "))
    df = pd.read_csv('login.csv')
    for line in df :
        item = line.split(',')    
    if username == item[0] :
        print ('\n')
        print ('USERNAME SUDAH DIGUNAKAN')
        input ('ENTER UNTUK MENGULANG PENDAFTARAN')
    elif re_pass != password :
        print ('\n')
        print ('PASSWORD TIDAK SAMA')
        input ('ENTER UNTUK MENGULANG PENDAFTARAN')  
    else :
        df.loc[-1] = (nama, username, password,status )  
        df.to_csv('login.csv', index=False)
        print ('\n')
        print ('PENDAFTARAN BERHASIL')
        input ('ENTER UNTUK MASUK')
        masuk()

def masuk():
    os.system('cls')
    print(50*'=')
    print("MASUK".center(50))
    print(50*'=')
    username=(input("Masukkan Username : "))
    password =(input("Masukkan Password : "))
    global datalogin
    file = open('login.csv', 'r')
    index = 0
    for line in file:
        item = line.split(',')
        if username == item[1] and password == item[2]:
            datalogin = username
            os.system('cls')
            print ('BERHASIL MASUK')
            input ('ENTER UNTUK MELANJUTKAN')
            if item[3].strip() == "user" :
                tampilan()
        elif line[0:4] == 'nama':
            print('')
        elif username != item[1] and password != item[2]:
            print('BELUM ADA AKUN TERDAFTAR, SILAHKAN DAFTAR TERLEBIH DAHULU')
            input()
        index += 1

def tampilanawal():
    os.system("cls")
    print(f"""
    {50*"="}
    |{"AGROBOT".center(48)}|
    {50*"="}
    |{" Apakah anda sudah memiliki akun :".ljust(48)}|
    |{" ".center(48)}|
    |{" 1. Masuk".ljust(48)}|
    |{" 2. Daftar".ljust(48)}|
    |{" ".center(48)}|
    |{" 3. EXIT".ljust(48)}|
    {50*"="}
    """)
    opsi = int(input("Pilih opsi : "))
    if opsi == 1:
        masuk()
    elif opsi == 2:
        daftar()
    elif opsi == 3:
        exit()
        
def tampilan():
    os.system("cls")
    print(f"""
    {50*"="}
    |{"AGROBOT".center(48)}|
    {50*"="}
    |{" Option :".ljust(48)}|
    |{" ".center(48)}|
    |{" 1. Lahan".ljust(48)}|
    |{" 2. Bibit".ljust(48)}|
    |{" 3. Cuaca".ljust(48)}|
    |{" 4. Wikipedia Agrobot".ljust(48)}|
    |{" ".center(48)}|
    |{" 5. EXIT".ljust(48)}|
    {50*"="}
    """)
    opsi = int(input("Pilih opsi : "))
    if opsi == 1:
        opsiLahan()
    elif opsi == 2:
        opsiBenih()
    elif opsi == 3 :
        ramalan()
    elif opsi == 4 :
        wikipedia()
    elif opsi == 5 :
        exit()

# FITUR KEMBALI KE TAMPILAN HOME
def back():
    input("Tekan enter untuk kembali...")
    tampilan()

# FITUR OPSI LAHAN
def opsiLahan():
    os.system("cls")
    print(f"""
    {50*"="}
    |{"AGROBOT".center(48)}|
    {50*"="}
    |{" Option :".ljust(48)}|
    |{" ".center(48)}|
    |{" 1. Input Luas Lahan".ljust(48)}|
    |{" 2. Informasi Lahan".ljust(48)}|
    |{" 3. Hapus Data Lahan".ljust(48)}|
    |{" ".center(48)}|
    |{" 4. BACK".ljust(48)}|
    {50*"="}
    """)
    opsi = int(input("Pilih opsi : "))
    if opsi == 1:
        lahan()
    elif opsi == 2:
        infoLahan()
    elif opsi == 3:
        delete_lahan()
    elif opsi == 4:
        tampilan()   

# FITUR LAHAN 1 (CREATE LAHAN)
def lahan():
    os.system("cls")
    listLahan = []
    with open("dataLahan.csv", mode="r") as informasiLahan:
        reader = csv.DictReader(informasiLahan)
        for row in reader:
            listLahan.append(row)
    with open("dataLahan.csv", mode='a',newline='') as dataLahan:
        fieldnames = ['kode', 'luas', 'lokasi', 'populasi']
        writer = csv.DictWriter(dataLahan, fieldnames=fieldnames)
        
        kode = int(input("Kode Lahan: "))
        luasLahan = int(input("Luas Lahan: "))
        jarakTanam = int(input("Jarak Tanam: "))
        lokasi = input("Lokasi Lahan : ")
        populasi = luasLahan * jarakTanam
        for data in listLahan:
            if kode == int(data['kode']):
                print(f"Data dengan Kode Lahan {kode} sudah ada")
                input("silahkan masukkan Kode Lahan setelahnya..")
                lahan()
        writer.writerow({'kode': kode, 'luas': luasLahan, 'lokasi': lokasi, 'populasi' : populasi})    
        print("Berhasil disimpan!")
    back()

# FITUR LAHAN 2 (READ LAHAN)
def infoLahan():
    os.system("cls")
    listLahan = []
    with open("dataLahan.csv", mode="r") as informasiLahan:
        reader = csv.DictReader(informasiLahan)
        for row in reader:
            listLahan.append(row)
    jumlahLahan = sum(1 for row in listLahan)
    print("=" * 50)
    print("INFORMASI LAHAN".center(48))
    print("=" * 50)

    print("Kode \t Luas(ha) \t\t Lokasi \t Populasi")
    print("-" * 50)
    for data in listLahan:
        print(f"{data['kode']} \t {data['luas']} \t\t {data['lokasi']} \t {data['populasi']}")
    print("=" * 50)
    print("Total Lahan: ",jumlahLahan)
    print("=" * 50)
    back()

#  FITUR LAHAN 3 (DELETE LAHAN)
def delete_lahan():
    os.system("cls")
    lahan = []

    with open("dataLahan.csv", mode="r") as delete:
        csv_reader = csv.DictReader(delete)
        for row in csv_reader:
            lahan.append(row)

    print("Kode \t Luas \t\t Lokasi \t Populasi")
    print("-" * 55)

    for data in lahan:
        print(f"{data['kode']} \t {data['luas']} \t {data['lokasi']} \t {data['populasi']}")

    print("-----------------------")
    kode = int(input("Hapus lahan dengan kode : "))

    indeks = 0
    for data in lahan:
        if int(data['kode']) == kode:
            lahan.remove(lahan[indeks])
        indeks += 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open("dataLahan.csv", mode="w") as delete:
        fieldnames = ['kode', 'luas', 'lokasi', 'populasi']
        writer = csv.DictWriter(delete, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in lahan:
            writer.writerow({'kode': new_data['kode'], 'luas': new_data['luas'], 'lokasi': new_data['lokasi'], 'populasi': new_data['populasi']}) 

    print("Data sudah terhapus")
    back()

# FITUR OPSI BENIH
def opsiBenih():
    os.system("cls")
    print(f"""
    {50*"="}
    |{"AGROBOT".center(48)}|
    {50*"="}
    |{" Option :".ljust(48)}|
    |{" ".center(48)}|
    |{" 1. Daftar Benih".ljust(48)}|
    |{" 2. Tambah Benih".ljust(48)}|
    |{" 3. Hapus Benih".ljust(48)}|
    |{" 4. Search Benih".ljust(48)}|
    |{" ".center(48)}|
    |{" 5. BACK".ljust(48)}|
    {50*"="}
    """)
    opsi = int(input("Pilih opsi : "))
    if opsi == 1:
        daftarBenih()
    elif opsi == 2:
        tambahBenih()
    elif opsi == 3:
        delete_benih()
    elif opsi == 4:
        search_barang()
    elif opsi == 5:
        tampilan() 

# FITUR BENIH 1 (DAFTAR BENIH)
def daftarBenih():
    os.system("cls")
    listbenih = []
    with open("dataBenih.csv", mode="r") as dataBenih:
        reader = csv.DictReader(dataBenih)
        for row in reader:
            listbenih.append(row)
    jumlahbenih = sum(1 for row in listbenih)
    print("=" * 50)
    print("INFORMASI DAFTAR BENIH".center(48))
    print("=" * 50)

    print("Nama \t\t Berat (gram) \t\t Harga")
    print("-" * 50)
    for data in listbenih:
        if len(data['nama']) <= 6 :
            print(f"{data['nama']} \t\t {data['berat']} \t\t\t Rp.{data['harga']}")
        elif len(data['nama']) > 6 :
            print(f"{data['nama']} \t {data['berat']} \t\t\t Rp.{data['harga']}")
    print("=" * 50)
    print("Total Benih: ",jumlahbenih)
    print("=" * 50)
    back()

# FITUR BENIH 2 (UPDATE BENIH)
def tambahBenih():
    os.system("cls")
    listBenih = []
    with open("dataBenih.csv", mode="r") as dataBenih:
        reader = csv.DictReader(dataBenih)
        for row in reader:
            listBenih.append(row)
    with open("dataBenih.csv", mode='a',newline='') as dataLahan:
        fieldnames = ['nama', 'berat', 'harga']
        writer = csv.DictWriter(dataLahan, fieldnames=fieldnames)
        
        nama = input("Nama Benih: ")
        berat = int(input("Berat Benih: "))
        harga = int(input("Harga Benih : "))
        for data in listBenih:
            if nama == data['nama']:
                print(f"Data dengan nama {nama} sudah ada")
                input("silahkan masukkan daftar benih lain..")
                tambahBenih()
        writer.writerow({'nama': nama, 'berat': berat, 'harga': harga})    
        print("Berhasil disimpan!")
    back()

# FITUR BENIH 3 (DELETE BENIH)
def delete_benih():
    os.system("cls")
    benih = []

    with open("dataBenih.csv", mode="r") as delete:
        csv_reader = csv.DictReader(delete)
        for row in csv_reader:
            benih.append(row)

    print("Nama \t\t Berat (gram) \t\t Harga")
    print("-" * 55)

    for data in benih:
        if len(data['nama']) <= 6 :
            print(f"{data['nama']} \t\t {data['berat']} \t\t\t Rp.{data['harga']}")
        elif len(data['nama']) > 6 :
            print(f"{data['nama']} \t {data['berat']} \t\t\t Rp.{data['harga']}")

    print(20*"=")
    nama = input("Hapus benih dengan nama : ")
    indeks = 0
    for data in benih:
        if data['nama'] == nama:
            benih.remove(benih[indeks])
        indeks += 1
    with open("dataBenih.csv", mode="w") as delete:
        fieldnames = ['nama', 'berat', 'harga']
        writer = csv.DictWriter(delete, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in benih:
            writer.writerow({'nama': new_data['nama'], 'berat': new_data['berat'], 'harga': new_data['harga']}) 

    print("Data sudah terhapus")
    back()

# FITUR BENIH 4 (SEARCH BENIH)
def search_barang():
    os.system("cls")
    Barang = []
    with open("dataBenih.csv", mode="r") as benih:
        reader = csv.DictReader(benih)
        for row in reader:
            Barang.append(row)

    nama = input("Cari bibit ")

    data_found = []
    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['nama'] == nama):
            data_found = Barang[indeks]
            
        indeks += 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['nama']}")
        print(f"Berat: {data_found['berat']} gram")
        print(f"Harga : Rp. {data_found['harga']}")
    else:
        print("Data tidak ditemukan")
    back()

# FITUR CUACA
def ramalan():
    os.system("cls")
    kota = input("Masukkan lokasi kota : ")
    url = 'https://wttr.in/{}'.format(kota)
    res = requests.get(url)
    print(res.text)
    back()

# FITUR WIKIPEDIA
def wikipedia():
    os.system("cls")
    print(f"""
    {50*"="}
    |{"AGROBOT".center(48)}|
    {50*"="}
    |{" Option :".ljust(48)}|
    |{" ".center(48)}|
    |{" 1. Informasi Benih".ljust(48)}|
    |{" 2. Tambah Informasi Benih".ljust(48)}|
    |{" 3. Hapus Informasi Benih".ljust(48)}|
    |{" 4. Informasi Penyakit".ljust(48)}|
    |{" ".center(48)}|
    |{" 5. BACK".ljust(48)}|
    {50*"="}
    """)
    opsi = int(input("Pilih opsi : "))
    if opsi == 1:
        infoBenih()
    elif opsi == 2:
        tambahinfobenih()
    elif opsi == 3:
        deleteinfoBenih()
    elif opsi == 4:
        penyakitBenih()
    elif opsi == 5:
        tampilan()       

# FITUR INFORMASI BENIH 1 (READ INFORMASI BENIH)
def infoBenih():
    os.system("cls")
    databenih = []
    with open("infoBenih.csv", mode="r") as informasibenih:
        reader = csv.DictReader(informasibenih)
        for row in reader:
            databenih.append(row)
    print("=" * 50)
    print("INFORMASI BENIH".center(48))
    print("=" * 50)
    print("Kode  Jenis")
    print("-" * 50)
    for data in databenih:
        if int(data['kode']) < 10 :
            print(f"{data['kode']}   {data['jenis']}")
        elif int(data['kode']) > 9 :
            print(f"{data['kode']}  {data['jenis']}")
        elif int(data['kode']) > 99 :
            print(f"{data['kode']} {data['jenis']}")
    print("=" * 50)
    informasi = int(input("Masukkan kode : "))
    informasibenih = []
    with open("datainfoBenih.csv", mode="r") as datainfobenih:
        reader_2 = csv.DictReader(datainfobenih)
        for row in reader_2:
            informasibenih.append(row)
    for data in informasibenih:
        if informasi == int(data['kode']):
            print(f"""
            Nama Benih          : {data['jenis']}
            Tipe Perkecambahan  : {data['perkecambahan']}
            Tipe Dormansi       : {data['dormansi']}
            Daya Tumbuh         : {data['daya']}
            """)
    back()

# FITUR INFORMASI BENIH 2 (ADD INFORMASI BENIH)
def tambahinfobenih():
    os.system("cls")
    listinfobenih = []
    with open("datainfoBenih.csv", mode="r") as datainfoBenih:
        reader = csv.DictReader(datainfoBenih)
        for row in reader:
            listinfobenih.append(row)
    with open("datainfoBenih.csv", mode='a',newline='') as datainfoBenih:
        fieldnames = ['kode','jenis','perkecambahan','dormansi','daya']
        writer = csv.DictWriter(datainfoBenih, fieldnames=fieldnames)
        
        kode = int(input("Kode Benih: "))
        jenis = input("Jenis Benih: ")
        perkecambahan = input("Tipe Perkecambahan Benih : ")
        dormansi = input("Tipe Dormansi Benih : ")
        daya = input("Daya Tumbuh : ")

        for data in listinfobenih:
            if kode == int(data['kode']):
                print(f"Data dengan Kode Benih {kode} sudah ada")
                input("silahkan masukkan kode benih lain..")
                tambahinfobenih()
        writer.writerow({'kode': kode, 'jenis': jenis, 'perkecambahan': perkecambahan, 'dormansi' : dormansi, 'daya' : daya})
        with open("infoBenih.csv", mode='a',newline='') as infoBenih:
            fieldnames = ['kode','jenis']
            writer = csv.DictWriter(infoBenih, fieldnames=fieldnames)
            writer.writerow({'kode': kode, 'jenis': jenis})
        
        print("Berhasil disimpan!")
    back()

# FITUR INFORMASI BENIH 3 (DELETE BENIH)
def deleteinfoBenih():
    os.system("cls")
    informasiBenih = []

    with open("datainfoBenih.csv", mode="r") as delete:
        csv_reader = csv.DictReader(delete)
        for row in csv_reader:
            informasiBenih.append(row)

    print("Kode \t Jenis \t\t Perkecambahan \t Dormansi \t Daya Tumbuh")
    print("-" * 70)

    for data in informasiBenih:
        if len(data['jenis']) < 6: 
            print(f"{data['kode']} \t {data['jenis']} \t\t {data['perkecambahan']} \t {data['dormansi']} \t {data['daya']}")
        elif len(data['jenis']) < 6 or len(data['dormansi']) < 6: 
            print(f"{data['kode']} \t {data['jenis']} \t {data['perkecambahan']} \t {data['dormansi']} \t\t {data['daya']}")
        elif len(data['jenis']) > 12:
            print(f"{data['kode']} \t {data['jenis']}  {data['perkecambahan']} \t {data['dormansi']} \t {data['daya']}")
        else:
            print(f"{data['kode']} \t {data['jenis']} \t {data['perkecambahan']} \t {data['dormansi']} \t {data['daya']}")
    print("-----------------------")
    kode = int(input("Hapus Informasi Benih dengan kode : "))

    indeks = 0
    for data in informasiBenih:
        if int(data['kode']) == kode:
            informasiBenih.remove(informasiBenih[indeks])
        indeks += 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open("datainfoBenih.csv", mode="w") as delete:
        fieldnames = ['kode', 'jenis', 'perkecambahan', 'dormansi', 'daya']
        writer = csv.DictWriter(delete, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in informasiBenih:
            writer.writerow({'kode': new_data['kode'], 'jenis': new_data['jenis'], 'perkecambahan': new_data['perkecambahan'], 'dormansi': new_data['dormansi'], 'daya' : new_data['daya']}) 
        with open("infoBenih.csv", mode="w") as delete:
            fieldnames = ['kode', 'jenis']
            writer = csv.DictWriter(delete, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in informasiBenih:
                writer.writerow({'kode': new_data['kode'], 'jenis': new_data['jenis']}) 

    print("Data sudah terhapus")
    back()

# FITUR INFORMASI PENYAKIT 4 (READ PENYAKIT BENIH)
def penyakitBenih():
    os.system("cls")
    penyakitbenih = []
    with open("penyakit.csv", mode="r") as penyakit:
        reader = csv.DictReader(penyakit)
        for row in reader:
            penyakitbenih.append(row)
    print("=" * 50)
    print("INFORMASI PENYAKIT BENIH".center(48))
    print("=" * 50)
    print("Kode  Jenis")
    print("-" * 50)
    for data in penyakitbenih:
        if int(data['kode']) < 10 :
            print(f"{data['kode']}   {data['jenis']}")
        elif int(data['kode']) > 9 :
            print(f"{data['kode']}  {data['jenis']}")
        elif int(data['kode']) > 99 :
            print(f"{data['kode']} {data['jenis']}")
    print("=" * 50)
    obat = int(input("Masukkan kode : "))
    perawatanbenih = []
    with open("perawatan.csv", mode="r") as perawatan:
        reader_2 = csv.DictReader(perawatan)
        for row in reader_2:
            perawatanbenih.append(row)
    for data in perawatanbenih:
        if obat == int(data['kode']):
            print(f"Perawatannya : {data['perawatan']} \r\n")
    back()  

def exit():
    print(20*"=","TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI","="*20)

tampilanawal()


