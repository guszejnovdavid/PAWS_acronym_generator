# Overview

The PAWS (Proper Acronyms With Synonyms) is a python algorithm to generate English acronyms from a set of keywords. It is inspired by ACRONYM (Acronym CReatiON for You and Me, https://github.com/bacook17/acronym) but unlike ACRONYM this algorithm creates proper acronyms using the first N letters from keywords in all possible combinations. Furthermore, it can replace any keyword with its synonyms (using nltk) to provide more alternatives.

The code is highly customizable, it is possible to set which keywords can be replaced by synonyms as well as establishing dependencies between words so that similar or contradictory keywords are not used in the same acronym. Also, it is possible to force the use of important keywords in the resulting acronyms.

# Install

Can be installed with pip:
```
$ pip3 install paws_acronym
```
or by downloading the repository and then running
```
$ make install
```

# Usage

PAWS is designed to be called in the format
```
$paws_acronym <keywords> ... [options]
```
Keywords are to be entered separated by spaces (e.g., `large code`). To allow the code to substitute a word with its synonyms, put a `*` in front of the word (e.g., `*good`). It is also possible to group words together by listing them one after another, separeted by commas and no whitespaces, from each group only one word is used in an acronym (e.g., `bike,car`)

Options:                                                                       
```
   -h --help                         Shows options
   --forced_words=<words>            List of words (separated by commas) that MUST be part of the acronym (these words should be already included with keywords).
   --min_acronymlength=<N>           Minimum length of the acronym [default: 3]
   --max_letters_to_use=<N>          Sets the maximum number of letters that can be used from the beginning of keywords [default: 5]
   --use_synonyms_for_all            If turned on, all keywords can have synonyms. Note that this can drastically increase the number of results
   --strict=<f>                      Sets how strictly should words be related to English by changing the `nltk` word corpus (0: `words`, 1: `brown`, other: `gutenberg`) [default: None]
```
# Examples

Let's try to name an algorithm that generates acronyms using synonyms.
```
$ paws_acronym acronym generator synonyms
Using keywords:  acronym generator synonyms
Number of words to process 460
Words processed, 7 acronyms found, filtering for extra criteria...
        AGE : Acronym GEnerator
        AGEN : Acronym GENerator
        AGES : Acronym GEnerator Synonyms
        GAS : Generator Acronym Synonyms
        GENERA : GENERator Acronym
        SAC : Synonyms ACronym
        SAGE : Synonyms Acronym GEnerator
```
These are quite limited in scope, we could get a lot more options if we added some optional adjectives and prepositions. Also, we could replace `generator` with `algorithm` or `code`. To avoid repetition of similar words we can define them to be dependent on each other, so we get maximum one adjective, one preposition and one of `code`/`generator`/`algorithm`. Also, it is a good idea to enable the use of synonyms. Note that allowing synonyms for words like `good` will lead to a lot of possible acronyms so let's filter our results to the ones that include the key words of `acronym` and `synonyms`. 
```
$ paws_acronym acronym generator,code,algorithm synonyms *with,*of,*from *good,*proper --forced_words=acronym,synonyms
Using 43 keywords:  acronym adept algorithm beneficial code commodity dear dependable effective estimable expert from full generator good goodness honest honorable just near of practiced proficient proper respectable right ripe safe salutary secure serious skilful skillful sound soundly synonyms thoroughly undecomposed unspoiled unspoilt upright well with
Keyword dependencies:  [0. 4. 1. 4. 1. 4. 4. 4. 4. 4. 4. 3. 4. 1. 4. 4. 4. 4. 4. 4. 3. 4. 4. 4.
 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 4. 2. 4. 4. 4. 4. 4. 4. 3.]
Number of words to process 29492
Words processed, 1718 acronyms found, filtering for extra criteria...
        ACCESS : ACronym Code EStimable Synonyms
        ...
```
This will put out over a hundred possible acronyms. At this point it is up to the user to peruse them and identify the ones that could work with little or no modifications, like:
```
ADAGES : ADept Acronym GEnerator using Synonyms
AGENTS : Acronym GENeration Through Synonyms
EASY : Expert Acronyms from SYnonyms
GAS : Generator of Acronyms from Synonyms
GREASY : Generator of REspectable Acronyms from SYnonyms
HAGS : Honest Acronym Generation from Synonyms
PAGES : Proper Acronym GEneration from Synonyms
PAWS : Proper Acronym With Synonyms
RAGES : Respectable Acronym GEneration with Synonyms
SEAS : SErious Acronyms from Synonyms
```