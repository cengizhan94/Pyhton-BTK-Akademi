from types import coroutine


website = "http://www.cengizhanuyar.com"
course="Python Kursu : Baştan sona python programlama rehberiniz (40 saat)"

#1)'course' karakter dizisinde kaç karakter bulunmaktadır?
result=len(course)
length=len(website)
#2)website içindeki 'www' karakterini alalım
result=website[7:10]

#3) website içindeki 'com' karakterini alalım
result=website[length-3:length]

#4)course içindeki ilk 15 ve son 15 karakterleri alalım (iki noktanın yeri çok önemli)
result=course[0:15]
result = course[:15]
result=course[-15:]
#5)'course' içindeki ifadeleri tersten yazdıralım
result=course[::-1]

firstName, lastName, age, job = 'Cengiz Han', 'Uyar', 27, 'Yazılımcı'

result='Hi my name is '+firstName+" "+lastName+","+" Yaşım "+str(age)+" ve mesleğim "+job+"."#<int bir değeri + işareti ile birleştirmek istiyorsak age'i str ile parantez içine alabiliriz.

result = "Hi my name is {0} {1}, ben {2} yaşındayım. mesleğim ise {3}".format(firstName,lastName,age,job)

#7) 'Hello world' ifadesindeki 'w' harfini 'W' olarak değiştirelim.'
s="Hello world"
s=s[0:6] + 'W' + s[-4:]
s.replace('w','W')
print(s)

#8) 'abc ifadesini yan yana 3 defa yazdıralım'

result = 'abc' * 3 

print(result)