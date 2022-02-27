def filteroptions(myinput):
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
        "hahal_menu_option" : "/Content/Images/WebCodes/128px/hal.png",
        "low_carbon_footprint" : "/Content/Images/WebCodes/128px/lc.png",
        "high_carbon_footprint" : "/Content/Images/WebCodes/128px/hc.png"
    }

    import requests
    from bs4 import BeautifulSoup

    URL = "https://menu.dining.ucla.edu/Menus"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    entire_page = soup.find(id="main-content")
    food_items = entire_page.find_all("li", class_="menu-item")
    filter = []
    for each in myinput:
        filter.append(food_types[each])
    result = []
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