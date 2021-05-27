from LnkHeader import hex_to_int, LinkFlags, SwChange, FileAttr


def fileopen():
    data = bytearray()
    file = "Color cop.lnk"
    with open(file, 'rb') as f:
        data = f.read()
    return data


def lnkparse(data):
    
    lnk_header_signature = bytes(b'L\x00\x00\x00') # fixed value
    lnk_header_clsid = uuid.UUID('{00021401-0000-0000-c000-000000000046}') # fixed value
    lnk_fixedValue_size = 20
    lnk_time_size = 8
    lnk_header_size = 76
    
    
    lnk_header_clsid_1 = data[4:8]
    lnk_header_clsid_2 = data[8:20]
    lnk_header_clsid_1 = lnk_header_clsid_1[::-1]
    lnk_header_clsid_3 = lnk_header_clsid_1+lnk_header_clsid_2
    lnk_header_clsid_4 = uuid.UUID(bytes=lnk_header_clsid_3)
    
    if lnk_header_signature == data[0:4] and lnk_header_clsid == lnk_header_clsid_4:
        print("check sig and uuid")
        
        lnk_header_flags = data[20:24]
        lnk_header_fileattr = data[lnk_fixedValue_size+len(lnk_header_flags):lnk_fixedValue_size+len(lnk_header_flags)+4]
        
        lnk_header_CreationTime = data[lnk_fixedValue_size+8:lnk_fixedValue_size+8+lnk_time_size] # number 8 mean lnk_header flags, fileattr size
        lnk_header_AccessTime = data[lnk_fixedValue_size+8+lnk_time_size:lnk_fixedValue_size+8+(lnk_time_size*2)]
        lnk_header_WriteTime = data[lnk_fixedValue_size+8+(lnk_time_size*2):lnk_fixedValue_size+8+(lnk_time_size*3)]
        
        lnk_FileSize = data[lnk_fixedValue_size+8+(lnk_time_size*3):lnk_fixedValue_size+8+(lnk_time_size*3)+4]
        
        lnk_IconIndex = hex_to_int(data[lnk_fixedValue_size+8+(lnk_time_size*3)+4:lnk_fixedValue_size+8+(lnk_time_size*3)+8])
        
        lnk_SwValue = data[lnk_fixedValue_size+8+(lnk_time_size*3)+8:lnk_fixedValue_size+8+(lnk_time_size*3)+8+4]
        
        lnk_hotkey = data[lnk_fixedValue_size+8+(lnk_time_size*3)+8+4:lnk_fixedValue_size+8+(lnk_time_size*3)+8+4+2]
        
        lnk_unknown = 10 # Unknown byte total 2byte + 4byte + 4byte not use
        
        
        a = LinkFlags(lnk_header_flags)
        
        
        b = FileAttr(lnk_header_fileattr)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else: return 0
    
    






if __name__ == '__main__':
    import uuid
    lnk_data = fileopen()
    
    lnkparse(lnk_data)
    