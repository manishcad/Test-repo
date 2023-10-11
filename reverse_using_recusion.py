def reverse(string:str):
    if string=="":
        return string
    s=reverse(string[1:])+string[0]
    print(s)
    return s


reverse("manish")