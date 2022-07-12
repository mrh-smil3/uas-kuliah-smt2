# Nama  : Muhammad Arif Hidayanto
# NIM   : 211240001205


import datetime
import time

now = datetime.datetime.now()
tanggal = now.date()
waktu = now.time()

d_nomor = {'00001':'00001','00002':'00002','00003':'00003'}
d_nama = {'00001':'anandito','00002':'bagas','00003':'zidan'}
d_kode = {'01':'01','02':'02','03':'03'}
d_barang = {'01':'Laptop','02':'Mouse','03':'Keyboard'}
d_pinjam = {'anandito':'Laptop','bagas':'Mouse','zidan':'Keyboard'}

d_barang2=[]
i=0
head = ('''
--------------------------------------------------------------------
            |       PROGRAM PEMINJAMAN BARANG       |               
            |   ---------------------------------   |
--------------------------------------------------------------------        
''')

def menu():
    print(head)
    print('''
                            - MENU -
                    __________________________
                        1. Data
                        2. Peminjaman Barang
                        3. Keluar
    ''')
    while True:
        pilih = input('Masukkan pilihan : ')
        if pilih=='1':
            data()
            break
        elif pilih=='2':
            peminjaman()
            break
        elif pilih=='3':
            break
        elif not pilih :
            print()
        else:
            print()

def peminjaman():
    print(head)
    print('''
                            - Peminjaman -
                    _______________________________
    ''')
    nip = input('Masukkan Nomor Induk Pegawai anda : ')
    print()
    print('Nama ==>',d_nama[nip])
    print()
    print('tekan q atau Q ketika sudah melakukan pinjaman')
    while True:
        kode = input('Masukkan kode barang : ')
        if kode == 'q' or kode == 'Q':
            print()
            print('''
            --------------------------------------------
                |       Cetak Bukti Peminjaman      |      
                |             DIVISI IT             |
            --------------------------------------------
            ''')
            print('Nama Peminjam : ',d_nama[nip])
            print('Barang yang dipinjam : ')
            for n in range(len(d_barang2)):
                n+1
                print('\t\t %s\t    \t\t'%(d_barang2[n]))
            print('___________________________________________________________')
            print('Total barang yang dipinjam :',len(d_barang2))
            print
            print('Barang dikembalikan dalam waktu 12 hari setelah peminjam')
            print('-----------------------------------------------------------')
            print('Tanggal. %s-%s-%s    %s:%s:%s'%(tanggal.day,tanggal.month,tanggal.year,waktu.hour,waktu.minute,waktu.second),'v.1.0')
            print('''
            ---------------------------------------------
                     JANGAN LUPA MENGEMBALIKAN          
            ---------------------------------------------
                ''')
            break
        elif kode ==d_kode[kode]:
            barang=d_barang[d_kode[kode]]
            d_barang2.append(barang)
            print('==>',d_barang[kode])
        else:
            print
    while True:
        tanya = input('lagi? y/t ==>')
        if tanya == 'y'or tanya =='Y':
            peminjaman()
            break
        else:
            if tanya == 't' or tanya=='T':
                menu()
                break
            else:
                print

# daftar anggota
def daftar():
    print('''
                - DAFTAR ANGGOTA PEMINJAM BARANG -
            ___________________________________________
    ''')
    print('NIP dan nama karyawan peminjam : ',d_nama)
    print('')

    while True:
        pilih = input ('Masukkan angka 1 untuk kembali : ')
        if pilih =='1':
            datauser()
            break
        else:
            print   
#tambah anggota
def tambah():
    print('''
                - TAMBAH ANGGOTA PEMINJAM BARANG -
            ___________________________________________
    ''')
    nomor= input ('Masukkan NIP karyawan : ')
    print('')
    nama = input ('Masukkan nama karyawan : ')
    print('')
    d_nomor[nomor]=nomor
    d_nama[nomor]=nama
    while True:
        tanya = input('lagi? y/t ==>')
        if tanya =='y' or tanya=='Y':
            tambah()
            break
        else: 
            if tanya =='t' or tanya=='T':
                datauser()
                break
            else:
                print

#hapus anggota
def hapus():
    print('''
                - HAPUS ANGGOTA PEMINJAM -
            ___________________________________
    ''')
    nomor= input ('Masukkan NIP Karyawan : ')
    print(' ==>',d_nama[nomor],'Telah dihapus')
    del d_nomor[nomor]
    del d_nama[nomor]
    print('')
    while True:
        tanya = input('lagi? y/t : ')
        if tanya == 'y' or tanya == 'Y':
            hapus()
            break
        else:
            if tanya == 't' or tanya== 'T':
                datauser()
                break
            else:
                print

def datauser():
    print('''
                - DATA PEMINJAM BARANG -
            _________________________________
                1. Daftar Anggota
                2. Tambah Anggota
                3. Hapus Anggota
                4. Kembali
        ''')
    while True:
        pilih = input ('Masukklah Pilihan : ')
        if pilih == '1':
            daftar()
            break
        else:
            if pilih == '2':
                tambah()
                break
            else:
                if pilih == '3':
                    hapus()
                    break
                else:
                    if pilih == '4':
                        data()
                        break
                    else:
                        print
#daftar barang
def daftarbarang():
    print('''
                - KODE BARANG -
            ______________________
    ''')
    print('Masukkan kode dan nama barang : ',d_barang)
    print('')

    while True:
        pilih = input ('Masukkan angka 1 untuk kembali : ')
        if pilih =='1':
            databarang()
            break
        else:
            print   

#tambah barang
def tambahbarang():
    print('''
                - TAMBAH BARANG -
            ___________________________
    ''')
    kode= input ('Masukkan kode barang : ')
    print('')
    barang= input('Masukkan nama barang : ')
    print('')
    d_kode[kode]=kode
    d_barang[kode]=barang
    while True:
        tanya = input('lagi? y/t ==>')
        if tanya =='y' or tanya=='Y':
            tambahbarang()
            break
        else:
            if tanya =='t' or tanya=='T':
                databarang()
                break
            else:
                print

#hapus barang
def hapusbarang():
    print('''
                - HAPUS BARANG -
            __________________________
    ''')
    kode = input ('Masukkan kode barang yang ingin dihapus : ')
    print(' ==>',d_barang[kode],'Telah dihapus')
    del d_kode[kode]
    del d_barang[kode]
    print('')
    while True:
        tanya = input('lagi? y/t : ')
        if tanya == 'y' or tanya == 'Y':
            hapusbarang()
            break
        else:
            if tanya == 't' or tanya== 'T':
                databarang()
                break
            else:
                print           
# data barang
def databarang():
    print('''
                - DATA BARANG -
            _________________________________
                1. Daftar barang
                2. Tambah barang
                3. Hapus barang
                4. Kembali
        ''')
    while True:
        pilih = input ('Masukklah Pilihan : ')
        if pilih == '1':
            daftarbarang()
            break
        else:
            if pilih == '2':
                tambahbarang()
                break
            else:
                if pilih == '3':
                    hapusbarang()
                    break
                else:
                    if pilih == '4':
                        data()
                        break
                    else:
                        print

def datapeminjaman():
    print('''
                - DATA PEMINJAMAN -
            _____________________________
    ''')
    print('Nama Peminjam        : ',d_nama)
    print('Barang yang dipinjam : ',d_pinjam)
    print('')

    while True:
        pilih = input ('===> Masukkan angka 1 untuk kembali : ')
        if pilih == '1':
            data()
            break
        else:
            print

def data():
    print(head)
    print('''
                    - DATA -
                ___________________________
                    1. Data User Peminjam
                    2. Data Barang
                    3. Data Peminjaman
                    4. Keluar
    ''')

    while True:
        pilih= input ('Masukkan pilihan : ')
        if pilih == '1':
            datauser()
            break
        else:
            if pilih == '2':
                databarang()
                break
            else:
                if pilih == '3':
                    datapeminjaman()
                    break
                else:
                    if pilih == '4':
                        menu()
                        break
                    else:
                        print

# login aplikasi
print(head)
print('''
                - LOGIN -
        __________________________
''')
while True:
    user = input ('Masukkan Username : ')
    pas  = input ('Masukkan Password : ')
    if user=='q' or user=='Q':
        break
    elif pas == 'admin' and user == 'admin':
        menu()
        break
    else:
        print('~ password anda tidak sesuai ~\n')
    print

