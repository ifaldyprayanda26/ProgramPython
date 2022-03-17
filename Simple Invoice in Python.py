from num2words import num2words

kode_barang=[]
input_kode_barang=[]
jumlah_barang=[]
deskripsi_barang=[]
harga_barang=[]
total_harga=[]
unit = []
pajak = []
disc = []

print("==================================================")
print("             PT. SAMPLE DATA ZAHIR                ")
print("==================================================")
print("Kode Barang      Deskripsi Barang    Unit    Harga")
print("--------------------------------------------------")
print("PRO-11           Produk K            Pcs     150.000")
print("PRO-024          Produk X            Pcs     150.000")
print("PRO-025          Produk Y            Pcs     150.000")
print("PRO-026          Produk Z            Pcs     150.000")
print("===================================================")

banyak_jenis=int(input("Banyak Jenis Barang : "))

i = 0
while i<banyak_jenis:
    print("Barang ke -", 1+i)
    input_kode_barang.append(int(input("Kode Barang [11/24/25/26]")))
    jumlah_barang.append(int(input("Jumlah Barang : ")))

    if input_kode_barang[i]==11:
        deskripsi_barang.append("Produk K")
        kode_barang.append("PRO-11")
        harga_barang.append(150000)
        total_harga.append(jumlah_barang[i]*150000)
        unit.append("Pcs")
        pajak.append(10)
        disc.append(0)
    elif input_kode_barang[i]==24:
        deskripsi_barang.append("Produk X")
        kode_barang.append("PRO-024")
        harga_barang.append(150000)
        total_harga.append(jumlah_barang[i]*150000)
        unit.append("Pcs")
        pajak.append(10)
        disc.append(0)
    elif input_kode_barang[i]==25:
        deskripsi_barang.append("Produk Y")
        kode_barang.append("PRO-025")
        harga_barang.append(150000)
        total_harga.append(jumlah_barang[i]*150000)
        unit.append("Pcs")
        pajak.append(10)
        disc.append(0)
    elif input_kode_barang[i]==26:
        deskripsi_barang.append("Produk Z")
        kode_barang.append("PRO-026")
        harga_barang.append(150000)
        total_harga.append(jumlah_barang[i]*150000)
        unit.append("Pcs")
        pajak.append(10)
        disc.append(0)
    else:
        harga_barang.append(0)
        kode_barang.append("Kode Barang tidak tersedia")
        deskripsi_barang.append("Deskripsi tidak ditemukan")
        total_harga.append(jumlah_barang[i]*0)
        unit.append("Pcs")
        pajak.append(0)
        disc.append(0)
    i = i + 1

print("FAKTUR PEMBELIAN                          PT. SAMPLE DATA ZAHIR")
print("===============================================================")
print("Nomor   : 00000036                      Pengiriman : 1 May 2018")
print("Tanggal : 2 May 2018                    Nomor PO   : PO000013  ")
print("Kepada  : Sample Vendor                 Mata Uang  : IDR(Rupiah)")
print("Up      :                               Term       : Cash/Tunai")
print("                                                               ")
print("===============================================================")
print("Kode    Deskripsi    Jumlah    Unit    Disc    Sub Total  Pajak")
print("===============================================================")

total_bayar = 0
p = 0
while p<banyak_jenis:
    total_bayar = total_bayar+total_harga[p]
    print("%s     %s       %i       %s       %i      %i      %i" %(kode_barang[p],   deskripsi_barang[p],   jumlah_barang[p],   unit[p],   disc[p],   total_harga[p],   pajak[p]))
    p = p + 1

print("===============================================================")

total_pajak = (total_bayar*10)/100
result = num2words(int(total_bayar+total_pajak), lang="id")
print("Terbilang : " + result + " Rupiah")
print("===============================================================")
print("                                 Sub Total         : Rp ", total_bayar)
print("                                 Total Pajak       : Rp ", int(total_pajak))
print("                                 Biaya Pengantaran : 0")
print("                                 Dibayar           : 0")
print("                                 Saldo             : Rp ", int(total_bayar+total_pajak))
print("                                 ==============================")
print("                                                                ")
print("         Sample Vendor                     PT. SAMPLE DATA ZAHIR\n")
print("                                                               ")
print("                                                               ")
print("                                                               ")
print("      ------------------                  ----------------------")

