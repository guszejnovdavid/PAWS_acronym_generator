#Overview
=====

acronym_gen is a python algorithm to generate English acronyms from a set of keywords. 
It is inspired by ACRONYM (Acronym CReatiON for You and Me, https://github.com/bacook17/acronym) but unlike ACRONYM this algporithm creates proper acronyms using the first N letters from keywords in all possible combinations.

#Install
=====

Can be installed with pip:
```
$ pip install acronym_gen
```
or by downloading the repository and then running
```
$ make install
```

#Usage
=====

acronym_gen is designed to be called in the format
```
$python acronym_gen.py <keywords> ... [options]
```

Options:                                                                       
   -h --help                  Show this screen.
   --min_acronymlength=<N>    Minimum length of the acronym [default: 3]
   --max_letters_to_use=<N>   Sets the maximum number of letters that can be used from the beginning of keywords [default: 5]
   --use_synonyms             Whether to add the synonyms of the given keywords to the list (it can drastically increase the number of results, off by default)
   --strict=<f>               Sets how strictly should words be related to English [default: None]

#Example
```
$python acronym_gen.py giant nebula star in --max_letters_to_use=2
        GIN : Giant In Nebula
        GIN : Giant IN
        GIN : GIant Nebula
        GINN : Giant IN Nebula
        GINNE : Giant IN NEbula
        GINS : Giant In Nebula Star
        GINS : Giant IN Star
        GINS : GIant Nebula Star
        GIS : Giant In Star
        GIS : GIant Star
        GIST : Giant In STar
        GIST : GIant STar
        ING : In Nebula Giant
        ING : IN Giant
        INN : IN Nebula
        INNS : IN Nebula Star
        ISN : In Star Nebula
        IST : In STar
        NEST : NEbula STar
        NING : Nebula IN Giant
        SIGN : Star In Giant Nebula
        SIGNE : Star In Giant NEbula
        SIN : Star In Nebula
        SIN : Star IN
        SING : Star In Nebula Giant
        SING : Star IN Giant
        SINN : Star IN Nebula
        SINNE : Star IN NEbula
        STIG : STar In Giant
        STING : STar In Nebula Giant
        STING : STar IN Giant
```
At this point the use must pick out the ones that make sense, like SIGN : Stars In Giant Nebulas or STING : STars IN Giants
