import json
from urllib import request

def init(_username):
# tentukan url endpoint
    _url = f"https://api.github.com/users/{_username}"

    # lakukan http request ke server
    _response = request.urlopen(_url)

    # parsing data json
    _data = json.loads(_response.read())

    # cetak hasil parsing data
    print(_data)
    
    # Cetak rapih
    print(f"""
          
Username    : {_data['login']}              
ID          : {_data['id']}
Pengikut    : {_data['followers']}
Akun dibuat : {_data['created_at']}
Jumlah Repo : {_data['public_repos']}

          """)
    
selectUser = input("Ketik username: ")
init(selectUser)