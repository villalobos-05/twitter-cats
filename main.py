import tweepy
from typing import Union
from io import BytesIO
from fastapi import FastAPI
import os
app = FastAPI()

# Credentials
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authentication for API v1.1
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api_v1 = tweepy.API(auth)

# Configure client with credentials for API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# FUNCTIONS

# Upload image using API v1.1
def upload_twitter_image(imageBytes: BytesIO):

    try:
        media = api_v1.media_upload(filename="gato.jpg", file=imageBytes)
        mediaId: int = media.media_id
        print(f"Image uploaded successfully. Media ID: {mediaId}")
        return mediaId
    except tweepy.TweepyException as e:
        print(f"Error uploading image: {e}")

# Publish tweet with API v2
def publish_tweet(text: Union[str, None], mediasId: Union[list[int], None]):
    # Validations
    if ((text == None or not text) and (mediasId == None or not mediasId)):
        raise Exception("No parameters were added!")

    # Publish tweet
    try:
        response = client.create_tweet(text=text, media_ids=mediasId)
        print(f"Tweet successfully published: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Error publishing the tweet: {e}")

from cat import get_cat_image

def publish_cat():

    # Cat image
    imageFile: BytesIO = get_cat_image("")

    mediaId = upload_twitter_image(imageFile)
    publish_tweet(text="", mediasId=[mediaId])


if (__name__ == '__main__'):
    publish_cat()