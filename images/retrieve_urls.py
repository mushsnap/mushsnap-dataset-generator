
#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer
from urllib import request
import os
import pandas as pd


dir = './images/'


def fetch_url(url):
    url, name = url
    try:
        f = dir + name + os.sep + url.split('/')[-1]
        print(f)

        request.urlretrieve(url, f)
        return url, ''
    except Exception as e:
        return url, e


for csv in os.listdir("url"):
    urls = pd.read_csv(f"url/{csv}",
                       index_col=0)["0"].values.tolist()

    name = csv.split(".")[0]

    if not os.path.exists(dir + name):
        os.mkdir(dir + name)

    urls = [(url, name) for url in urls]

    results = ThreadPool(20).imap_unordered(
        fetch_url, urls)  # 20 threads

    for i, (url, resp) in enumerate(results):
        print('%g %r %s' % (i, url, resp))
    print(f"Done: {csv}")
