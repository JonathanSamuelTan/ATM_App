from customer import *
import datetime
import random


def quit(atm):
    print("Resi tercetak otomatis saat anda keluar.")
    print("Harap disimpan sebagai bukti transaksi.")
    print(45*"=")
    print("No. Record       :"+str(random.randint(10000,100000)))
    print("Tanggal          :",datetime.datetime.now())
    print("Saldo akhir anda :Rp"+str(atm.getBalance()))
    print(45*"=")
    print("TERIMAKASIH , PASTIKAN TIDAK MENINGGALKAN BARANG BAWAAN ANDA :)")
    exit() 

atm = Customer(id)
repeat = True
while repeat:
    print("SELAMAT DATANG DI ATM PROGATE X JONATHAN")
    id = int(input("Masukan PIN Anda : "))
    trial = 0
    while(id != atm.getPin() and trial<3):
        print("Pin Anda SALAH , Silahkan Coba Lagi")
        id = int(input("Masukan PIN Anda : "))
        trial +=1
    if trial == 3 :
        print("ERROR , Silahkan Ambil Kartu dan Coba Lagi")
        break

    print("JENIS TRANSAKSI : ")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Simpan")
    print("4. Ganti PIN")
    print("5. Keluar")
    select = int(input("Silahkan Pilih Menu : "))


    if select == 1:
        print("Saldo anda sekarang :Rp"+str(atm.getBalance()))
        repeat = input("Apakah anda mau melakukan transaksi lainnya (yes/no)? => ")
        if(repeat.casefold()=="no"):
            repeat = False
        else:
            continue

    elif select == 2:
        print("Saldo awal anda :Rp"+str(atm.getBalance()))
        nominal = int(input("Masukan Nominal yang Ingin Ditarik :Rp"))
        if(atm.getBalance()>=nominal):
            atm.withdraw(nominal)
            print("Transaksi Berhasil...")
            print("Saldo anda sekarang :Rp"+str(atm.getBalance()))
        else:
            print("Transaksi Gagal...")
            print("Maaf saldo anda tidak cukup")

        repeat = input("Apakah anda mau melakukan transaksi lainnya (yes/no)? => ")
        if(repeat.casefold()=="no"):
            repeat = False
        else:
            continue


    elif select == 3:
        print("Saldo awal anda :Rp"+str(atm.getBalance()))
        nominal = int(input("Masukan Nominal yang Ingin Disimpan :Rp"))
        atm.deposit(nominal)
        print("Transaksi Berhasil...")
        print("Saldo anda sekarang :Rp"+str(atm.getBalance()))
        repeat = input("Apakah anda mau melakukan transaksi lainnya (yes/no)? => ")
        if(repeat.casefold()=="no"):
            repeat = False
        else:
            continue


    elif select == 4:
        id = int(input("Masukan PIN lama anda :"))
        trial = 0
        #validasi
        while(id != atm.getPin() and trial<3):
            print("Pin Anda SALAH , Silahkan Coba Lagi")
            id = int(input("Masukan PIN Anda : "))
            trial +=1
        if trial == 3 :
            print("ERROR , Silahkan Ambil Kartu dan Coba Lagi")
            exit()
        
        #ganti pin
        cont = True
        while(cont):
            new_PIN = int(input("Masukan PIN baru anda (4 digit angka) : "))
            confirm = int(input("Masukan kembali PIN baru anda untuk konfirmasi : "))
            #validasi
            if(new_PIN==confirm and len(str(new_PIN))==4):
                atm.custPin = new_PIN
                print("PIN berhasil diubah")
                print("PIN anda sekarang : "+atm.custPin)
                cont = False
            elif(len(str(new_PIN))<4):
                print("PIN baru tidak boleh menggunakan 0 pada digit pertama! Silahkan coba lagi")
                cont = True
            else:
                print("Pin Anda SALAH atau PIN baru anda tidak sesuai, Silahkan Coba Lagi")
                cont = True

        repeat = input("Apakah anda mau melakukan transaksi lainnya (yes/no)? => ")
        if(repeat.casefold()=="no"):
            repeat = False
        else:
            continue


    elif select == 5:
        quit(atm)
    else:
        print("Error , Menu Tidak Tersedia")

quit(atm)
    