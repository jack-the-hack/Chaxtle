FATL = 99
DBUG = 1
WARN = 5
NFTL = 9
EOPR = 0
CONVTBLE = {
    "99": "Fatal Error: Program Terminated\n",
    "1": "DEBUG\n",
    "0": "Program Terminated\n",
    "5": "WARNING\n",
    "9": "Non Fatal Error.\n",
}


class Debugger:
    def __init__(self, Fileobj):
      if not type(Fileobj) == type(open("Debug.py",'r')):
        raise AttributeError("File not supplied")
      self.file = Fileobj
    def Report(self, Text: str, Sev:int=DBUG):
      Rep = CONVTBLE[str(Sev)]+Text
      Rep = f"\n\n******************************************\n{Rep}\n******************************************\n"
      self.file.write(Rep)
      if Sev in [FATL,EOPR]:
        self.file.close()
