# Medium [1] Anagram Number:

def anagram_number(number):
    number_unchange=number
    revert_number=0
    if number==0:
        return True
    else:
        while (number != 0):
            a=number %10
            revert_number=revert_number*10 + a
            number=number //10

        if(revert_number == number_unchange):
            return True
        return False
      




# Medium [2] Roman to Integer
.
def roman_to_int(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number
