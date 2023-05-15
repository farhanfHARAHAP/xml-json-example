import xml.dom.minidom as minidom
import os

# Directory Path
# Ganti dengan lokasi folder Produk sampean
PATH_PRODUCT = "C:\\Users\\HP\\Downloads\\mdi-xml-python-test\\soal1_ver2\\Produk"

def fn_init(index):
    # Init
    _doc = minidom.parse(f"{PATH_PRODUCT}\\produk{index}.xml")
    return _doc

def fn_init(index):
    # Init
    _doc = minidom.parse(f"{PATH_PRODUCT}\\produk{index}.xml")
    return _doc

def fn_setNamaProduk(index, str):
    # Set nama produk
    _doc = fn_init(index)
    _doc.getElementsByTagName("namaProduk")[0].setAttribute("val",str)
    file_xml = open(f"{PATH_PRODUCT}\\produk{index}.xml","w")
    _doc.writexml(file_xml)
    file_xml.close()
    
def fn_setTipeProduk(index, str):
    # Set tipe produk
    _doc = fn_init(index)
    _doc.getElementsByTagName("tipeProduk")[0].setAttribute("val",str)    
    file_xml = open(f"{PATH_PRODUCT}\\produk{index}.xml","w")
    _doc.writexml(file_xml)
    file_xml.close()
    
def fn_tambahVariasiProduk(index, strWarna, strUkuran, strHarga, strStok):
    # Set tipe produk
    _doc = fn_init(index)
    _variasiBaru = _doc.createElement("variasiProduk")   
    _variasiBaru.setAttribute("warna", strWarna)
    _variasiBaru.setAttribute("ukuran", strUkuran)
    _variasiBaru.setAttribute("harga", strHarga)
    _variasiBaru.setAttribute("stok", strStok)
    _doc.firstChild.appendChild(_variasiBaru)
    file_xml = open(f"{PATH_PRODUCT}\\produk{index}.xml","w")
    _doc.writexml(file_xml)
    file_xml.close()    
    

def ui_menu():
    print("""
= Menu =
1. Edit Nama produk
2. Edit Tipe produk
3. Tambah Variasi produk
          """)
    _select = input("INPUT << ")
    return int(_select)

def control():
    os.system("cls")
    _selectOpt = ui_menu()
    if (_selectOpt == 1):
        _index = input("INDEX << ")
        _str = input("NEW VALUE << ")
        fn_setNamaProduk(_index, _str)
    elif (_selectOpt == 2):
        _index = input("INDEX << ")
        _str = input("NEW VALUE << ")
        fn_setTipeProduk(_index, _str)   
    elif (_selectOpt == 3):
        _index = input("INDEX << ")
        _strWarna = input("NEW VALUE (Warna) << ")
        _strUkuran = input("NEW VALUE (Ukuran) << ")
        _strHarga = input("NEW VALUE (Harga) << ")
        _strStok = input("NEW VALUE (Stok) << ")
        fn_tambahVariasiProduk(_index, _strWarna, _strUkuran, _strHarga, _strStok)
        
# Start
control()        

