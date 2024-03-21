from bs4 import BeautifulSoup
import requests


url = "https://onepunchman.fandom.com/wiki/Saitama" # <--- Change this to the URL of the page you want to scrape
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')
image = soup.find_all('img', class_='pi-image-thumbnail')
print(type(image))
imagenew = str(image)
print(type(imagenew))
print(imagenew)
print
src = imagenew.split('srcset="')[1].split('"')[0]
src = src.split(' ')[2].split(' ')[0]
print(src)
cover = requests.get(src)
print(type(cover))
print(cover.status_code)
if(cover.status_code == 200):
    with open("cover.jpg", "wb") as file:
        file.write(cover.content)
