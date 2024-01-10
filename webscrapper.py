
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

basliklar = soup.find_all("h1")

for baslik in basliklar:
    print(baslik.text)