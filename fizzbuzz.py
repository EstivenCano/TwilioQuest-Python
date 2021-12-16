import sys

arguments = sys.argv
arguments.pop(0)


for i in arguments:
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        print("fizzbuzz")
    elif(int(i) % 3 == 0):
        print("fizz")
    elif(int(i) % 5 == 0):
        print("buzz")
    else:
        print(i)
