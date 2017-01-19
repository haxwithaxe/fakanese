# Description
fakanese.py is a library for generating random human readable and pronouncable strings for use as IDs. The keyspace of the strings is too small for use as secure passwords.

It uses the 1 to 4 latin character syllables as the base unit of the "words". The number of characters in a syllable is random. The phonemes that are combined to make the syllables are defined as part of the library as curated sets of characters that will interact well when combined.

Inspired by: http://thedailywtf.com/articles/the-automated-curse-generator.aspx

# Disclaimer
This is heavily biased towards anglophones. There are plans to make the phoneme sets configurable in a separate config file to help alleviate that shortcoming. 

# Example:
```
>>> from fakanese import word
>>> word.random(4)
'foyplanoy'
>>> word.random(2, delimeter='-')
'f-aybl'
>>> word.random(4, delimeter='.')
'iw.oys.aw.oy'
>>> word.upper(5, delimeter='-')
'J-AYB-U-B-U'
>>> word.camel_case(5, delimeter='-') #broken atm
'j-u-t-o-ra' # see, broken
>>> word.camel_case(5, inverse=True) #broken atm
'MAYSWOBAYP' # see, broken
```

# To Do
1. Add word ending rules to prevent unvoiced consonants from being the last character in the word.
1. Configurable phoneme sets.
1. Fix camel case.
1. Random case.
