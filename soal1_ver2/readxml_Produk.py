import xml.dom.minidom as minidom
import os

# Directory Path
# Ganti dengan lokasi folder Produk sampean
PATH_PRODUCT = "C:\\Users\\HP\\Downloads\\mdi-xml-python-test\\soal1_ver2\\Produk"

def fn_countFiles():
    _count = 0
    for path in os.scandir(f"{PATH_PRODUCT}"):
        if path.is_file():
            _count += 1
    return _count

def fn_init(index):
    # Init
    _doc = minidom.parse(f"{PATH_PRODUCT}\\produk{index}.xml")
    return _doc

def fn_getNamaProduk(index):    
    # Return nama 
    _doc = fn_init(index)
    _namaProduk = _doc.getElementsByTagName("namaProduk")[0].getAttribute("val")
    return (_namaProduk)

def fn_getTipeProduk(index):    
    # Return nama 
    _doc = fn_init(index)
    _tipeProduk = _doc.getElementsByTagName("tipeProduk")[0].getAttribute("val")
    return (_tipeProduk)
     
def fn_getVariasiProduk(index):     
    # Return stok produk
    _doc = fn_init(index)
    _variasiProduk = _doc.getElementsByTagName("variasiProduk")
    return  _variasiProduk

def ui_showProduct(index):
    # Cetak Produk
    _namaProduk = fn_getNamaProduk(index)         
    _tipeProduk = fn_getTipeProduk(index)
    print("""

    Produk {}
    Nama Produk: {}
    Tipe: {}         
          """.format(index,_namaProduk,_tipeProduk))
    
def ui_showProductDetail(index):
    # Cetak Produk
    _namaProduk = fn_getNamaProduk(index)         
    _tipeProduk = fn_getTipeProduk(index)
    _variasiProduk = fn_getVariasiProduk(index)
    print("""
= Detail Produk =

    Produk {}
    Nama Produk: {}
    Tipe: {}         
          """.format(index,_namaProduk,_tipeProduk))  
    print ("""
    Variasi Tersedia:
    """)
    for i in range(len(_variasiProduk)):
        print("""
    - Warna: {} Ukuran: {} Harga: Rp. {} Stok: {}
              """.format(
            _variasiProduk[i].getAttribute("warna"),
            _variasiProduk[i].getAttribute("ukuran"),
            _variasiProduk[i].getAttribute("harga"),
            _variasiProduk[i].getAttribute("stok")
        ))
        
def ui_mainmenu(registered):
    print("""
= Homepage =

Produk Tersedia:          
          """)
    for _i in  range(registered):
        ui_showProduct(_i)
        
    print("""

Pilih produk dengan memasukkan index produk          
          """)
    _selected = input("INDEX << ")
    return _selected

def ui_refresh():
    os.system("cls")

def control():
    _registered_product = 0
    
    while True:
        _registered_product = fn_countFiles()
        _select = ui_mainmenu(_registered_product)
        ui_showProductDetail(_select)
        input()
        ui_refresh()
        
# Start        
control()