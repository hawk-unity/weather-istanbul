from bs4 import BeautifulSoup
import requests
import datetime
import os
import tkinter as tk
r = requests.get("http://www.havadurumu15gunluk.net/havadurumu/istanbul-hava-durumu-15-gunluk.html")
soup = BeautifulSoup(r.content)
os.system("cls")
print("Kaç Derece: ")
find = soup.find("strong",attrs={"class":"strong2"})
print(find.text)
find2 = soup.find("strong",attrs={'class':'strong3'})
print("Durum : ")
print(find2.text)
#tarihler
trh = datetime.datetime.now()
ay = trh.month
yil = trh.year
gun = trh.day
print("Tarih: ", gun,ay,yil)

i=tk.Tk()
i.configure(background='black')
i.title("MULTİ TOOL : H4WK OFCX")
greeta = tk.Label(i,text=("Derece : ", find.text) ,font='Verdana 40', bg="black" , fg="white")
greeta.grid(column=0, row=1)
greeta2 = tk.Label(i,text=("Açık / Kapalı :", find2.text) ,font='Helvatica 40', bg="black" , fg="white")
greeta2.grid(column=0, row=2)
greeta2 = tk.Label(i,text=("Tarih: ", gun,ay,yil) ,font='Verdana 40', bg="black" , fg="white")
greeta2.grid(column=0, row=3)
i.mainloop()
