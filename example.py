# Here is an Example of an Fully working Discord Tool using Dickscord 🍆🫧

from Dickscord import *

def set_command_prompt_size(columns, lines):
    command = f"mode con: cols={columns} lines={lines}"
    os.system(command)

set_command_prompt_size(132, 25)
x = (f"""{Fore.LIGHTBLUE_EX}
                                                        ____  ________  _________
                                                       / __ \/ ____/  |/  /_  __/
                                                      / / / / /_  / /|_/ / / /   
                                                     / /_/ / __/ / /  / / / /    
                                                    /_____/_/   /_/  /_/ /_/     
                                                                                 """)
print(x)
menu = """
  [01] - Channel Spammer      [02] - Nickname Changer     [03] - Fake Typing       [04] - Token Activity      [05] - Advanced Spam"""
print(menu)
choice = Style.input(f"  (#): Choice?: ")
if choice == "1":
    Dickcord.spamchannel('tokens.txt')
if choice == "2":
    Dickcord.nicknamechanger('tokens.txt')
if choice == "3":
    Dickcord.faketyping('tokens.txt')
if choice == "4":
    Dickcord.settokenactivity('tokens.txt')
if choice == "5":
    Dickcord.advancedspam('tokens.txt')