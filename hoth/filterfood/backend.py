def filteroptions(myinput, month = -1, day = -1, year = -1, meal = "", dininghall = ""):
    food_types = {
        "Vegetarian Menu Option" : "/Content/Images/WebCodes/128px/v.png",
        "Vegan Menu Option" : "/Content/Images/WebCodes/128px/vg.png",
        "Contains Peanuts" : "/Content/Images/WebCodes/128px/apnt.png",
        "Contains Tree Nuts" : "/Content/Images/WebCodes/128px/atnt.png",
        "Contains Wheat" : "/Content/Images/WebCodes/128px/awht.png",
        "Contains Gluten" : "/Content/Images/WebCodes/128px/agtn.png",
        "Contains Soy" : "/Content/Images/WebCodes/128px/asoy.png",
        "Contains Dairy" : "/Content/Images/WebCodes/128px/amlk.png",
        "Contains Eggs" : "/Content/Images/WebCodes/128px/aegg.png",
        "Contains Crustacean Shellfish" : "/Content/Images/WebCodes/128px/acsf.png",
        "Contains Fish" : "/Content/Images/WebCodes/128px/afsh.png",
        "Halal Menu Option" : "/Content/Images/WebCodes/128px/hal.png",
        "Low Carbon Footprint" : "/Content/Images/WebCodes/128px/lc.png",
        "High Carbon Footprint" : "/Content/Images/WebCodes/128px/hc.png"
    }

    import requests
    import datetime
    import time
    from bs4 import BeautifulSoup

    if day == -1:
        mydate = datetime.date.fromtimestamp(time.time())
    else:
        mydate = datetime.datetime(year, month, day)
    str = mydate.isoformat()
    timenow = datetime.datetime.now()
    hournow = timenow.hour
    if meal == "":
        if hournow < 11:
            meal = "Breakfast"
        elif hournow < 15:
            meal = "Lunch"
        else: meal = "Dinner"
    URL = "https://menu.dining.ucla.edu/Menus/" + str
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    entire_page = soup.find(id="main-content")
    if meal == "Breakfast":
        dining_halls = entire_page.find_all("div", class_="menu-block half-col")
    else:
        dining_halls = entire_page.find_all("div", class_="menu-block third-col")
    if meal == "Dinner":
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

# array = filteroptions(["Vegetarian Menu Option"])
# print(array)