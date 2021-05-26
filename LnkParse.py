
def fileopen():
    data = bytearray()
    file = "Color cop.lnk"
    with open(file, 'rb') as f:
        data = f.read()
    return data


def lnkparse(data):
    
    lnk_header_signature = bytes(b'L\x00\x00\x00') # fixed value
    lnk_header_clsid = uuid.UUID('{00021401-0000-0000-c000-000000000046}') # fixed value
    
    lnk_header_clsid_1 = data[4:8]
    lnk_header_clsid_2 = data[8:20]
    lnk_header_clsid_1 = lnk_header_clsid_1[::-1]
    lnk_header_clsid_3 = lnk_header_clsid_1+lnk_header_clsid_2
    lnk_header_clsid_4 = uuid.UUID(bytes=lnk_header_clsid_3)
    
    if lnk_header_signature == data[0:4] and lnk_header_clsid == lnk_header_clsid_4:
        print("check sig and uuid")
        
        lnk_header_flags = data[20:24]
        lnk_header_fileattr_1 = int.from_bytes(data[20+len(lnk_header_flags):20+len(lnk_header_flags)+4], byteorder='little', signed=True)
        
        print(lnk_header_fileattr_1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else: return 0
    
    






if __name__ == '__main__':
    import uuid
    lnk_data = fileopen()
    
    lnkparse(lnk_data)
    