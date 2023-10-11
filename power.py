def power(num,pow):
    if pow==0:
        return
    value=num*pow
    print(value)
    power(value,pow-1)

power(5,3)
