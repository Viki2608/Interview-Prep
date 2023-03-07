# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    l =[]
    l = re.split('_|-' , text)
    for i in range(len(l)):
        if i !=0:
            l[i] = l[i][0].upper() + l[i][1:]
    return ''.join(l)

print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The-Stealth_Warrior"))
print(to_camel_case("the_Stealth-Warrior"))