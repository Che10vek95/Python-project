# Adding the necessary librories
from gtts import gTTS
from pygame import *
import os
import time
import random

# Additional libraries for colored output and tables
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table

# Initializing colorama
init(autoreset=True)

# Example usage of colored text
print(Fore.RED + "This is red text")
print(Back.YELLOW + "This is text with yellow background")

# Initializing rich console
console = Console()

# Creating a table
table = Table(title="Таблиця оцінок")

# Adding columns
table.add_column("Name", justify="left", style="cyan", no_wrap=True)
table.add_column("Math", justify="center", style="magenta")
table.add_column("Chemistry", justify="center", style="green")

# Adding rows
table.add_row("Karl", "9", "10")
table.add_row("Maria", "12", "12")
table.add_row("Peter", "4", "3")

# Displaying the table
console.print(table)

# Function for colored text output
def colored_text(text: str, color: str = "RED") -> str:
    
    # Dictionary for color mapping
    color_dict = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    
# Default to WHITE if color not found   
    return color_dict.get(color.upper(), Fore.WHITE) + text

# Function for colored background output
def print_colored_background(text: str, background: str = "BLACK") -> str:
    
# Dictionary for background color mapping
    background_dict = {
        "BLACK": Back.BLACK,
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE
    }
    
    """
    Returns text in the specified color.
    
    Parameters:
    text : str - Text to output
    color : str - Text color (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
    
    Returns:
    str - Text with color
    """
    
# Dictionary for color mapping
    color_dict = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
    }
# Default to original if color not found  
    return background_dict.get(background.upper(), Back.BLACK) + text

# Printing examples
print(colored_text("Insanity is doing the exact same thing over and over again, expecting it to change. That is crazy", "RED"))
print(print_colored_background("Maria", "YELLOW"))
print(colored_text("In case I don't see ya, have a good afternoon, good evening, and good night!", "CYAN"))
print(print_colored_background("gobbledygook", "GREEN")) # In case you didn't know, it means language that’s meaningless or hard to understand,





def text_to_speech(phrase: str, lang: str = "en") -> str:
    """
    The function voices the transmitted text and saves it in an mp3 file with a unique name.
    
    Parameters:
    phrase (str) : Text to be voiced
    lang (str)   : Voice language (default is Ukrainian “uk”)
    
    Returns:
    str : name of the saved mp3 file
    """
    # Adding a random number to the file name for uniqueness
    filename = f"voice_{random.randint(1000, 9999)}.mp3"
    
    # Creating text object in gTTs
    tts = gTTS(phrase, lang=lang)

    #saves empty file
    tts.save("filename")

    # Starting the mixer, downloading and playing the file
    mixer.init()
    mixer.music.load("filename")
    mixer.music.play()

    # Every 0.5 seconds cheaking if the music is still playing
    while mixer.music.get_busy():
        time.sleep(0.5)

    # Unloading and deleting the file
    mixer.music.unload()
    mixer.quit()
        
    return filename



def delete_file(filename: str) -> bool:
    """
    This function deletes a file from the disk.
    
    Parameters:
    filename (str) : Name of the file to be deleted.
    
    Returns:
    bool : True if the file was deleted successfully, False if an error occurred.
    """
    try:
        
        # Deleting the file
        os.remove("filename")
        return True
    except Exception as e:
        print(f"Помилка при видаленні файлу: {e}")
        return False
    
    

f=input("Enter something:")
l=int(input("Enter language: 1 - Ukrainian, 2 - English, 3 - Swedish")  )
my_lang="uk"
if l==1:
    my_lang="uk"
elif l==2:
    my_lang="en"
elif l==3:
    my_lang="sv"
else:
    print("Wrong input, setting default language to Ukrainian")
    
    
    
file: str = text_to_speech(f, my_lang)
success: bool = delete_file(file)
print(f"File deletion successful: {success}")


