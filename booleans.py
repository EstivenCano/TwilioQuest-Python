import sys

arguments = sys.argv
arguments.pop(0)

python_is_glorious = True
failure_is_option = False

proper_greeting = True if arguments[0] == 'For the glory of Python!' else False
