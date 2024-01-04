import cv2
import numpy as np
from utils.image_utils import load_image

def detect_faces(image_path):
    #Load the image
    image = load_image(image_path)   #returns a matrix
    #Convert the image to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6) #Here tuple would be returned
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image