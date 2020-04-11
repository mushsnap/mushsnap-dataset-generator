import argparse
import os
import time
import pandas as pd

import requests
from flickrapi import FlickrAPI

# Flickr API key https://www.flickr.com/services/apps/create/apply
key = '6ef690766cf433e07fe6e7560d6fdf08'
secret = '25b6843554095fc4'

DATASET = 'all_spieces_alphabetically'


def download_uri(uri, dir='./'):
    with open(dir + uri.split('/')[-1], 'wb') as f:
        f.write(requests.get(uri, stream=True).content)


def get_urls(search='honeybees on flowers', n=10, download=False):
    t = time.time()
    flickr = FlickrAPI(key, secret)
    photos = flickr.walk(text=search,  # http://www.flickr.com/services/api/flickr.photos.search.html
                         extras='url_o',
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
            url = photo.get('url_o')  # original size
            if url is None:
                url = 'https://farm%s.staticflickr.com/%s/%s_%s_b.jpg' % \
                      (photo.get('farm'), photo.get('server'), photo.get(
                          'id'), photo.get('secret'))  # large size

            # download
            if download:
                download_uri(url, dir)

            urls.append(url)
            print('%g/%g %s' % (i, n, url))
        except:
            print('%g/%g error...' % (i, n))

    if not download:
        dir = os.getcwd() + os.sep + 'url' + os.sep + \
            search.replace(' ', '_') + ".csv"

        urls = pd.Series(urls)
        urls.to_csv(dir)

    print('Done. (%.1fs)' % (time.time() - t) +
          ('\nAll images saved to %s' % dir if download else ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--search', type=str, default='honeybees on flowers', help='flickr search term')
    parser.add_argument('--n', type=int, default=10, help='number of images')
    parser.add_argument('--download', action='store_true',
                        help='download images')
    opt = parser.parse_args()

    with open(f"../spieces/data/{DATASET}.txt", "r") as f:
        for search in f.readlines():
            search = search[:-1].split("(")[0].strip()
            print("'" + search + "'")
            get_urls(search=search,  # search term
                     n=opt.n,  # max number of images
                     download=opt.download)  # download images
