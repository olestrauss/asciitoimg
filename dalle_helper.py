from openai import OpenAI
import urllib.request 
import os

class Dalle():
    def __init__(self):
        self.client = OpenAI()

    def generate_image(self, ascii):
        self.ascii = ascii

        self.response = self.client.images.generate(
            model="dall-e-3",
            prompt=f"Generate an image based on this ascii art: \n\n {self.ascii}",
            size="1024x1024",
            quality="standard",
            n=1
        )

        self.image_url = self.response.data[0].url
        self.image_path = self.download_and_save_image(self.image_url)
        return self.image_path

    def get_file_count(self):
        return len(os.listdir(os.path.join(os.getcwd(), 'output_images')))

    def download_and_save_image(self, image_url): # returns image path
        self.filename = f"output_images/IMAGE_{self.get_file_count()}.png"
        urllib.request.urlretrieve(image_url, self.filename)
        return self.filename