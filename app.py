from ascii_magic import AsciiArt
import os
from dotenv import load_dotenv
from PIL import Image 
from dalle_helper import Dalle
from image_resizer import Resizer
from tkinter import filedialog

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv()

    dalle = Dalle()
    resizer = Resizer()

    img_path = open_and_resize(resizer)
    ascii_str = to_ascii(img_path)
    to_image(ascii_str, dalle)
    show_image(dalle.image_path)


def open_and_resize(resize_object):
    image_path = filedialog.askopenfilename()
    resize_object.resize_image(image_path)
    return image_path

def to_ascii(image_path):
    my_art = AsciiArt.from_image(image_path)
    ascii_str = my_art.to_ascii(monochrome=True, columns=100)
    return ascii_str

def to_image(ascii_str, dalle_object):
    dalle_object.generate_image(ascii_str)
    
def show_image(image_path):
    img = Image.open(image_path)
    img.show()

if __name__ == "__main__":
    main()