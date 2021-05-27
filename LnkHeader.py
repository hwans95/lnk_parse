def hex_to_int(num):
    number = int.from_bytes(num, byteorder="little",signed=True)
    return number

def LinkFlags(flags):
    rec_1 = hex_to_int(flags)
    num_val = 27
    rec_2 = format(rec_1,'b')
    rec_3 = rec_2.zfill(num_val)
    rec_4 = rec_3[::-1]
    flags_list = []
    attr_list = ["HasLinkTargetIDList", "HasLinkInfo", "HasName", "HasRelativePath", "HasWorkingDir",
                 "HasArguments", "HasIconLocation", "IsUnicode", "ForceNoLinkInfo", "HasExpString",
                 "RunInSeparateProcess", "Unused1", "HasDarwinID", "RunAsUser", "HasExpIcon",
                 "NoPidlAlias", "Unused2", "RunWithShimLayer", "ForceNoLinkTrack", "EnableTargetMetadata",
                 "DisableLinkPathTracking", "DisableKnownFolderTracking", "DisableKnownFolderAlias", "AllowLinkToLink",
                 "UnaliasOnSave", "PreferEnvironmentPath", "KeepLocalIDListForUNCTarget"]
    i = 0
    while i <= 26:
        if rec_4[i] == '1':
            flags_list.append(attr_list[i])
        i = i+1
    return flags_list

def FileAttr(attr):
    num_val = 15
    fa_1 = hex_to_int(attr)
    fa_2 = format(fa_1, 'b')
    fa_3 = fa_2.zfill(num_val)
    fa_4 = fa_3[::-1]
    fa_list = []
    fa_attr = ['FILE_ATTRIBUTE_READONLY', 'FILE_ATTRIBUTE_HIDDEN', 'FILE_ATTRIBUTE_SYSTEM', 'Reserved1', 'FILE_ATTRIBUTE_DIRECTORY',
               'FILE_ATTRIBUTE_ARCHIVE', 'Reserved2', 'FILE_ATTRIBUTE_NORMAL', 'FILE_ATTRIBUTE_TEMPORARY', 'FILE_ATTRIBUTE_SPARSE_FILE',
               'FILE_ATTRIBUTE_REPARSE_POINT', 'FILE_ATTRIBUTE_COMPRESSED', 'FILE_ATTRIBUTE_OFFLINE', 'FILE_ATTRIBUTE_NOT_CONTENT_INDEXED',
               'FILE_ATTRIBUTE_ENCRYPTED']
    
    i = 0 
    while i <= 14:
        if fa_4[i] == '1':
            fa_list.append(fa_attr[i])
        i += 1
    
    return fa_list
    









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
    