name="Emir"
surname="Yılmaz"
age=str(23)
tanit='My name is '+name+" "+surname+" and\nI am "+age+" years old"
# \n kodu string ifadesini alt satıra indirir
print(tanit)
lenght=len(tanit)
print(len(tanit))
# len methodu str dizisinin kaç karakterli olduğunu gösterir.
print(tanit[lenght-1])
print(tanit[-1])
#[] işareti indeks belirtir, indeks 0 dan başlar en sondaki indeks için ise -1 çağırılır.
print(tanit[25:31]),print(tanit[1:20:3])
# [sayi:sayi] şeklinde indeks aralığı belirtilir. , [1:20:3] şeklinde ise sondaki sayı kaç karakterde bir alması gerektiğini belirleriz.






