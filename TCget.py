import json
from Debug import *

bugger=Debugger(open("DEBUG.txt",'a+'))
bugger.Report("TCget Imported")
def lcomp(x: list, y: list):
    cmn = False
    if (x in y) or (y in x):
        cmn = True
    else:
        for z in x:
            for yz in y:
                if yz == z:
                    cmn = True
                    break
    print(cmn)
    if not cmn:
        return False
    else:
        return True


File = open("Trainchain.json", "r+")
print(type(File))
tcjson = json.load(File)


def Pull(Filters: dict, Prompt=""):
    assert type(Prompt) == str
    possible = []
    possibler = []
    required = []
    for Chain in tcjson["Chains"]:
        Chain = Chain["Conv"]
        if Prompt:
            for tple in Chain:
                if Prompt == tple["tple"][0]:
                    possibler.append(tple)
        if "Cat" in Filters.keys():
            if possibler:
                for tple in possibler:
                    print("\n")
                    print(Filters["Cat"].split(","))
                    print("\n")
                    print(tple["PTYPE"].split(","))
                    if lcomp(Filters["Cat"].split(","), tple["PTYPE"].split(",")):
                        print(1)
                        possible.append(tple)
            else:
                for tple in Chain:
                    if lcomp(Filters["Cat"].split(","), tple["PTYPE"].split(",")):
                        possible.append(tple)
        if "UAID" in Filters.keys():
            if possibler:
                for tple in possibler:
                    if Filters["UAID"] == int(tple["UAID"]):
                        possible.append(tple)
            else:
                for tple in Chain:
                    if Filters["UAID"] == int(tple["UAID"]):
                        possible.append(tple)
        if "AREQ" in Filters.keys():
            if possibler:
                for tple in possibler:
                    if bool(Filters["AREQ"]) == bool(tple["Ansreq"]):
                        required.append(tple)
            else:
                for tple in Chain:
                    if bool(Filters["AREQ"]) == bool(tple["Ansreq"]):
                        possible.append(tple)
    print(possibler)
    print(str(possible) + "***")
    if required:
        return required
    elif possible:
        return possible
    else:
        return None

def bye():
  bugger.Report("Termiated.",EOPR)