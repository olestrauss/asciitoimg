from PIL import Image

class Resizer:
    def __init__(self, max_width=1000):
        self.max_width = max_width

    def resize_image(self, path):
        with Image.open(path) as img:
            width_percent = (self.max_width / float(img.size[0]))
            new_height = int((float(img.size[1]) * float(width_percent)))

            if img.size[0] > self.max_width:
                img = img.resize((self.max_width, new_height), Image.LANCZOS)
            else:
                new_height = img.size[1]

            img.save(path)