import requests
from bs4 import BeautifulSoup
import os
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings


def download_image(search_query):
    query = '+'.join(search_query.split())
    url = f'https://www.google.com/search?hl=en&tbm=isch&q={query}'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not img_tags:
        print("No images found.")
        return None

    img_url = img_tags[1]['src']  # Skip the first image which is a placeholder
    
    
    img_response = requests.get(img_url)
    img_response.raise_for_status()

    # Save image locally
    image_name = f"{search_query.replace(' ', '_')}.png"
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    
    with open(image_path, 'wb') as file:
        file.write(img_response.content)

    # Construct the URL for the image
    image_url = os.path.join(settings.MEDIA_URL, image_name)
    
    return image_url
