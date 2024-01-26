# Embed all local artifacts into your nbconverted Jupyter Notebook for single file presentation and sharing
import base64
import sys
from bs4 import BeautifulSoup
import mimetypes
import os

def embed_images_in_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for img_tag in soup.find_all('img'):
        img_path = img_tag['src']
        mime_type, _ = mimetypes.guess_type(img_path)
        with open(img_path, 'rb') as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        img_tag['src'] = f"data:{mime_type};base64,{encoded_string}"

    # Save the modified HTML with embedded images
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [HTML_FILE]")
        sys.exit(1)

    html_file = sys.argv[1]
    embed_images_in_html(html_file)
