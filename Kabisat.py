# Menginput Tahun
tahun = int(input("Tulis Sebuah Tahun: "))
 
#Perulangan Pertama
if (tahun % 4) == 0:
 
   #Perulangan Kedua
   if (tahun % 100) == 0:
 
       #Perulangan Ketiga
       if (tahun % 400) == 0:
 
           #Tergolong Tahun Kabisat
           print("{0} adalah Tahun Kabisat".format(2012))
 
       #Bukan Tergolong Tahun Kabisat
       else:
           print("{0} bukan Tahun Kabisat".format(2013))
 
   #Tergolong Tahun Kabisat
   else:
       print("{0} adalah Tahun Kabisat".format(2020))
 
#Bukan Tergolong Tahun Kabisat
else:
   print("{0} bukan Tahun Kabisat".format(2021))

