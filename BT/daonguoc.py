def convert_string(s):
    list_str= s.split(" ")
    list_str.reverse()
    str = " ".join(list_str)
    new_str = ''
    for i in str:
        if i.isupper(): new_str += i.lower()
        elif i.islower(): new_str += i.upper()
        else: new_str += i
    return new_str

s = "tHE fOX iS cOMING fOR tHE cHICKEN"
print(convert_string (s) ) 