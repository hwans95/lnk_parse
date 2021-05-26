
def fileopen():
    data = bytearray()
    file = "Color cop.lnk"
    with open(file, 'rb') as f:
        data = f.read()
    return data


def hex_to_int(num):
    number = int.from_bytes(num, byteorder="little",signed=True)
    return number

def SwChange(sw):
    value_0 = [0,'SW_HIDE']
    value_1 = [1,'SW_SHOWNORMAL']
    value_2 = [2,'SW_SHOWMINIMIZED']
    value_3 = [3,'SW_SHOWMAXIMIZED']
    value_4 = [4,'SW_SHOWNOACTIVATE']
    value_5 = [5,'SW_SHOW']
    value_6 = [6,'SW_MINIMIZE']
    value_7 = [7,'SW_SHOWMINNOACTIVE']
    value_8 = [8,'SW_SHOWNA']
    value_9 = [9,'SW_RESTORE']
    value_10 = [10,'SW_SHOWDEFAULT']
    value_11 = [11,'SW_FORCEMINIMIZE']
    value_error = 'Unknown'
    
    value = hex_to_int(sw)
    
    if value == value_0[0]:
        return value_0[1]
    elif value == value_1[0]:
        return value_1[1]
    elif value == value_2[0]:
        return value_2[1]
    elif value == value_3[0]:
        return value_3[1]
    elif value == value_4[0]:
        return value_4[1]
    elif value == value_5[0]:
        return value_5[1]
    elif value == value_6[0]:
        return value_6[1]
    elif value == value_7[0]:
        return value_7[1]
    elif value == value_8[0]:
        return value_8[1]
    elif value == value_9[0]:
        return value_9[1]
    elif value == value_10[0]:
        return value_10[1]
    elif value == value_11[0]:
        return value_11[1]
    else: return value_error
    

def lnkparse(data):
    
    lnk_header_signature = bytes(b'L\x00\x00\x00') # fixed value
    lnk_header_clsid = uuid.UUID('{00021401-0000-0000-c000-000000000046}') # fixed value
    lnk_fixedValue_size = 20
    lnk_time_size = 8
    
    
    lnk_header_clsid_1 = data[4:8]
    lnk_header_clsid_2 = data[8:20]
    lnk_header_clsid_1 = lnk_header_clsid_1[::-1]
    lnk_header_clsid_3 = lnk_header_clsid_1+lnk_header_clsid_2
    lnk_header_clsid_4 = uuid.UUID(bytes=lnk_header_clsid_3)
    
    if lnk_header_signature == data[0:4] and lnk_header_clsid == lnk_header_clsid_4:
        print("check sig and uuid")
        
        lnk_header_flags = data[20:24]
        lnk_header_fileattr_1 = data[lnk_fixedValue_size+len(lnk_header_flags):lnk_fixedValue_size+len(lnk_header_flags)+4]
        
        #print(lnk_header_fileattr_1)
        
        lnk_header_CreationTime = data[lnk_fixedValue_size+8:lnk_fixedValue_size+8+lnk_time_size] # number 8 mean lnk_header flags, fileattr size
        lnk_header_AccessTime = data[lnk_fixedValue_size+8+lnk_time_size:lnk_fixedValue_size+8+(lnk_time_size*2)]
        lnk_header_WriteTime = data[lnk_fixedValue_size+8+(lnk_time_size*2):lnk_fixedValue_size+8+(lnk_time_size*3)]
        
        lnk_FileSize = data[lnk_fixedValue_size+8+(lnk_time_size*3):lnk_fixedValue_size+8+(lnk_time_size*3)+4]
        
        lnk_IconIndex = hex_to_int(data[lnk_fixedValue_size+8+(lnk_time_size*3)+4:lnk_fixedValue_size+8+(lnk_time_size*3)+8])
        
        lnk_SwValue = data[lnk_fixedValue_size+8+(lnk_time_size*3)+8:lnk_fixedValue_size+8+(lnk_time_size*3)+8+4]
        
        lnk_hotkey = data[lnk_fixedValue_size+8+(lnk_time_size*3)+8+4:lnk_fixedValue_size+8+(lnk_time_size*3)+8+4+2]
        
        lnk_unknown = 10 # Unknown byte total 2byte + 4byte + 4byte
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else: return 0
    
    






if __name__ == '__main__':
    import uuid
    lnk_data = fileopen()
    
    lnkparse(lnk_data)
    