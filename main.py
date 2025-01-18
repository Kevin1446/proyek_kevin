import sys


Daftar_menu = {
    1:"BAKSO RUDAL",
    2:"MIE AYAM",
    3:"BAKSO SUMSUM",
    4:"BAKSO BERANAK",
    5:"BAKSO IGA",
}

Daftar_harga = {
    1: 13000,
    2: 13000,
    3: 50000,
    4: 35000,
    5: 25000

}
dict_trx ={}
daftar_metode_pembayaran = {
    1:"Cash",
    2:"QR CODE",
    3:"TRANSFER"
}

print(login())

print("=====================SELAMAT DATANG DI ANGEL SHOP BAKSO DAN MIE AYAM============")
print("======================================List Product==============================")
for x in Daftar_menu:
        print("Id_Product: ",x,"\t Nama Product : ",
          Daftar_menu[x],"\t\t Harga Product : ",Daftar_harga[x])
print("===============================================================================")

pilih_id = int(input("pilih Id: "))

if pilih_id in Daftar_menu : 
        pilih_id = input ("Ingin Beli ? (Y/N): ")
        if pilih_id == "y" or pilih_id== "Y":
            Nama_penerima       = input("Nama Penerima      : ")
            Alamat_penerima     = input("Alamat Penerima    : ")
            Telepon             = input("No HP              : ")
            Kurir_pengiriman    = input("Kurir Pengiriman   : ")
            dict_trx = {
                "Nama_penerima":Nama_penerima,
                "Alamat_penerima":Alamat_penerima,
                "No HP":Telepon,
                "Kurir Pengiriman":Kurir_pengiriman,
                "product id":pilih_id,
            }   
        else:
            print("GOOD BYE BROOOOO")
            sys.exit()

        if len (dict_trx) > 0:
            print(" ========================== Metode Pembayaran =========================")
        for x in daftar_metode_pembayaran:
            print("id : ",x, "\t Metode Pembayaran : ", daftar_metode_pembayaran[x])
        pilih_metode = int(input("Pilih ID Metode Pembayaran: "))
        if pilih_metode in daftar_metode_pembayaran :
            print("Nama Penerima : ", dict_trx["Nama_penerima"])
            print("Alamat Penerima : ", dict_trx["Alamat_penerima"])
            print("No HP : ", dict_trx["No HP"])
            print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
            print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
            konfirmasi = input("Apakah Anda Yakin ingin melakukan pembayaran? (Y/N) : ")
            if konfirmasi == "y" or konfirmasi == "Y":
                print("TERIMA KASIH ANDA TELAH MELAKUKAN PEMBELIAN DI TOKO KAMI")
            else:
                print("EXIT")
            sys.exit()
        else:
            print("ID METODE PEMBAYARAN TIDAK TERSEDIA")
else:
    print("ID PRODUCT TIDAK TERSEDIA")
sys.exit()
