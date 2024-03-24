#Dictionary Project
#We should have a data source (Download from the link above)
#Learn how to load json data into a python dictionary
#Create a function that returns a definition of a word
#Consider a condition that the entered word is not in a dictionary
#Consider input from user having different cases - upper/ lower case or mixed eg: RAIN/rain/RaIN
#Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
#eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here

import json
import difflib


with open('./data.json') as data:
     dictionary = json.load(data)

def get_word_definition(word):
     word = word.lower()

     if word in dictionary:
          return dictionary[word]
     else:
          suggested_words = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.7)
          if suggested_words:
               return (f"Word not in dictionary! Did you mean: {', '.join(suggested_words)}?")
          else:
               return(f"Word not in dictionary! No close matches either")

def main():
     word = input("Enter word for definition: ")
     definition = get_word_definition(word)
     print(f"{word} : {definition}")

if __name__ == "__main__":
     main()