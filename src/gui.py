import tkinter as tk
from tk import *
from tkinter import filedialog
from haar_cascades import detect_faces
from utils.image_utils import *
import os

OUT_PATH = os.path.join(os.getcwd(), "output")

class FaceDetectionApp:
    def __init__(self,master):
        self.master = master
        master.title("Face Detecction App")
        self.select_image_button = tk.Button(master, text="Select Image", command=self.select_image, width=15, height=3)
        self.select_image_button.pack(pady=30)
        self.detect_faces_button = tk.Button(master, text="Detect Faces", command=self.detect_faces, width=15, height=3)
        self.detect_faces_button.pack(pady=30)

    def select_image(self):
        file_path = filedialog.askopenfilename(initialdir="images/", title="Select image", filetypes=(("Image files", "*.jpg; *.png"),("all files", "*.*")))
        if file_path:
            self.image_path = file_path
            self.original_image = load_image(file_path)
            display_image(self.original_image, "Original Image")
    
    def detect_faces(self):
        if hasattr(self, 'image_path'):
            detected_image = detect_faces(self.image_path)
            display_image(detected_image, "Detected Faces")
            save_image(detected_image, os.path.join(OUT_PATH, "out1.jpg"))
        else:
            print("Please select an image first.")
        
        


        
        
