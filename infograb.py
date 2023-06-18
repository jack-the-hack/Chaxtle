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
import itertools

def test(numbers):
    # Your implementation of the test function
    # ...
    pass

def generate_input_list(example_list, max_value, step_size):
    num_steps = int(max_value / step_size) + 1

    for bits in itertools.product([0, 1], repeat=len(example_list)):
        input_list = [round(example_list[i], 1) if bit else round(step_size * j, 1)
                      for i, (bit, j) in enumerate(zip(bits, range(num_steps)))]
        yield input_list

def find_best_input_list(example_list):
    max_ones = 0
    best_input_list = []

    max_value = 20
    step_size = 0.1

    for input_list in generate_input_list(example_list, max_value, step_size):
        classification = test(input_list)
        ones = classification.count(1)

        if ones > max_ones:
            max_ones = ones
            best_input_list = input_list

    return best_input_list

# Example usage:
example_list = [0.3, 5, 0.3, 0.5, 8, 0.005, 0.008, 0.010, 10, 2]
best_input = find_best_input_list(example_list)
classification = test(best_input)

print("Example List:", example_list)
print("Best Input List:", best_input)
print("Classification:", classification)
print("Number of 1s:", classification.count(1))
