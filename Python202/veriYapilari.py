# VERI YAPILARI

# Listeler

# []
# list()

notlar = [70, 85, 90, 60]
liste = ["a", 19.3, 90]
list_genis = ["a", 19.3, 90, notlar]

print(len(list_genis))

print(type(notlar))

print(type(list_genis[2]))

tum_liste = [liste, list_genis]
# del tum_liste


# Listeler - Eleman Islemleri

liste1 = [10, 20, 30, 40, 50]
liste1[0]
liste1[1]
# liste1[6]

liste1[0:2]  # 0dan 2 ye kadar
liste1[:2]  # 0dan 2 ye kadar

liste1[2:]  # 2den sona kadar

liste2 = ["a", 10, [10, 20, 30, 40, 50]]
liste2[2]

liste2[0:2]
liste2[2][4]  # 50

# Listeler - Eleman Değiştirme

liste3 = ["ali", "veli", "berkcan", "ayse"]

liste3[1] = "velinin-babasi"

liste3[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"
print(liste3)

liste3 = ["ali", "veli", "berkcan", "ayse"]
liste3 + ["kemal"]
print(liste3)
liste3 = liste3 + ["kemal"]
liste3.append("kemal")
print(liste3)
del liste3[4]
liste3.remove("kemal")
liste3.pop(2)
print(liste3)

# insert - ekleme

print(liste3)
liste3.insert(0, "fatma")
print(liste3)
liste3[0] = "mustafa"
print(liste3)
liste3.insert(4, "mehmet")
print(liste3)
liste3.insert(len(liste3), "merve")
print(liste3),


# pop - silme

liste3.pop(0)
print(liste3)
# count - saydırma

liste3 = ["ali", "veli", "isik", "ali", "veli"]
liste3.count("veli")
print(liste3.count("ali"))

# copy kopya
list_yedek = liste3.copy()

print(list_yedek)

# extend birleştir

liste3.extend(["a", "b", 10])
print(liste3)

# index() index bilgisini verir

print(liste3.index("ali"))

# reverse() tersten yazdırma

liste3.reverse()
print(liste3)

# sort() sıralama

liste = [10, 50, 40, 90]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

# Veri Yapıları - Tuple
# kapsayıcı,sıralı,değiştirilemez
t = ("ali", "veli,", 1, 2, 3.2, [1, 2, 3, 4])
t = "ali", "veli", 1, 2, 3.2, [1, 2, 3, 4]

# tuple()

t = ("eleman",)  # virgül olmazsa tuple olmaz #####
print(type(t))
t = "ali", "veli", 1, 2, 3.2, [1, 2, 3, 4]
t[1]
print(t[0:3])

# t[2] = 99  #hata verir tuple elemanları değiştirilemez

# Veri yapıları - Dictionary (sözlük)

# kapsayıcı,değiştirilebilir,sırasız
# listelerdeki gibi indexleme işlemleri yapılamaz
# key-value
sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

print(sozluk)

print(len(sozluk))

sozluk = {"REG": 10,
          "LOJ": 20,
          "CART": 30}

sozluk = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}

print(sozluk)
