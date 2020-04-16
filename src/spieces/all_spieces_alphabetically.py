

import selenium
from selenium import webdriver

wd = webdriver.Chrome()

spieces = []

wd.get(f"http://www.mushroom.world/mushrooms/namelist")
for div in wd.find_elements_by_class_name("item"):
    spieces.append(div.find_element_by_css_selector("a").text)

print(spieces)

with open("data/all_spieces_alphabetically.txt", "w") as e:
    for s in spieces:
        e.write(s + "\n")
    e.close()
