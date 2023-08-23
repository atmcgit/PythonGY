print(type(9))

print(type(9.2))

print(9+9)
print(9*9)

print(type(9+9))
print(type(9*9))

print('HELLO ERA AI')
print(type('HELLO ERA AI'))

#SAYILAR VE STRINGLERE GIRIS
""
''
123
print(type("123"))
print("a"+"b")
print("a"+"-b")

#STRING METODLARI - LEN

gel_yaz = "gelecegi_yazanlar"

a = 9
b = 10
a*b
print(len(gel_yaz))

#STRING METODLARI - upper() & lower()

B = gel_yaz.upper()
K = gel_yaz.lower()
print(B)
print(K)
print(B.islower())
print(B.isupper())
print(K.isupper())
print(K.islower())

#STRING METODLARI - replace()

gel_yaz.replace("e","a")
C  = gel_yaz.replace("e","a")
print(C)
X = gel_yaz.replace("a","i")
print(X)

#STRING METODLARI - strip()

# Python'un strip() yöntemi, bir dizenin başındaki ve sonundaki belirli karakterleri kaldırmak için kullanılır. 
gel_yaz = " gelecegi_yazanlar "
print(gel_yaz.strip())

gel_yaz= "*gelecegi_yazanlar*"
print(gel_yaz.strip("*"))

# METODLARA GENEL BAKIŞ
gel_yaz= "gelecegi_yazanlar"
print(dir(gel_yaz))

print(gel_yaz.capitalize()) # ilk harf büyüt
print(gel_yaz.title())      # baş harfleri büyüt

# SUBSTRİNGLER
gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]
print(gel_yaz[3:8])