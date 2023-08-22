from difflib import SequenceMatcher

with open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\text1.txt') as text1, open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\text2.txt') as text2:
    file1 = text1.read()
    file2 = text2.read()
    match = SequenceMatcher(None,file1,file2).ratio()
    print(f'The contents are {match*100}% common.')
