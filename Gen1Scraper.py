import requests
from bs4 import BeautifulSoup
#gen1=open("gen1.txt","w")

count=1
url = "https://pokemon.fandom.com/wiki/List_of_Generation_I_Pok%C3%A9mon"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="wikitable")
pokemons = results.find_all("a")
for pokemon in pokemons:
    if count==0:
        print(pokemon.get_text("title"))
        # gen1.write(pokemon.get_text("title"))
        # gen1.write("\n")
        count=1
    if pokemon.get_text("title")=="":
        count=0
input()
#gen1.close()