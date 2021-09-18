# 1
# Easy [1] Day different:

from datetime import date
from datetime import time
from datetime import datetime


def day_diff(release_date, code_complete_day):
    format_string="%d/%m/%Y"
    release=datetime.strptime(release_date, format_string)
    format_string2="%Y-%d-%m"
    complete=datetime.strptime(code_complete_day, format_string2)
    can_test = release - complete    
    return can_test


# Easy [2] Alphabet and Number:

# 2
import re
def alpha_num(sentence):
    matched = re.findall(
        r'(?:[a-zA-Z]+\d+|\d+[a-zA-Z]+)[a-zA-Z\d]*(?=\s|$)', sentence)
    return matched


