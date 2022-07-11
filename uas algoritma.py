from ast import Break
from cmath import pi
from curses import KEY_OPEN
from tkinter.tix import InputOnly
import datetime
import time
from typing import Tuple
now = datetime.datetime.now()
tanggal = now.date()
waktu = now.time()

d_nomor = {'00001':'00001','00002':'00002','00003':'00003'}
d_nama = {'00001':'anandito','00002':'bagas','00003':'zidan'}
d_kode = {'01':'01','02':'02','03':'03'}
d_barang = {'01':'Laptop','02':'mouse','03':'keyboard'}
d_pinjam = {'anandito':'Laptop HP warna hitam','bagas':'mouse wireless','zidan':'keyboard mecanic'}

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
        pilih = input('Masukkan pilihan')
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
    print('Nama ==>',d_nama[nomor])
    print()
    print('tekan q atau Q ketika sudah melakukan pinjaman')
    while True:
        kode = input('Masukkan kode barang : ')
        if kode == 'q' or kode == 'Q':
            print()
            print('''--------------------------------------------
                        |       Cetak Bukti Peminjaman      |   
                        |             DIVISI IT             |
                    --------------------------------------------
            ''')
            print('Nama Peminjam : ',d_nama[nomor])
            print('Buku yang dipinjam : ')
            for n in range(len(d_barang2)):
                n+1
                print('\t\t %s\t    \t\t'%(d_barang2[n]))
            print('___________________________________________________________')
            print('Total barang yang dipinjam :',len(d_barang2))
            print
            print('Barang dikembalikan dalam waktu 12 hari setelah peminjam')
            print('-----------------------------------------------------------')
            print('Tanggal. %s-%s-%s    %s:%s:%s'%(tanggal.day,tanggal.month,tanggal.year,waktu.hour,waktu.minute,waktu.second),'v.1.0')
            print('''-----------------------------------------------------------
                                 TERIMAKASIH ATAS KUNJUNGAN ANDA             
                    -----------------------------------------------------------
                ''')
            break
        elif kode ==d_kode[kode]:
            buku=d_barang[d_kode[kode]]
            d_barang2.append(barang)
            d_barang2.append(barang)
            print('==>',d_barang[kode]);
        else:
            print
    while True:
        tanya = input('lagi? ==>')
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
    print('Nomor dan nama anggota peminjam : ',d_nama)
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
    nomor= input ('Masukkan nomor anggota peminjam barang : ')
    print('')
    nama= input('Masukkan nama anggota peminjam barang : ')
    print('')
    d_nomor[nomor]=nomor
    d_nama[nomor]=nama
    while True:
        tanya = input('lagi? ==>')
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
    nomor= input ('Masukkan nomor anggota peminjam : ')
    print(' ==>',d_nama[nomor],'Telah dihapus')
    del d_nomor[nomor]
    del d_nama[nomor]
    print('')
    while True:
        tanya = input('lagi? : ')
        if tanya == 'y' or tanya == 'Y':
            hapus()
            break
        else:
            if tanya == 'y' or tanya== 'Y':
                datauser()
                break
            else:
                print

def datauser():
    print('''
                - DATA PEMINJAM BARANG -
            _________________________________
                1. Daftar anggota
                2. Tambah anggota
                3. Hapus anggota
                4. Kembali
        ''')
    while True:
        pilih = input ('Masukklah Pilihan')
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
    kode= input ('Masukkan kode buku : ')
    print('')
    barang= input('Masukkan nnama barang : ')
    print('')
    d_kode[kode]=kode
    d_barang[kode]=barang
    while True:
        tanya = input('lagi? ==>')
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
        tanya = input('lagi? : ')
        if tanya == 'y' or tanya == 'Y':
            hapusbarang()
            break
        else:
            if tanya == 'y' or tanya== 'Y':
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
        pilih = input ('Masukklah Pilihan')
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
            _____________________
                1. Data User Peminjam
                2. Data Barang
                3. Data Peminjaman
                4. Keluar
    ''')

    while True
