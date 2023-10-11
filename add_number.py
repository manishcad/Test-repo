number1="1234"
number2="9678"

carry=0
for i in range(len(number1)-1,-1,-1):
    val=int(number1[i])+int(number2[i])+carry
    carry=val//10
    value=val%10

    #print(carry)
    if carry:
        print(value+carry)
    else:
        print()

