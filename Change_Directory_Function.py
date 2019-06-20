def change_path(oldpath, newpath):
    oldpath = oldpath.replace('/','').strip()
    oldlist = list(oldpath)
    newpath = newpath.replace('..','.')
    newpath = newpath.replace('/','').strip()
    newlist = list(newpath)
    length_newlist = len(newlist)
    i = 0
    currentpath = '/'
   
    #if directly changing to parent directory using cd /
    if(length_newlist == 0):
        return(currentpath)

    #if changing from parent directory like cd /a/b
    if(newlist[i] != '.'):
        oldlist = []
        while(i<length_newlist):
            if(newlist[i] != '.'):
                oldlist.append(newlist[i])
                i += 1
            else:
                break
    
    #impleting stack method to change the directory
    while(i < length_newlist):
        if(newlist[i] == '.'):
            if(oldlist):
                oldlist.pop()
                i +=1
            else:
                return("Invalid Directory")
        else:
            oldlist.append(newlist[i])
            i += 1

    currentpath += '/'.join(oldlist)
    return(currentpath)
   
if __name__ == '__main__':
    oldpath = "/a/b/c/d"
    newpath = str('/../../../x/d/../../b/c/d')
    result = change_path(oldpath, newpath)
    print("Present working directory is : ",result)