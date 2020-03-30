import os
import re
import argparse

'''
dot : 1 unit
dash: 3 units
space between dots and dashes in the same letter: 1 unit
space between dots and dashes in the same word: 3 units
space between words: 7 units
Morse code was designed so that the length of each symbol
is approximately inverse to the frequency of occurrence
in text of the English language character that it represents
'''

letter_dict = {
  'a': '.-',    'b': '-...',    'c': '-.-.',  'd': '-..',
  'e': '.',     'f': '..-.',    'g': '--.',   'h': '....',
  'i': '..',    'j': '.---',    'k': '-.-',   'l': '.-..',
  'm': '--',    'n': '-.',      'o': '---',   'p': '.--.',
  'q': '--.-',  'r': '.-.',     's': '...',   't': '-',
  'u': '..-',   'v': '...-',    'w': '.--',   'x': '-..-',
  'y': '-.--',  'z': '--..',
  '0': '-----', '1': '..---',   '2': '...--', '3': '...--',
  '4': '....-', '5': '.....',   '6': '-....', '7': '--...',
  '8': '---..', '9': '----.',
}

def convert_morse(s):
  lower = s.lower()
  
