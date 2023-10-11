def SumOfDigit(lst,add=1):
    if lst==[]:
        return add
    value=add*lst[0]
    return SumOfDigit(lst[1:],value)
    return value


print(SumOfDigit([5,2,3,2]))