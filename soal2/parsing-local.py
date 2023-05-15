import json

def init(_filename):
    _file = open(_filename)
    _dataPerson = json.loads(_file.read())
    print(_dataPerson)
    _file = open("local-data-desc.json")
    _dataDesc = json.loads(_file.read())
    
    # Make Description
    _desc = ""
    
    if(_dataPerson['status']['isMarried']):
        _desc = _desc+_dataDesc['isMarried']
    else:
        _desc = _desc = _desc+_dataDesc['isNotMarried']
        
    if(_dataPerson['status']['isAlive']):
        _desc = _desc+" "+_dataDesc['isAlive']
    else:
        _desc = _desc+" "+_dataDesc['isNotAlive']
        
    if(_dataPerson['status']['isEmployed']):
        _desc = _desc+" "+_dataDesc['isEmployed']
    else:
        _desc = _desc+" "+_dataDesc['isNotEmployed']
        
    if(_dataPerson['age'] < 60):
        _desc = _desc+" "+_dataDesc['isYoung']
    else:
        _desc = _desc+" "+_dataDesc['isNotYoung']
    
    

    print(f"""
          
    Name: {_dataPerson['fullname']}  
    Country: {_dataPerson['country']}   
    Age: {_dataPerson['age']}    

    Description: 
    {_desc} 
    
    Contact:
    - Phone {_dataPerson['contact-info']['phone']}
    - Email {_dataPerson['contact-info']['email']}     
    - Instagram {_dataPerson['contact-info']['instagram']}
        """)
    
selectFile = input("Input filename: ")    
init(selectFile)