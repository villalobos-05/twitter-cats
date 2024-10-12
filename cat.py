import requests
from io import BytesIO

CAT_URL = "https://cataas.com/cat"

def get_cat_image(text):

    # URL of the image
    if (text != ""):
        print(not text) 
        CAT_URL_FINAL = f"{CAT_URL}/says/{text}?font=Impact&fontSize=82&fontColor=%23e6eded&fontBackground=none"
    else:
        CAT_URL_FINAL = CAT_URL

    # Download image from URL to memory
    try:
        response = requests.get(CAT_URL_FINAL)
        response.raise_for_status()  # Verify that there was not an error on download
        image_data = BytesIO(response.content)  # Store image on buffer memory
        print("Image donwloaded successfully!")
        return image_data
    except requests.exceptions.RequestException as e:
        print(f"Error on image downloading: {e}")