#VERI YAPILARI

#Listeler

#[]
#list()

notlar = [70,85,90,60]
liste = ["a",19.3,90]
list_genis = ["a",19.3,90, notlar]

print(len(list_genis))

print(type(notlar))

print(type(list_genis[2]))

tum_liste = [liste,list_genis]
 #del tum_liste


#Listeler - Eleman Islemleri

liste1=[10,20,30,40,50]
liste1[0]
liste1[1]
#liste1[6]

liste1[0:2] #0dan 2 ye kadar  
liste1[:2] #0dan 2 ye kadar

liste1[2:] #2den sona kadar

liste2=["a",10,[10,20,30,40,50]]
liste2[2]

liste2[0:2]
liste2[2][4] #50

#Listeler - Eleman Değiştirme

liste3 = ["ali","veli","berkcan","ayse"]

liste3[1] = "velinin-babasi"

liste3[0:3]= "alinin_babasi","velinin_babasi","berkcanin_babasi"
print(liste3)

liste3 = ["ali","veli","berkcan","ayse"]
liste3 + ["kemal"]
print(liste3)
liste3 = liste3 + ["kemal"]
liste3.append("kemal")
print(liste3)
del liste3[4]
liste3.remove("kemal")
liste3.pop(2)
print(liste3)
