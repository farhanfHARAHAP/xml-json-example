import xml.dom.minidom as minidom

def main():
    # Cetak isi doc dan tag pertamanya
    doc = minidom.parse("AtasanPria.xml")
    print (doc.nodeName)
    print (doc.firstChild.tagName)
    
    # Cetak nama 
    namaProduk = doc.getElementsByTagName("namaProduk")[0].firstChild.data
    print (namaProduk)
    
    # Cetak harga produk
    hargaProduk = doc.getElementsByTagName("hargaProduk")[0].firstChild.data
    print (hargaProduk)
     
    # Cetak stok produk
    stokProduk = doc.getElementsByTagName("stokProduk")
    
    print ("\nStok Tersedia:")
    for i in range(len(stokProduk)):
        print("- Warna: {} Ukuran: {} Stok: {}".format(
            stokProduk[i].getAttribute("warna"),
            stokProduk[i].getAttribute("ukuran"),
            stokProduk[i].getAttribute("stok")
        ))
        
main()       