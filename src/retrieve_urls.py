import argparse
import os
import time
import pandas as pd

import requests
from flickrapi import FlickrAPI
from config import FLICKR_KEY, FLICKR_SECRET, DATASET, CSV_URL_PATH, IMAGE_SIZE, SPIECES_PATH


# Flickr API key https://www.flickr.com/services/apps/create/apply

def get_urls(search='honeybees on flowers', n=10, download=False):
    t = time.time()
    flickr = FlickrAPI(FLICKR_KEY, FLICKR_SECRET)
    photos = flickr.walk(text=search,  # http://www.flickr.com/services/api/flickr.photos.search.html
                         extras='url_' + IMAGE_SIZE,
                         per_page=100,
                         sort='relevance')

    if download:
        dir = os.getcwd() + os.sep + 'images' + os.sep + \
            search.replace(' ', '_') + os.sep  # save directory
        if not os.path.exists(dir):
            os.makedirs(dir)

    urls = []
    for i, photo in enumerate(photos):
        if i == n:
            break

        try:
            # construct url https://www.flickr.com/services/api/misc.urls.html
            url = photo.get('url_' + IMAGE_SIZE)  # SIZE

            if url is None:  # It has no of that size
                url = 'https://farm%s.staticflickr.com/%s/%s_%s_b.jpg' % \
                      (photo.get('farm'), photo.get('server'), photo.get(
                          'id'), photo.get('secret'))  # large size

            urls.append(url)
            print('%g/%g %s' % (i, n, url))
        except:
            print('%g/%g error...' % (i, n))

    if not download:
        dir = CSV_URL_PATH + search.replace(' ', '_') + ".csv"

        urls = pd.Series(urls)
        urls.to_csv(dir)

    print('Done. (%.1fs)' % (time.time() - t) +
          ('\nAll images saved to %s' % dir if download else ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=10, help='number of images')
    opt = parser.parse_args()

    with open(f"{SPIECES_PATH}/{DATASET}.txt", "r") as f:
        for search in f.readlines():
            search = search[:-1].split("(")[0].strip()
            print("'" + search + "'")
            get_urls(search=search,  # search term
                     n=opt.n)  # max number of images
