def can_place(flower_list,n):
    new_List=flower_list.insert(0,0)
    flower_list.append(0)
    start=1
    for i in range(start,len(flower_list)):
        if flower_list[i]==0 and flower_list[i-1]==0 and flower_list[i+1]==0:
            flower_list[i]=1
            n-=1
    if n>0:
        return False
    else:
        return True





print(can_place([1,0,0,0,0,1],2))