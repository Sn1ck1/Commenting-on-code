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
# Defining characters


morseCodeReverse = {}

for key in morseCode.keys():
    morseCodeReverse[morseCode[key]] = key

def translate(letter, code):
    letter = letter.lower()

    if letter in code.keys():
        return code[letter]
    return '?'

def encodeMessage(message, code):
    output = ''
    for letter in message:
        output += '{}/'.format(translate(letter, code))
    output += '/'
    return output

def decodeMessage(message, code):
    decoded = ''
    for sign in message.split('/'):
        decoded += translate(sign, code)
    return decoded.strip()

if __name__ == '__main__':
    original = input('')
    tilMorse = encodeMessage(original, morseCode)
    print(tilMorse)
    fraMorse = decodeMessage(tilMorse, morseCodeReverse)
    print(fraMorse)
    if original.lower() == fraMorse.lower():
        print('Programmet virker')
