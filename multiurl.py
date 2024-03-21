

from bs4 import BeautifulSoup
import requests
import time

pages = ["Thriller_Bark_Arc","Fish-Man_Island_Arc","Water_7_Arc","Egghead_Arc","Enies_Lobby_Arc","Arabasta_Arc","Skypiea_Arc","Whole_Cake_Island_Arc","Dressrosa_Arc","Wano_Country_Arc"] # <--- Change this to the sub URLs of the pages you want to scrape

url = "onepiece.fandom.com/wiki/"

image_get = {}
for page in pages:
    start = time.time()
    opened = requests.get("https://"+url+page)
    soup = BeautifulSoup(opened.text, 'html.parser')
    image = soup.find_all('img', class_='pi-image-thumbnail')
    imagenew = str(image)
    src = imagenew.split('srcset="')[1].split('"')[0]
    src = src.split(' ')[2].split(' ')[0]
    cover = requests.get(src)
    if(cover.status_code == 200):
    #   with open(page+".jpg", "wb") as file:
    #     file.write(cover.content)
        file_path = "./images/" + page + ".jpg"
        with open(file_path, "wb") as file:
            file.write(cover.content)
    print("done "+page)
    end = time.time()
    print(end - start)
    continue

print("done")