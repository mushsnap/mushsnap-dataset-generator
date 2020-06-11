from config import SPIECES_PATH, IMAGES_PATH, DATASET_PATH
import shutil
import os


spieces = {}

edible = open(f"{SPIECES_PATH}/edible_spieces.txt", "r").read().splitlines()
inedible = open(f"{SPIECES_PATH}/inedible_spieces.txt",
                "r").read().splitlines()
poisonous = open(f"{SPIECES_PATH}/poisonous_spieces.txt",
                 "r").read().splitlines()


def move_folder_images(mushroom_spiece: str, folder: str):

    folder_name = mushroom_spiece.replace(" ", "_")
    try:

        for images_path in os.listdir(f"{IMAGES_PATH}{folder_name}"):
            shutil.copy(
                f"{IMAGES_PATH}{folder_name}/{images_path}",
                f"{DATASET_PATH}{folder}"
            )

    except Exception as e:
        print(e)


list(map(lambda e: move_folder_images(e, 'edible'), edible))
list(map(lambda e: move_folder_images(e, 'poisonous'), inedible))
list(map(lambda e: move_folder_images(e, 'poisonous'), poisonous))
