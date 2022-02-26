import requests
from bs4 import BeautifulSoup

URL = "https://menu.dining.ucla.edu/Menus"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
entire_page = soup.find(id="main-content")
food_items = entire_page.find_all("li", class_="menu-item")

for food_item in food_items:
    title = food_item.find("a")
    icons = food_item.find_all("img")
    for img in icons:
        img_source = img["src"]
        if img_source== "/Content/Images/WebCodes/128px/v.png":
            print(title.text + " is vegeterian!")
            break