import os


FLICKR_KEY = '6ef690766cf433e07fe6e7560d6fdf08'
FLICKR_SECRET = '25b6843554095fc4'

DATASET = 'all_spieces_alphabetically'

CSV_URL_PATH = os.getcwd() + '/../data/url_csv/'
IMAGES_PATH = os.getcwd() + '/../data/spieces/'
SPIECES_PATH = os.getcwd() + '/spieces/data'

# Image Flickr Size
# Depending on the size of the network

IMAGE_SIZE = 'n'

#  The letter suffixes are as follows:
#  s	small square 75x75
#  q	large square 150x150
#  t	thumbnail, 100 on longest side
#  m	small, 240 on longest side *********OK**********
#  n	small, 320 on longest side *********OK**********
#  -	medium, 500 on longest side
#  z	medium 640, 640 on longest side *********OK*********+ (Bigger networks)
#  c	medium 800, 800 on longest side†
#  b	large, 1024 on longest side*
#  h	large 1600, 1600 on longest side†
#  k	large 2048, 2048 on longest side†
#  o	original image, either a jpg, gif or png, depending on source format
