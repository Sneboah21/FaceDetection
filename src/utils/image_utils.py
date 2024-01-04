import cv2

def load_image(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise OSError("Image could not be loaded!")
        return image
    except OSError as error:
        print(error.args[0])

def display_image(image, window_title="Image"):
    cv2.imshow(window_title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#display_image(load_image("./images/blah.png"))
def save_image(image, output_path):
     cv2.imwrite(output_path, image)
