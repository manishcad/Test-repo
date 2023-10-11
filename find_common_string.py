def common(string_1,string_2):
    data_set=set()
    for i in string_1:
        data_set.add(i)
    for i in string_2:
        if i in data_set:
            print(i)
        else:
            pass


common("NAINAZ","REENEZ")