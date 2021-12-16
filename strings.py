import sys

arguments = sys.argv
arguments.pop(0)

string = ' '.join(arguments)
finalStr = str.upper(string)+'!!!'

print(finalStr)
