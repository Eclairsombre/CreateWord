import csv
import json
import random

def parseDico():
    
    result = {
        "a":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "b":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "c":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "d":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "e":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "f":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "g":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "h":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "i":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "j":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "k":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "l":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "m":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "n":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "o":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "p":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "q":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "r":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "s":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "t":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "u":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "v":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "w":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "x":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "y":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "z":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        }
    }
    with open('Fr.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['a']
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
                if elt > 1:
                    if word[elt-2].lower() not in result:
                        continue
                    if word[elt-2].lower() not in result[letter]["LetterBeforeOne"]:
                        result[letter]["LetterBeforeOne"][word[elt-2].lower()] = 1
                    else:
                        result[letter]["LetterBeforeOne"][word[elt-2].lower()] += 1
    with open('output.json', 'w') as outfile:
        json.dump(result, outfile)
    
def countNbLetter():
    with open('Fr.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            for letter in row['a']:
                if letter.isalpha():
                    count += 1
        return count
    
def countNbWord():
        with open('Fr.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                count += 1
            return count
            
            
def statJson():
    result = {
        "a":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "b":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "c":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "d":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "e":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "f":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "g":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "h":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "i":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "j":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "k":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "l":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "m":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "n":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "o":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "p":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "q":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "r":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "s":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "t":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "u":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "v":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "w":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "x":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "y":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        },
        "z":{
            "PlaceInWord":{},
            "NbOccurence":0,
            "LetterBefore":{}, "LetterBeforeOne":{}
        }
    }
    with open('output.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for key in data:
            nbIteration = data[key]["NbOccurence"]
            for elt in data[key]["PlaceInWord"]:
                result[key]["PlaceInWord"][elt] = round((data[key]["PlaceInWord"][elt]/nbIteration) * 100, 3)
            for letter in data[key]["LetterBefore"]:
                result[key]["LetterBefore"][letter] = round((data[key]["LetterBefore"][letter]/nbIteration) * 100, 3)
            for letter in data[key]["LetterBeforeOne"]:
                result[key]["LetterBeforeOne"][letter] = round((data[key]["LetterBeforeOne"][letter]/nbIteration) * 100, 3)
            result[key]["NbOccurence"] = round((nbIteration / countNbLetter()) *100 ,3)
    with open('stat.json', 'w') as outfile:
        json.dump(result, outfile)



def getStatLetterForPostion(n):
    with open('stat.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        result = {}
        for key in data:
            if n in data[key]["PlaceInWord"]:
                result[key] = data[key]["PlaceInWord"][n]
        return result
    




def load_stats():
    with open('stat.json', 'r') as jsonfile:
        return json.load(jsonfile)
    
def choose_letter(prob_dict):
    letters = list(prob_dict.keys())
    probabilities = list(prob_dict.values())
    return random.choices(letters, probabilities)[0]

def generate_letter(stats, position=None, prev_letter=None, prev_letter_one=None):
    letter_probs = {}
    
    for letter, data in stats.items():
        prob = data["NbOccurence"]
        
        if position is not None:
            prob *= data["PlaceInWord"].get(str(position), 0)
        
        if prev_letter is not None:
            d = data["LetterBefore"].get(prev_letter, 0)
            if d <=1.0:
                prob *= 0.1
            else:
                prob *= data["LetterBefore"].get(prev_letter, 0)
            
        if prev_letter_one is not None:
            d= data["LetterBeforeOne"].get(prev_letter_one, 0)
            if d <=1.0:
                prob *= 0.1
            else:
                prob *= data["LetterBeforeOne"].get(prev_letter_one, 0)
        
        letter_probs[letter] = prob
    
    return choose_letter(letter_probs)
  
def generate_word(stats, length):
    word = ""
    for i in range(length):
        prev_letter = word[-1] if word else None
        prev_letter_one = word[-2] if len(word) > 1 else None
        word += generate_letter(stats, position=i, prev_letter=prev_letter, prev_letter_one=prev_letter_one)
    return word


if __name__ == "__main__":
    countNbWord()
    #parseDico()
    #statJson()
    
    stats = load_stats()

    temp = []
    for i in range(30):
        temp.append(generate_word(stats, random.randint(3, 10)))
    print(temp)
    #generate_letter(stats, position=0, prev_letter=None)
    