
#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor
from time import time
from urllib import request
import os
import pandas as pd
from config import IMAGES_PATH, CSV_URL_PATH
from tqdm import tqdm


def fetch_url(url):
    """Download the url in the folder name given in the second index of url parameter

    Arguments:
        url {tuple} -- Two values the url itself and the name associated to it.

    Returns:
        url -- the url
    """
    url, name = url
    try:
        f = IMAGES_PATH + name + os.sep + url.split('/')[-1]
        request.urlretrieve(url, f)
        return url, ''
    except Exception as e:
        return url, e


t = time()
for csv in tqdm(os.listdir(CSV_URL_PATH)):
    if csv is None or csv[0] == '.':
        continue

    urls = pd.read_csv(f"{CSV_URL_PATH}/{csv}",
                       index_col=0)["0"].values.tolist()

    name = csv.split(".")[0]

    if not os.path.exists(IMAGES_PATH + os.sep + name):
        os.mkdir(IMAGES_PATH + os.sep + name)

    urls = [(url, name) for url in urls]

    results = ThreadPoolExecutor().map(fetch_url, urls)

    for i, (url, resp) in enumerate(results):
        pass

    print(f"Done: {csv}")

print(time() - t)
