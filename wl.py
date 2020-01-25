import requests
from bs4 import BeautifulSoup		#Kütüpheneleri tanımlıyoruz.
 
u = input("Lütfen url giriniz: \n")	#Wordlist oluşturulacak site url'si... 	
req = requests.get(u)			#url'e get isteği atıyoruz.
soup = BeautifulSoup(req.text, "lxml")	#BeautifulSoup ile sayfadaki html parsellerini alıyoruz.
soup = soup.find_all("p")		#find_all ile tüm p etiketlerini alıyoruz.
file = open('wordlist', 'w')		#wordlist dosyasını açıyoruz(yoksa oluşturuyoruz).
for i in soup:				#soup'da bulunan p etiketlerini for döngüsü ile tek tek alıyoruz.
	al = str(i.text)		#".text" ile taglerden arındırıyoruz.
	al = al.split()			#temiz içeriği parçalıyoruz
	for j in al:
		file.write(j + "\n")	#parçaları açmış olduğumuz wordlist dosyasına yazıyoruz.

file.close() 				#dosyayı kapatıyoruz.
print("wordlist başarılı bir şekilde oluşturuldu.")

"""
author: Yunus Emre DEMİR
"""
