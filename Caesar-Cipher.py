"""
File        : Caesar-Cipher.py  
Instructor  : Prof. Natasha Kourtonina
Date        : 12/13/2017
Author      : Radhika Hegde
Description : Caesar Cipher
"""

MAX_KEY_SIZE = 26
#Let the user type in if they want encryption or decryption mode for the program. 
#The value returned from input() and lower() is stored in mode
def getMode():
    while True:
         print('Do you wish to encrypt or decrypt a message?\n' 
               'Enter either "encrypt" or "e" or "decrypt" or "d".')
         mode = input().lower()
         if mode in 'encrypt e decrypt d brute b'.split():
             return mode
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d".')
             
#Simply gets the message to encrypt or decrypt from the user and returns it.
def getMessage():
    print('Enter your message:')
    return input()

#lets the user type in the key they will use to encrypt or decrypt the message.
#The while loop ensures that the function keeps looping until the user enters a valid key.
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
     if mode[0] == 'd': #mode sets the function to encryption mode or decryption mode.
         key = -key
     translated = ''

     for symbol in message:
         if symbol.isalpha():
             num = ord(symbol)
             num += key  #shifts the value in num by the value in key.

             if symbol.isupper():
                 if num > ord('Z'):
                     num -= 26
                 elif num < ord('A'):
                     num += 26
             elif symbol.islower():
                 if num > ord('z'):
                     num -= 26
                 elif num < ord('a'):
                     num += 26

             translated += chr(num)
         else:
             translated += symbol
     return translated

#the program calls each of the three functions 
#defined previously to get the mode, message, and key from the user.
mode = getMode()
message = getMessage()
if mode[0] != 'b':
     key = getKey()

print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))