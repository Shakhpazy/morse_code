import winsound
import time
#morse code dictionary:
MORSE_CODE_DICT = {'A':'.-', 
                   'B':'-...', 
                   'C':'-.-.', 
                   'D':'-..', 
                   'E':'.', 
                   'F':'..-.', 
                   'G':'--.', 
                   'H':'....', 
                   'I':'..', 
                   'J':'.---', 
                   'K':'-.-', 
                   'L':'.-..', 
                   'M':'--', 
                   'N':'-.', 
                   'O':'---', 
                   'P':'.--.', 
                   'Q':'--.-', 
                   'R':'.-.', 
                   'S':'...', 
                   'T':'-', 
                   'U':'..-', 
                   'V':'...-', 
                   'W':'.--', 
                   'X':'-..-', 
                   'Y':'-.--', 
                   'Z':'--..', 
                   '1':'.----', 
                   '2':'..---', 
                   '3':'...--', 
                   '4':'....-', 
                   '5':'.....', 
                   '6':'-....', 
                   '7':'--...', 
                   '8':'---..', 
                   '9':'----.', 
                   '0':'-----', 
                   ',':'--..--', 
                   '.':'.-.-.-', 
                   '?':'..--..', 
                   '/':'-..-.', 
                   '-':'-....-', 
                   '(':'-.--.', 
                   ')':'-.--.-',
                   ' ': '/'}
INV_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


#User inputs 
user_input = input("Type a word or sentence to translate into morse code: ")







#gets a word or phrase and translates it into morse code
#translates "how, are you" --> .... --- .-- , / .- .-. . / -.-- --- ..-
def to_morse_code(word):
    word = word.upper()
    morse_word = ""
    #loops through the word and translates each chacter while adding a space at the end.
    for i in word:
        letter_translation = MORSE_CODE_DICT[i]
        morse_word += letter_translation + " "
    #to remove the last " " charcter at the end.
    morse_word = morse_word[:-1]
    return morse_word
    
def to_normal(morse_code):
    morse_code = morse_code.split()
    translation = ""
    for i in morse_code:
        morse_code_char_translation = INV_MORSE_CODE_DICT[i]
        translation += morse_code_char_translation
    return translation


#audio
def beep(duration):
    winsound.Beep(frequency=600, duration=duration)
    time.sleep(0.001)

def short_pause():
    """ Since you are sleeping 1 milisecond 
    after every charceter, you would need to 
    sleep 2 more miliseconds to make it sleep 
    for a total of 3 miliseconds for letter gaps"""
    time.sleep(0.002)

def long_pause():
    """ Since you are sleeping 3 miliseconds before 
        '/' and 2 miliseconds after, you need this to be
        2 miliseconds as well for a total of 7miliseconds"""
    time.sleep(0.002)

#takes in a morse code string ex: ".... --- .-- / .- .-. . / -.-- --- ..-"
#audio rules --> short-mark = 1unit, long-mark = 3unit, inter-element-pause = 1unit, short-gap = 3units, long-gap = 7units
def morse_code_audio_create(morse_code_string):
    code_word = morse_code_string
    num = 0
    for char in code_word:
        if char == '.':
            beep(duration=100)
        elif char == '-':
            beep(duration=300)
        elif char == ' ':
            short_pause()
        elif char == "/":
            long_pause()
        else:
            print(f" error ")
        print(f"{num} char:  {char}")
        num += 1


#Testing to see if code works and translates properly.
morse_code = to_morse_code(word = user_input)
normal = to_normal(morse_code = morse_code)
print(morse_code)
print(normal)
morse_code_audio_create(morse_code_string=morse_code)
