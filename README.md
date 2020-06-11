<h1 align="center">Welcome to mushsnap-dataset-generator 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="docurl" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>



> This repository provides python script to scrap information from websites. First we have use selenium with chrome to gather data in the raw format. And after that we have used a specific library to gather images from FLICKR. All this data has been gathered to apply Deep learning on it and be able to create an AI capable of differentiate inedible and edible mushrooms.

### 🏠 [MushSnap](https://mailchi.mp/652773124a95/mushsnap)

MushSnap is an App that uses Deep learning to recognize edible and poisonous mushrooms.

## Install

```sh
pip install -r requirements.txt
```

## Usage

You have all available execution commands in the Makefile.

```sh
# Makefile rules
```

## Explanation

1. Retrieve spieces (names to look) - 139 spieces
2. Retrieve urls
3. Retrieve images
4. Order images
5. Zip images

Once you have the images in the zip you can send them to the training environment to start with the AI-process.

### Libraries

To execute all the tasks to retrieve all aspects i have use scrapper libreries such as Selenium for Websites with the ChromeDriver and Flickr to retrieve the images.

### References

- [Selenium](https://www.selenium.dev/)
- [Chrome Driver](https://chromedriver.chromium.org/)
- [Flickr api](https://www.flickr.com/services/api/misc.urls.html)
- [Spieces](http://www.mushroom.world/mushrooms)

## Author

👤 **ospinooo**

* Website: https://ospino.me
* Github: [@ospinooo](https://github.com/ospinooo)
* LinkedIn: [@pabloospino](https://linkedin.com/in/pabloospino)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_