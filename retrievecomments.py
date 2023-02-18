import os
import json

from googleapiclient.discovery import build
from os.path import join, dirname
from dotenv import load_dotenv

class RetrieveComments:

    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    
    def __init__(self, url: str):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        apiKey = os.getenv("YOUTUBE_API_KEY")
        self.youtube = build("youtube", "v3", developerKey=apiKey)
        #get the video id 
        self.videoId = url.split("?v=")[1]
        # self.channelId = "UCpi8TJfiA4lKGkaXs__YdBA"

    def getComments(self) -> list:
        comments = [] 

        request = self.youtube.commentThreads().list(
            part = "snippet",
            videoId = self.videoId
        )

        response = request.execute() 

        # print(response)

        while response:

            # print(response["items"][0]["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

            for i in response["items"]:
                comments.append(i["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

            if "nextPageToken" in response:
                response = self.youtube.commentThreads().list(
                    part = "snippet",
                    videoId = self.videoId,
                    maxResults = 50,
                    pageToken = response["nextPageToken"]
                ).execute()
            else:
                break

        return comments
        
    def getVideoTitle(self) -> str:
        request = self.youtube.videos().list(
            part = "snippet",
            id = self.videoId
        )

        response = request.execute()

        return response["items"][0]["snippet"]["title"]