#!/bin/python3

from json import dump, load
from string import ascii_uppercase
from collections import Counter

letters = ascii_uppercase

STD_FREQ = {
    'E': 0.111607,        'A': 0.084966,
    'R': 0.075809,        'I': 0.075448,
    'O': 0.071635,        'T': 0.069509,
    'N': 0.065544,        'S': 0.057351,
    'L': 0.054893,        'C': 0.045388,
    'U': 0.036308,        'D': 0.033844,
    'P': 0.031671,        'M': 0.030129,
    'H': 0.030034,        'G': 0.024705,
    'B': 0.020720,        'F': 0.018121,
    'Y': 0.017779,        'W': 0.012899,
    'K': 0.011016,        'V': 0.010074,
    'X': 0.002902,        'Z': 0.002722,
    'J': 0.001965,        'Q': 0.001962
}

def getCipher(filesList:list[str]) -> None:
    cipherText = dict()

    for f in filesList:
        with open("data/found1", "r") as file:
            file1 = file.read()

        with open("data/found2", "r") as file:
            file2 = file.read()

        cipherText["found1"] = file1.replace(" ", "")
        cipherText["found2"] = file2.replace(" ", "")

    with open("data/ciphers.json", "w") as file:
        dump(cipherText, file, indent=2)

def getSubtext(cipher:str, keylen:int) -> dict:
    '''returns a splitted subtexts for the length of the key -> dictionary'''

    st = {str(i): [] for i in range(keylen)}        # st: subtext

    cipherlen = len(cipher)
    cycles = cipherlen // keylen
    remainder = cipherlen % keylen
    # cycles += remainder # to add the remainder chars to the cycle

    for subtext in range(keylen):
        index = subtext

        for _ in range(cycles):
            st[str(subtext)].append(cipher[index])
            index += keylen

        if subtext < remainder:
            st[str(subtext)].append(cipher[index])
        
        st[str(subtext)] = "".join(st[str(subtext)]) 
    
    return st
    
def showFreqs(subtextNum:int, file="data/freq.json"):
    '''displays the frequency from the highest to the lowest'''

    with open(file, "r") as file:
        frequencies = load(file)
    
    notUsedLetters = []
    
    for char in letters:    
        if char not in frequencies[str(subtextNum)]: # meaning the letter was not used
            notUsedLetters.append(char)
    
    i = 0
    letterOrder = list(STD_FREQ.keys())
    output = "\n\n     Subtext's Letter Frequency          |     Standard English Letter Frequency      "
    line = list("-" * len(output))
    middle_index = (len(output) // 2) - 3 
    line[middle_index] = "+"
    line = "".join(line)
    print(f"{output}\n{line}")
    for letter, freq in frequencies[str(subtextNum)].items():
        print(f"               {letter}: {freq:<8}               |               {letterOrder[i]}: {round(STD_FREQ[letterOrder[i]], 3)}")
        i += 1
    
    # notUsedLetters = "".join(notUsedLetters)
    # print(f"\nThe following letters weren't use in this subtext: {notUsedLetters}")
    strzero = "0"
    for letter in notUsedLetters:
        print(f"               {letter}: {strzero:<8}               |               {letterOrder[i]}: {round(STD_FREQ[letterOrder[i]], 3)}")
        i += 1
    
    print("\n\n")






















if __name__ == "__main__":
    with open("data/ciphers.json", "r") as file:
        ciphers = load(file)
    
    # clen = len(ciphers["found1"])
    # cycles = clen // 6
    # rem = clen % 6
    # last_extended_cycle = rem -1
    # print(cycles)
    # print(rem)
    # print(last_extended_cycle)

    # for i in range(6):
    #     if i <= last_extended_cycle:
    #         print("this cycle is extended")
    #     else:
    #         print("this cycle is normal")

    # subTs = getSubtext(ciphers["found1"], 6)
    # subFound2 = getSubtext(ciphers["found2"], 6)

    # for i in range(6):
    #     subTs[str(i)] = subTs[str(i)] + subFound2[str(i)]

    # for subtext, value in subTs.items():
    #     print(subtext, value)
    #     break
    
    # with open("data/subTexts.json", "w") as file:
        # dump(subTs, file, indent=2)


    # with open("data/subTexts.json","r") as file:
    #     subTexts = load(file)
    
    # frequencies = dict()
    
    # for index, text in subTexts.items():
    #     count = Counter(text)
    #     for letter, c in count.items():
    #         count[letter] = round( c/len(text), 3 ) # to get a float frequency
    #     sortedFreq = count.most_common()
        
    #     freq = dict()
    #     for key, value in sortedFreq:
    #         freq[key] = value



    #     frequencies[index] = freq 
    
    # with open("data/freq.json", "w") as file:
    #     dump(frequencies, file, indent=4)

    

    userInput = int(input("Enter the number of the subtext you want to check its letter frequencies (0-5): "))
    showFreqs(userInput)

