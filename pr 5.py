from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from random import randint

a=randint(0,10)


def response_films():
    response = requests.get("https://vlg.kinoafisha.info/").text
    soup = BeautifulSoup(response, "lxml")
    film = soup.find_all("a", class_="movieItem_title")
    film_digitals = soup.find_all("div", class_="movieItem_details")
    
    film_name = film[a].text
    film_details = film_digitals[a].text
    
    output.delete(1.0, END)
    output.insert(1.0, f"{film_name}\n{film_details}")

root = Tk()
root.title("KinoAfisha")
root.geometry("820x400")

label = Label(root, text="Нажмите для подборки фильма")
label.pack()

output = Text(root, width=100, height=10)
output.pack()

btn = ttk.Button(root, text="Показать", command=response_films)
btn.pack()

root.mainloop()