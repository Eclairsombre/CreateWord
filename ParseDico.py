import csv
import json

def parseDico():
    
    result = {
        "a":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "b":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "c":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "d":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "e":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "f":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "g":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "h":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "i":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "j":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "k":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "l":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "m":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "n":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "o":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "p":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "q":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "r":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "s":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "t":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "u":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "v":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "w":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "x":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "y":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        },
        "z":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}
        }
    }
    with open('dictionary.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['A']
            for elt in range(0, len(word)):
                letter = word[elt].lower()
                if letter not in result:
                    continue
                if elt not in result[letter]["PlaceInWord"]:
                    result[letter]["PlaceInWord"][elt] = 1
                else:
                    result[letter]["PlaceInWord"][elt] += 1
                result[letter]["NbOccurence"] += 1
                if elt > 0:
                    if word[elt-1].lower() not in result:
                        continue
                    if word[elt-1].lower() not in result[letter]["LetterBefore"]:
                        result[letter]["LetterBefore"][word[elt-1].lower()] = 1
                    else:
                        result[letter]["LetterBefore"][word[elt-1].lower()] += 1
    with open('output.json', 'w') as outfile:
        json.dump(result, outfile)
    
    

if __name__ == "__main__":
    
    parseDico()