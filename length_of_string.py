def lenght(string,size=0):
    if string=="":
        return size
    size+=1
    return lenght(string[1:],size)

#print(lenght("manish"))

