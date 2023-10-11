def find(neddle:str,haystack:str):
    start=0
    for i in range(0,len(neddle)-1):
        if neddle[i] != haystack[start]:
            continue
        else:
            name=""
            while start<len(haystack):
                if neddle[i] == haystack[start]:
                    name+=neddle[i]
                    start+=1
                    i+=1
                else:
                    start=0
                    break
        if len(name)==len(haystack):
            #print(i)
            print(i-start,i-1)
            break

    return -1
find("maructicar","car")