#! python3
# bulletPointAdder.py - Adds Wikipedia-style bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# seperate lines and add astericks
lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in 'lines' list
    lines[i] = '* ' + lines[i]  #add asterick to the start of each line
text = '\n'.join(lines)

pyperclip.copy(text)
