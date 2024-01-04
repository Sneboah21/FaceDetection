import os
from haar_cascades import detect_faces
from utils.image_utils import *  #"*" imports all methods

IMG_PATH = os.path.join(os.getcwd(), "images", "img1.jpg")
OUT_PATH = os.path.join(os.getcwd(), "output")

if __name__ == "__main__":
    detected_image = detect_faces(IMG_PATH)
    display_image(detected_image, "Detected image")
    save_image(detected_image, os.path.join(OUT_PATH, "out1.jpg"))
