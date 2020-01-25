import requests
from bs4 import BeautifulSoup
 
u = input("Lütfen url giriniz: \n")
req = requests.get(u)
soup = BeautifulSoup(req.text, "lxml")
soup = soup.find_all("p")
file = open('wordlist', 'w')

for i in soup:
	al = str(i.text)
	al = al.split()
	for j in al:
		file.write(j + "\n")

file.close() 
print("wordlist başarılı bir şekilde oluşturuldu")
