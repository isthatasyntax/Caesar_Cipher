# Coursework Assessment 1
# Name:Zaid Darsot
# Student No:2241296

# A Caesar Cipher Program
import os.path


def welcome():
    print("Welcome to the Caesar Cipher This program encrypts and decrypts text with the Caesar Cipher.\n")
    return


def enter_message():
    # This function Accepts user input
    mode = input('Would you like to encrypt (e) or decrypt (d): ')
    message = input('Enter a message: ').upper()
    shift = int(input("Enter the shift number between 1-25: "))
    if mode not in ('e', 'd'):
        print("Invalid mode entered")
        enter_message()
    elif (mode == 'd'):
        decrypt(message, shift)
    else:
        encrypt(message, shift)
    return (mode, message, shift)


def encrypt(message, shift):
    # This is the alphabet that will be used by to encrypt
    a = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    message = message.lower()  # lowercase text will be excrypted
    for b in message:
        if b in a:
            # will go through each letter of the alphabet one letter at a time, depending on the character you want to encrypt
            c = a.index(b)
            # moves places to whatever the shift number is and will go back to the start of alphabet if it reaches last letter
            d = (c + shift) % 26
            encrypted = encrypted + a[d]
        else:
            encrypted = encrypted + b
    print(encrypted.upper())  # prints the encrypted message in uppercase
    return (encrypted)
    return ''


# line 56-68... allows the user to decrypt a message
def decrypt(message, shift):
    a = 'abcdefghijklmnopqrstuvwxyz'  # This is the alphabet that the decrypt will use
    decrypted = ''
    message = message.lower()  # lowercase text will be excrypted
    for b in message:
        if b in a:
            c = a.index(b)
            # goes back places to whatever the shift number is and will go back to the start of the alphabet until it reaches the last letter
            d = (c - shift) % 26
            decrypted = decrypted + a[d]
        else:
            decrypted = decrypted + b
    print(decrypted.upper())  # prints the decryped message in uppercase
    return (decrypted)
    return ''


# This function encrypts or decrypts your file data
def process_file(filename, mode, shift):
    list_messages = []
    filename = input("Enter name of your file: ")
    mode = input('Would you like to encrypt (e) or decrypt (d): ')
    shift = int(input("Enter the shift number between 1-25: "))
    if is_file(filename) == False:
        print('Invalid filename,Enter valid file name')
        process_file(filename, mode, shift)
    else:
        input_file = open(filename, 'r')
        # open(filename,'r')
        for line in input_file:
            print(line)
            if mode == 'e':
                encrypt(line, shift)
                list_messages.append(line)
                write_messages(list_messages)
                print(line)

            else:
                decrypt(line, shift)
                print(line)

                list_messages.append(line)
                write_messages(list_messages)
        print("Output written in results.txt")
        input_file.close()

    return (list_messages)


def write_messages(list_messages):  # This function stores your file data to results.txt
    file = open('results.txt', 'w')

    for line in list_messages:
        file.write(line)

    file.close()

    return (line)


def is_file(filename):  # This Function checks the existence of your file
    return os.path.isfile(filename)


def message_or_file():  # This Function asks the user wether to encrypt or decrypt the file or console
    mode = ''
    filename = None
    message = None
    shift = 0
    info = input('Would you like to read from a file (f) or the console (c): ')
    if info not in ('c', 'f'):
        print("Invalid mode entered")
        message_or_file()
    elif (info == 'c'):
        enter_message()
    else:
        process_file(filename, mode, shift)
    return (mode, message, filename, shift)


"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    â€¢ Prompt users to select a mode: encrypt (e) or decrypt (d).
    â€¢ Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    â€¢ Prompt the user for the message they would like to encrypt/decrypt.
    â€¢ encrypt/decrypt the message as appropriate and print the output.
    â€¢ Prompt the user whether they would like to encrypt/decrypt another message.
        â€¢ Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            â€¢ End the program if the user selects no.
            â€¢ Proceed directly to step 2 if the user says yes.
    â€¢ Your program should be as close as possible to the example shown in the assessment specification.
"""


def main():  # This Function is where all functions are compiled
    welcome()
    message_or_file()
    confirm = input("Do you want to go again ?(y/n):")
    if confirm not in ('y', 'n'):
        print("Invalid")
        confirm()
    elif (confirm == 'y'):
        message_or_file()
    else:
        print("Goodbye.")

    return


# Program execution begins here
if __name__ == '__main__':
    main()
