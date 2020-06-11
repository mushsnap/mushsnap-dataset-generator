

import selenium
from selenium import webdriver


if __name__ == "__main__":
    wd = webdriver.Chrome()

    spieces = []

    for i in range(6):
        wd.get(f"http://www.mushroom.world/mushrooms/list?page={i}")
        for div in wd.find_elements_by_class_name("infolink"):
            spieces.append(div.find_element_by_css_selector("a").text)

    print(spieces)

    with open("data/all_spieces.txt", "w") as e:
        for s in spieces:
            e.write(s + "\n")
        e.close()
