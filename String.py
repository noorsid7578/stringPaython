# name="Siddique "
# print(name)
# print(name[0])
# print(type(name))
# print(name[2:5])
#
# print(len(name))
#
# print(name.upper())
#
# print(name.lower())
#
# print(name.strip())
#
# text="Hello !!!!"
# print(text.rstrip("!"))
#
# print(name.replace("Siddique","Khan"))
#
# full_name="Noor Khan"
# print(full_name)
# print(full_name.replace("Khan","Siddique"))
#
# title="Tufail"
# print(title.replace("T",'S'))
#
# str="!!! Noor!! Noor"
# print(str)
# print(str.split(" "))
#
# txt="Siddique  Khan Sheikh"
# print(txt.split(" "))
#
# name="farhan, noor,farhan"
# print(name.capitalize())
#
# txt="noor"
# txt1=txt.capitalize()
# print(txt1)
#
# str="welcome to the paython !!!"
#
# print(str.center(40))
# print(len(str.center(50)))
# print(len(str))

# print(name.count("farhan"))
#
# print(name.endswith('n'))
# print(name.endswith("o"))
#
# text="hello welcome to the console!!!!"
# print(text.endswith("!!!"))
# print(text.endswith("to",10,20))

text="he's name is Dam .he is an honest man"
print(text)

print(text.find("an"))
print(text.find("p"))

txt="he is an honest man"
print(txt.index("n"))
print(txt.index("a"))

# name="Noor"
# for n in name:
#     print(n)



str1="welcome to program"
print(str1.isalnum())

str="123445"
print(str.isalnum())

print(str.isalpha())
print(str1.isalpha())

str1="welcome to program"
print(str1.isalnum())
print(str1.islower())
str2="Welcon noor"
print(str2.islower())

print(str1.isprintable())
#Title Methode
ngo="World Healt Orginasation"
print(ngo)
print(ngo.istitle())

ngo1="World health orginasation"
print(ngo1.istitle())
#isupper methode
print(ngo.isupper())
NGO="WORLD HEALTH ORGINASTION"
print(NGO)
print(NGO.isupper())

#startswith methode

lang="paython is easy to learn language"

print(lang.startswith("is"))

print(lang.startswith("paython"))
print(lang.startswith("p"))

# Swapcase methode

lang="paython is easy to learn language"
print(lang.swapcase())
# print(lang.upper())

NGO="WORLD HEALTH ORGINASTION"
print(NGO.swapcase())
# print(NGO.lower())

# title methode

lang="paython is easy to learn language"
print(lang.title())

NGO="WORLD HEALTH ORGINASTION"
print(NGO.title())


#End Strings