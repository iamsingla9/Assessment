def change_dict(input_dict):
    #initializing an empty dictionary
    mdict = {}
   
    #iterating over input dictionary
    for keys,values in input_dict.items():
        if(values not in mdict):
            mdict.setdefault(values, [])
            mdict[values].append(keys)
        else:
            mdict[values].append(keys)
       
    return(mdict)
   
if __name__ == '__main__':
    input_dict = {'Julius Ceaser':'Shakespear', 'Train to pakistan':'Khushwant Singh', 'Orient Express':'Agatha Cristie', 'Macbeth':'Shakespear','Delhi':'Khushwant Singh'}
    result = change_dict(input_dict)
    print(result)