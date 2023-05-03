import numpy
import requests
import openai
import moviepy
import os
import json
from bs4 import BeautifulSoup
import time
import textblob
import TCget
from Debug import *

Bugg=Debugger(open("MainDEBUG.txt",'a+'))
Trainfile = open("Trainchain.json", "r+")
Chainy = json.load(Trainfile)
Chains = Chainy["Chains"]
punctrep = [".", ",", "!", "*", "?"]
Bugg.Report("Initialized.",)

class AIinst:
    def __init__(self):
        self.chain = []

    def Promptin(self, Prompt):
        Resp = ""
        Prompt = str((Prompt.lower()))
        while Prompt[-1] in punctrep:
            Prompt = Prompt[:-1]
        Bugg.Report(f"Prompt: {Prompt} \n Prompt type: {type(Prompt)}")
        if not self.chain:
            pResp = TCget.Pull({"Cat": "NSPEC,INTRO", "AREQ": True}, Prompt)
            Bugg.Report(f"pResp: {pResp}")
            if pResp:
              if len(pResp) > 1:
                # Multiple responses
                pass
              else:
                Resp = pResp[0]["tple"][1]
            if not Resp:
              # MAGIC-HAPPENS-HERE
              pass
            self.chain.append([Prompt,Resp])
            return Resp
    def Terminate():
      json.dump(Chainy,Trainfile)
      Trainfile.close()
      Bugg.Report("Terminated,Saved.",EOPR)
      TCget.bye()