from unittest import result


def filteroptions(myinput, month = -1, day = -1, year = -1, meal = "", dininghall = ""):
    food_types = {
        "vegetarian" : "/Content/Images/WebCodes/128px/v.png",
        "vegan" : "/Content/Images/WebCodes/128px/vg.png",
        "contains_peanuts" : "/Content/Images/WebCodes/128px/apnt.png",
        "contains_tree_nuts" : "/Content/Images/WebCodes/128px/atnt.png",
        "contains_wheat" : "/Content/Images/WebCodes/128px/awht.png",
        "contains_gluten" : "/Content/Images/WebCodes/128px/agtn.png",
        "contains_soy" : "/Content/Images/WebCodes/128px/asoy.png",
        "contains_dairy" : "/Content/Images/WebCodes/128px/amlk.png",
        "contains_eggs" : "/Content/Images/WebCodes/128px/aegg.png",
        "contains_crustacean_shellfish" : "/Content/Images/WebCodes/128px/acsf.png",
        "contains_fish" : "/Content/Images/WebCodes/128px/afsh.png",
        "halal_menu_option" : "/Content/Images/WebCodes/128px/hal.png",
        "low_carbon_footprint" : "/Content/Images/WebCodes/128px/lc.png",
        "high_carbon_footprint" : "/Content/Images/WebCodes/128px/hc.png"
    }

    import requests
    import datetime
    from datetime import date
    from datetime import datetime
    from datetime import time
    from bs4 import BeautifulSoup
    if day == -1:
        mydate = date.today()
    else:
        mydate = datetime.datetime(year, month, day)
    str = date.isoformat(mydate)
    timenow = datetime.now().time()
    hournow = timenow.hour
    if meal == "":
        if hournow < 11:
            meal = "breakfast"
        elif hournow < 15:
            meal = "lunch"
        else: meal = "dinner"
    URL = "https://menu.dining.ucla.edu/Menus/" + str
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    entire_page = soup.find(id="main-content")
    if meal == "breakfast":
        dining_halls = entire_page.find_all("div", class_="menu-block half-col")
    else:
        dining_halls = entire_page.find_all("div", class_="menu-block third-col")
    if meal == "dinner":
        dining_halls.pop(0)
        dining_halls.pop(0)
        dining_halls.pop(0)
    filter = []
    for each in myinput:
        filter.append(food_types[each])
    result = []
    for dining_hall in dining_halls:
        dininghallname = dining_hall.find("h3")
        food_items = dining_hall.find_all("li", class_="menu-item")
        if dininghallname.text == dininghall or dininghall == "":
            for food_item in food_items:
                title = food_item.find("a")
                icons = food_item.find_all("img")
                f = True
                for each in filter:
                    f2 = False
                    for img in icons:
                        img_source = img["src"]
                        if img_source == each:
                            f2 = True
                    if (not f2):
                        f = False 
                if f:
                    result.append(title.text)
    return result
