#!/usr/bin/env python
"""                                                                            
Algorithm that lists possible English acronyms from a listed keywords. 
It is inspired by ACRONYM (Acronym CReatiON for You and Me, https://github.com/bacook17/acronym) but unlike ACRONYM this algporithm creates proper acronyms using the first letters keywords in all possible combinations.

Usage: acronym_gen.py <keywords> ... [options]

Options:                                                                       
   -h --help                  Show this screen.
   --min_acronymlength=<N>    Minimum length of the acronym [default: 3]
   --max_letters_to_use=<N>   Sets the maximum number of letters that can be used from the beginning of keywords [default: 5]
   --use_synonyms             Whether to add the synonyms of the given keywords to the list (it can drastically increase the number of results, off by default)
   --strict=<f>               Sets how strictly should words be related to English [default: None]
"""
from __future__ import print_function
import numpy as np
import nltk
try:
    nltk.corpus.words.ensure_loaded()
    nltk.corpus.brown.ensure_loaded()
    nltk.corpus.gutenberg.ensure_loaded()
    nltk.corpus.wordnet.ensure_loaded()
except LookupError:
    print('Initial downloading of word corpus')
    for d in ['words', 'brown', 'gutenberg', 'wordnet']:
        nltk.download(d)
from docopt import docopt
        

def get_synonyms(word):
    #Get the synonyms for a word from Wordnet
    res = []
    for syn in nltk.corpus.wordnet.synsets(word):
        for l in syn.lemmas():
            res.append(l.name())
    return res
               
#global
combinations=[]

def next_piece_in_word(wordlist, word, orig_word=None,prev_choices=[],max_letters_to_use=3):
    #Checks which strings from wordlist matches the beginning of word, using 1-max_letters_to_use size chunks.
    #Recursive code, if it is possible toreconstruct the full word then the appropriate choices are saved to the global variable combinations
    global combinations
    if (orig_word is None):
        orig_word=word
    for w in wordlist:
        for i in range(np.min([len(w),max_letters_to_use])):
            s=w[0:(i+1)]
            if (s==word[0:(i+1)]): # we have a match
                new_choices=prev_choices[:]
                new_choices.append([w,i]) #each choice is represented by the word we used and the index of the last letter used
                if (len(s)==len(word)): # we have finished the word
                    combinations.append(new_choices) #store solution
                else:
                    new_wordlist=[wo for wo in wordlist if wo!=w] #remove the word we have just used, we can't repeat them
                    if len(new_wordlist):
                        new_word=word[(i+1):] #move onto the rest of the word we want to construct
                        #Call recursion
                        next_piece_in_word(new_wordlist, new_word, orig_word=orig_word,\
                                              prev_choices=new_choices,max_letters_to_use=max_letters_to_use)

def main():
    #Get options
    options = docopt(__doc__)    
    keywordlist = [w  for w in options["<keywords>"]] 
    min_acronymlength=int(options["--min_acronymlength"])
    max_letters_to_use=int(options["--max_letters_to_use"])
    strict=options["--strict"]
    if (strict!='None'): strict=int(strict)
    use_synonyms =  options["--use_synonyms"]
    #init global    
    global combinations
    combinations = []
    #Add synonyms if needed, note that this will add a LOT of new results many using synonyms of the same word several times
    if use_synonyms:
        temp_list=keywordlist[:]
        for w in keywordlist:
            syns=get_synonyms(w)
            for s in syns:
                if (s.isalpha()):
                    temp_list.append(s.lower())
        temp_list=np.unique(temp_list)
        keywordlist=temp_list
    #Keywords to lwercase, print list
    keywordlist = [w.lower() for w in keywordlist]
    print("Using keywords: ",keywordlist)
    #Collect all the letters of the laphabet used in keywords, usde to filter the words to test
    key_chars=[]
    for w in keywordlist:
        for c in w[0:(max_letters_to_use)]:
            key_chars.append(c)
    key_chars=np.unique(key_chars)
    #Choose word corpus based on how strict we are with the words we can use
    if strict == 0:
        corpus = nltk.corpus.words
    elif strict == 1:
        corpus = nltk.corpus.brown
    else:
        corpus = nltk.corpus.gutenberg
    #Choose words that have letter that are present in keywords and have at least the minimum length
    word_list = np.unique([w.lower() for w in corpus.words() if w.isalpha() and (len(w)>=min_acronymlength) and set(list(w)).issubset(set(key_chars))])    
    print("Numer of words to process %d"%(len(word_list)))
    #See which ones of these can be recovered
    for w in word_list:
        next_piece_in_word(keywordlist, w, max_letters_to_use=max_letters_to_use)
    #List possible acronyms
    if len(combinations):
        print("%d possible acronyms: "%(len(combinations)))
        #List possibilities
        for seq in combinations:
            #Recreate word and choices
            acronym=''
            exp_acronym=''
            for piece in seq:
                capital_part=(piece[0][0:(piece[1]+1)]).upper()
                noncapital_part=(piece[0][(piece[1]+1):]).lower()
                acronym+=capital_part
                exp_acronym+=capital_part+noncapital_part+' '
            print("\t"+acronym+' : '+exp_acronym)
    else:
        print("No appropriate acronyms found.")
        

if __name__ == "__main__": main()
