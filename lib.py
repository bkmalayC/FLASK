def validBookObject(requestObj) :
    keys = requestObj.keys()
    keys = list(keys)
    #print(keys)

    if ('name' in keys and 'price' in keys and 'isbn' in keys) :
        return True
    else:
        return False
