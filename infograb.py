import numpy
import requests
import openai
import moviepy
from pytube import YouTube
import os
import json
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch,Transcript
import time
video_ids=[]
def grabyt(searchtype,search:str):
  videosSearch = VideosSearch(search, limit = 10).result()
  print(videosSearch)
  for vid in videosSearch['result']:
    video_ids.append(vid['id'])
  # Download the videos as MP4 files
  print(video_ids)
  for video_id in video_ids:
    try:
      yt = Transcript.get(f"https://www.youtube.com/watch?v={video_id}")
      
      print(f"Failed to download video '{video_id}': {e}")
def grabgvids(searchtype,search):
  pass
def grabgtext(searchtype,search):
  pass
def refergpt(searchtype,search):
  pass
