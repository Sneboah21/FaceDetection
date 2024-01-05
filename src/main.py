import os
#from haar_cascades import detect_faces
#from utils.image_utils import *  #"*" imports all methods
from gui import FaceDetectionApp
import tkinter as tk

#IMG_PATH = os.path.join(os.getcwd(), "images", "img1.jpg")
#OUT_PATH = os.path.join(os.getcwd(), "output")

if __name__ == "__main__":
    root = tk.Tk()
    # root.winfo_width = 1000
    # root.winfo_height = 1000
    root.geometry("1080x600+200+200")
    root.configure(bg="#2d2d2d")
    app = FaceDetectionApp(root)
    root.mainloop()



    #detected_image = detect_faces(IMG_PATH)
    #display_image(detected_image, "Detected image")
    #save_image(detected_image, os.path.join(OUT_PATH, "out1.jpg"))
