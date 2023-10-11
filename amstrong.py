number="371" # o(1)
number_length=len(str(number)) #o(1)
sums=0 #o(1)
for i in str(number): # o(n)
    value=pow(int(i),number_length)
    sums+=value

print(sums) # o(1)