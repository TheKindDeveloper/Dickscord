from .imports import *
from .Style import Style

"""
Copyright 2023 KADIUM
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class pc:
    @staticmethod
    def tempcreate(content, filename):
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(content)
                temp_filename = temp_file.name
                Style.print(f"(+): Temp file Created > {content}")
        except Exception as e:
            Style.print(f"(!): Failed to create Temp file {e}")

    @staticmethod
    def createtext(filepath, content, file):
        try:
            full_path = os.path.join(filepath, file)
            with open(full_path, 'w') as text_file:
                text_file.write(content)
            Style.print(f"(+): Created File at: {full_path} ")
        except Exception as e:
            print(f"Failed to create text file: {e}")