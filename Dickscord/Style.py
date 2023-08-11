from .imports import *

"""
Copyright 2023 KADIUM
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class Style:
    @staticmethod
    def print(content: str):
        print(
            f'{Fore.LIGHTBLACK_EX}{datetime.fromtimestamp(time()).strftime(f"[{Fore.LIGHTBLUE_EX}%H{Fore.LIGHTBLACK_EX}:{Fore.LIGHTBLUE_EX}%M{Fore.LIGHTBLACK_EX}:{Fore.LIGHTBLUE_EX}%S{Fore.LIGHTBLACK_EX}]")}{Fore.RESET} ' +
            content
            .replace("->", f"{Fore.LIGHTBLACK_EX}->{Fore.LIGHTBLUE_EX}")
            .replace("(+)", f"{Fore.LIGHTBLACK_EX}({Fore.GREEN}+{Fore.LIGHTBLACK_EX}){Fore.LIGHTGREEN_EX}")
            .replace("($)", f"{Fore.LIGHTBLACK_EX}({Fore.GREEN}${Fore.LIGHTBLACK_EX}){Fore.GREEN}")
            .replace("(-)", f"{Fore.LIGHTBLACK_EX}({Fore.RED}-{Fore.LIGHTBLACK_EX}){Fore.LIGHTRED_EX}")
            .replace("(!)", f"{Fore.LIGHTBLACK_EX}({Fore.RED}!{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("(~)", f"{Fore.LIGHTBLACK_EX}({Fore.YELLOW}~{Fore.LIGHTBLACK_EX}){Fore.YELLOW}")
            .replace("(/)", f"{Fore.LIGHTBLACK_EX}({Fore.YELLOW}/{Fore.LIGHTBLACK_EX}){Fore.YELLOW}")
            .replace("(#)", f"{Fore.LIGHTBLACK_EX}({Fore.BLUE}#{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("(*)", f"{Fore.LIGHTBLACK_EX}({Fore.CYAN}*{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("[+]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLACK_EX}]{Fore.LIGHTGREEN_EX}")
            .replace("[-]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTBLACK_EX}]{Fore.LIGHTRED_EX}")
            .replace("[>]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}>{Fore.LIGHTBLACK_EX}]{Fore.LIGHTBLUE_EX}")
            .replace("(>)", f"{Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}>{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
        , end=f"{Fore.RESET}\n")

    @staticmethod
    def reset():
        Fore.RESET
    
    @staticmethod
    def input(prompt: str):
        colored_prompt = (
            prompt
            .replace("->", f"{Fore.LIGHTBLACK_EX}->{Fore.LIGHTBLUE_EX}")
            .replace("(+)", f"{Fore.LIGHTBLACK_EX}({Fore.GREEN}+{Fore.LIGHTBLACK_EX}){Fore.LIGHTGREEN_EX}")
            .replace("($)", f"{Fore.LIGHTBLACK_EX}({Fore.GREEN}${Fore.LIGHTBLACK_EX}){Fore.GREEN}")
            .replace("(-)", f"{Fore.LIGHTBLACK_EX}({Fore.RED}-{Fore.LIGHTBLACK_EX}){Fore.LIGHTRED_EX}")
            .replace("(!)", f"{Fore.LIGHTBLACK_EX}({Fore.RED}!{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("(~)", f"{Fore.LIGHTBLACK_EX}({Fore.YELLOW}~{Fore.LIGHTBLACK_EX}){Fore.YELLOW}")
            .replace("(/)", f"{Fore.LIGHTBLACK_EX}({Fore.YELLOW}/{Fore.LIGHTBLACK_EX}){Fore.YELLOW}")
            .replace("(#)", f"{Fore.LIGHTBLACK_EX}({Fore.BLUE}#{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("(*)", f"{Fore.LIGHTBLACK_EX}({Fore.CYAN}*{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
            .replace("[+]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLACK_EX}]{Fore.LIGHTGREEN_EX}")
            .replace("[-]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTBLACK_EX}]{Fore.LIGHTRED_EX}")
            .replace("[>]", f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}>{Fore.LIGHTBLACK_EX}]{Fore.LIGHTBLUE_EX}")
            .replace("(>)", f"{Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}>{Fore.LIGHTBLACK_EX}){Fore.LIGHTBLUE_EX}")
        )
        
        return input(colored_prompt)
    
    @staticmethod
    def midwrite(text):
        terminal_width, _ = shutil.get_terminal_size()
        text_width = len(text)
        padding = (terminal_width - text_width) // 2
        print(" " * padding + text)

    @staticmethod
    def slowtype(text, delay):
        for char in text:
            print(char, end='', flush=True)
            sleep(delay)
        print() 
    