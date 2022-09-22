
# "Mapper" alfabetet til tilsvarende morse kode for at vi nemt kan slå op hvilke bogstaver der er hvad.
morseCode = {'a': '.-',
           'b': '-...',
           'c': '-.-.',
           'd': '-..',
           'e': '.',
           'f': '..-.',
           'g': '--.',
           'h': '....',
           'i': '..',
           'j': '.---',
           'k': '-.-',
           'l': '.-..',
           'm': '--',
           'n': '-.',
           'o': '---',
           'p': '.--.',
           'q': '--.-',
           'r': '.-.',
           's': '...',
           't': '-',
           'u': '..-',
           'v': '...-',
           'w': '.--',
           'x': '-..-',
           'y': '-.--',
           'z': '--..',
           'æ': '.-.-',
           'ø': '---.',
           'å': '.--.-',
           '0': '-----',
           '1': '.----',
           '2': '..---',
           '3': '...--',
           '4': '....-',
           '5': '.....',
           '6': '-....',
           '7': '--...',
           '8': '---..',
           '9': '----.',
           '.': '.-.-.-',
           ',': '--..--',
           '!': '-.-.--',
           ' ': ''
           }

morseCodeReverse = {}

for key in morseCode.keys():
    morseCodeReverse[morseCode[key]] = key # Laver en omvendt dictionry af morseCode

def translate(letter, code):
    letter = letter.lower()

    if letter in code.keys():
        return code[letter] # Returnerer hver bogstavt bogstavs tilsvarende karakter.
    return '?'

def encodeMessage(message, code):
    output = ''
    for letter in message:
        output += '{}/'.format(translate(letter, code)) # Formatterer hver oversat karakter i "message" til morse
    output += '/'
    return output

def decodeMessage(message, code):
    decoded = ''
    for sign in message.split('/'):
        decoded += translate(sign, code) # Formatterer hver morse tegn til dets alfabetiske karakter
    return decoded.strip()

if __name__ == '__main__':
    original = 'Programmering er sjovt!'
    tilMorse = encodeMessage(original, morseCode)
    print(tilMorse)
    fraMorse = decodeMessage(tilMorse, morseCodeReverse)
    print(fraMorse)
    if original.lower() == fraMorse.lower(): # Checker om den har encoded og decoded beskeden ordenligt
        print('Programmet virker')
