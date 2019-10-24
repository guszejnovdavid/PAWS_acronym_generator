# Overview

acronym_gen is a python algorithm to generate English acronyms from a set of keywords. 
It is inspired by ACRONYM (Acronym CReatiON for You and Me, https://github.com/bacook17/acronym) but unlike ACRONYM this algporithm creates proper acronyms using the first N letters from keywords in all possible combinations.

# Install

Can be installed with pip:
```
$ pip install acronym_gen
```
or by downloading the repository and then running
```
$ make install
```

# Usage

acronym_gen is designed to be called in the format
```
$python acronym_gen.py <keywords> ... [options]
```

Options:                                                                       
   -h --help                         Show this screen.
   --forced_words=<words>            List of words (separated by commas) that MUST be part of the acronym (these words should be already included with keywords).
   --min_acronymlength=<N>           Minimum length of the acronym [default: 3]
   --max_letters_to_use=<N>          Sets the maximum number of letters that can be used from the beginning of keywords [default: 5]
   --use_synonyms=<0,1,1...>         Whether to add the synonyms of the given keywords to the list (any >0 number means True, all zeros by default)
   --use_synonyms_for_all           If turned on without all keywords can have synonyms. Note that this can drastically increase the number of results
   --strict=<f>                      Sets how strictly should words be related to English [default: None]
   --independence=<i1,i2...>         Defines dependences between keywords, if several words have the same id, only one can be used in an acronym (i.e. to handle synonyms). If undefined all keywords are assumed to be independent.

# Example

Let's try to name a simulation of stars in giant nebulas.
```
$ python acronym_gen.py giant nebula star in --strict=1
Using keywords:  ['giant', 'nebula', 'star', 'in']
Numer of words to process 2155
30 possible acronyms:
        GIANT : GIANT
        GIANTS : GIANT Star
        GIN : Giant In Nebula
        GIN : Giant IN
        GIN : GIant Nebula
        GINS : Giant In Nebula Star
        GINS : Giant IN Star
        GINS : GIant Nebula Star
        GIST : Giant In STar
        GIST : GIant STar
        INN : IN Nebula
        INNS : IN Nebula Star
        IST : In STar
        NEST : NEbula STar
        NESTING : NEbula STar IN Giant
        NIGS : Nebula In Giant Star
        SIGN : Star In Giant Nebula
        SIN : Star In Nebula
        SIN : Star IN
        SINE : Star In NEbula
        SING : Star In Nebula Giant
        SING : Star IN Giant
        STAG : STAr Giant
        STAIN : STAr In Nebula
        STAIN : STAr IN
        STAR : STAR
        STARING : STAR In Nebula Giant
        STARING : STAR IN Giant
        STING : STar In Nebula Giant
        STING : STar IN Giant

```
At this point the user must pick out the ones that make sense, like SIGN : Stars In Giant Nebulas or STAIN : STArs In Nebula
