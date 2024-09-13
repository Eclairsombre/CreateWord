import csv
import json
import random


def parseDico(dico, nameOutput):
    """Parse the dico and create a json file with the stats of the dico

    Args:
        dico (String): The name of the dico
        nameOutput (_type_): The name of the output file
    """

    result = {chr(i): {"PlaceInWord": {}, "NbOccurence": 0, "LetterBefore": {}, "Combinaison": {
    }, "CombinaisonPlusOne": {}, "EndWord": 0} for i in range(ord('a'), ord('z')+1)}
    prefixe = {}
    with open('Dico/' + dico, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['word']
            if len(word) < 3:
                continue
            if word[0].upper() + word[1].lower() not in prefixe:
                prefixe[word[0].upper() + word[1].lower()] = 1
            else:
                prefixe[word[0].upper() + word[1].lower()] += 1

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
                    combination = word[elt-2].lower() + word[elt-1].lower()
                    if combination not in result[letter]["Combinaison"]:
                        result[letter]["Combinaison"][combination] = 1
                    else:
                        result[letter]["Combinaison"][combination] += 1
                if elt > 2:
                    if word[elt-3].lower() not in result:
                        continue
                    combination = word[elt-3].lower() + \
                        word[elt-2].lower() + word[elt-1].lower()
                    if combination not in result[letter]["CombinaisonPlusOne"]:
                        result[letter]["CombinaisonPlusOne"][combination] = 1
                    else:
                        result[letter]["CombinaisonPlusOne"][combination] += 1
                if elt == len(word)-1:
                    result[letter]["EndWord"] += 1
    with open('Stats/' + nameOutput, 'w') as outfile:
        json.dump(result, outfile)
    with open("Stats/Prefixe" + nameOutput, 'w') as outfile:
        json.dump(prefixe, outfile)


def countNbLetter(dico):
    """Count the number of letter in the dico

    Args:
        dico (String): THe name of the dico

    Returns:
        Int: The number of letter in the dico
    """
    with open('Dico/' + dico, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            for letter in row['word']:
                if letter.isalpha():
                    count += 1
        return count


def countNbWord(dico):
    """Count the number of word in the dico

    Args:
        dico (String): The name of the dico

    Returns:
        Int: The number of word in the dico
    """
    with open('Dico/' + dico, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            count += 1
        return count


def statJson(dico, nameOutput, nameStat):
    """Create the stat json file with the percentage of each letter

    Args:
        dico (String): The name of the dico
        nameOutput (String): The name of the output file
        nameStat (String): The name of the stat file
    """
    result = {chr(i): {"PlaceInWord": {}, "NbOccurence": 0, "LetterBefore": {}, "Combinaison": {
    }, "CombinaisonPlusOne": {}, "EndWord": 0} for i in range(ord('a'), ord('z')+1)}

    with open('Stats/' + nameOutput, 'r') as jsonfile:
        data = json.load(jsonfile)
        for key in data:
            nbIteration = data[key]["NbOccurence"]
            for elt in data[key]["PlaceInWord"]:
                result[key]["PlaceInWord"][elt] = round(
                    (data[key]["PlaceInWord"][elt]/nbIteration) * 100, 3)
            for letter in data[key]["LetterBefore"]:
                result[key]["LetterBefore"][letter] = round(
                    (data[key]["LetterBefore"][letter]/nbIteration) * 100, 3)
            for letter in data[key]["Combinaison"]:
                result[key]["Combinaison"][letter] = round(
                    (data[key]["Combinaison"][letter]/nbIteration) * 100, 3)
            for letter in data[key]["CombinaisonPlusOne"]:
                result[key]["CombinaisonPlusOne"][letter] = round(
                    (data[key]["CombinaisonPlusOne"][letter]/nbIteration) * 100, 3)
            result[key]["NbOccurence"] = round(
                (nbIteration / countNbLetter(dico)) * 100, 3)
            result[key]["EndWord"] = round(
                (data[key]["EndWord"] / countNbWord(dico)) * 100, 3)

    with open('Stats/' + nameStat, 'w') as outfile:
        json.dump(result, outfile)

    with open("Stats/Prefixe" + nameOutput, 'r') as jsonfile:
        data = json.load(jsonfile)
        for key in data:
            data[key] = round((data[key] / countNbWord(dico)) * 100, 3)
    with open("Stats/Prefixe" + nameStat, 'w') as outfile:
        json.dump(data, outfile)


def getStatLetterForPostion(n, nameStat):
    """Get the stat of the letter for a specific position

    Args:
        n (Int): The position
        nameStat (String): The name of the stat file

    Returns:
        Float: The percentage of the letter for the position
    """
    with open('Stats/'  + nameStat, 'r') as jsonfile:
        data = json.load(jsonfile)
        result = {}
        for key in data:
            if n in data[key]["PlaceInWord"]:
                result[key] = data[key]["PlaceInWord"][n]
        return result


def load_stats(nameStat):
    """Load the stat file

    Args:
        nameStat (String): The name of the stat file

    Returns:
        JsonFile: The stat file
    """
    with open('Stats/' + nameStat, 'r') as jsonfile:
        return json.load(jsonfile)


def choose_letter(prob_dict):
    """Choose a letter based on the probability

    Args:
        prob_dict (Dictionnary): The probability of each letter

    Returns:
        Char: The letter chosen
    """
    letters = list(prob_dict.keys())
    probabilities = list(prob_dict.values())
    return random.choices(letters, probabilities)[0]


def generate_letter(stats, position=None, word=None):
    """Generate a letter based on the stats

    Args:
        stats (Dictionnary): The stats
        position (Int, optional): The potion of the letter to generate. Defaults to None.
        word (String, optional): The word who are currently generating. Defaults to None.

    Returns:
        Char: The letter generated
    """
    letter_probs = {}
    endWord = False
    prev_letter = word[-1] if word else None
    prev_letter_one = word[-2] if len(word) > 1 else None
    prev_letter_one_two = word[-3] if len(word) > 2 else None
    for letter, data in stats.items():
        prob = data["NbOccurence"]

        if position is not None:
            prob *= data["PlaceInWord"].get(str(position), 0)

        if prev_letter is not None:
            d = data["LetterBefore"].get(prev_letter, 0)
            if d <= 1.0:
                prob *= 0.1
            else:
                prob *= data["LetterBefore"].get(prev_letter, 0)

        if prev_letter_one is not None:
            d = data["Combinaison"].get(prev_letter_one+prev_letter, 0)
            if d <= 1.0:
                prob *= 0.1
            else:
                prob *= data["Combinaison"].get(prev_letter_one+prev_letter, 0)

        if prev_letter_one_two is not None:
            d = data["CombinaisonPlusOne"].get(
                prev_letter_one_two+prev_letter_one+prev_letter, 0)
            if d <= 1.0:
                prob *= 0.1
            else:
                prob *= data["CombinaisonPlusOne"].get(
                    prev_letter_one_two+prev_letter_one+prev_letter, 0)

        letter_probs[letter] = prob

    l = choose_letter(letter_probs)
    StatEndWord = stats[l]["EndWord"]
    endWord = random.choices(
        [True, False], [StatEndWord, 100 - StatEndWord])[0]
    return l, endWord


def generatePrefixe(stats):
    """Generate the prefixe of the word

    Args:
        stats (Dictionnary): The stats of the prefixe

    Returns:
        String: The prefixe generated
    """
    letter_probs = {}
    for letter, data in stats.items():
        prob = data
        letter_probs[letter] = prob
    l = choose_letter(letter_probs)
    return l


def generate_word(stats, prefixe, length):
    """Generate a word

    Args:
        stats (Dictionnary): The stats of the dico for the word
        prefixe (Dictionnary): The stats of the prefixe
        length (Int): The length of the word

    Returns:
        String: The word generated
    """
    word = ""

    word += generatePrefixe(prefixe)
    for i in range(length-2):
        letter, endWord = generate_letter(stats, position=i, word=word)
        word += letter
        if endWord and i > 2:
            break
    return word


def harmoniseStat(nameStat):
    """Harmonise the stat file  

    Args:
        nameStat (String): The name of the stat file
    """
    with open('Stats/' + nameStat, 'r') as jsonfile:
        data = json.load(jsonfile)
        for key in data:
            keys_to_delete = [letter for letter in data[key]
                              ["LetterBefore"] if data[key]["LetterBefore"][letter] <= 1.0]
            for letter in keys_to_delete:
                # del data[key]["LetterBefore"][letter]
                data[key]["LetterBefore"][letter] = 0.0

            keys_to_delete_one = [letter for letter in data[key]
                                  ["Combinaison"] if data[key]["Combinaison"][letter] <= 1.0]
            for letter in keys_to_delete_one:
                # del data[key]["Combinaison"][letter]
                data[key]["Combinaison"][letter] = 0.0

            keys_to_delete_two = [letter for letter in data[key]["CombinaisonPlusOne"]
                                  if data[key]["CombinaisonPlusOne"][letter] <= 1.0]
            for letter in keys_to_delete_two:
                # del data[key]["CombinaisonPlusOne"][letter]
                data[key]["CombinaisonPlusOne"][letter] = 0.0

    with open('Stats/' + nameStat, 'w') as outfile:
        json.dump(data, outfile)

    with open("Stats/Prefixe" + nameStat, 'r') as jsonfile:
        data = json.load(jsonfile)
        keys_to_delete = [letter for letter in data if data[letter] <= 1.0]
        for letter in keys_to_delete:
            # del data[letter]
            data[letter] = 0.0


def GenerateDataForLanguage(dico, nameOutput, nameStat):
    """Generate the data for the language

    Args:
        dico (String): The name of the dico
        nameOutput (String): The name of the output file
        nameStat (String): The name of the stat file
    """
    
    parseDico(dico, nameOutput)
    statJson(dico, nameOutput, nameStat)

    harmoniseStat(nameStat)
    PrefixeStat = load_stats("Prefixe" + nameStat)

    stats = load_stats(nameStat)
    temp = []
    for i in range(30):
        temp.append(generate_word(stats, PrefixeStat, random.randint(3, 10)))
    print(temp)


if __name__ == "__main__":
    GenerateDataForLanguage("output.csv", "dico.json", "stat.json")
