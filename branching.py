import sys

arguments = sys.argv
arguments.pop(0)

sum = int(arguments[0]) + int(arguments[1])

if(sum <= 0):
    print('You have chosen the path of destitution')
elif(1 < sum <= 100):
    print('You have chosen the path of plenty')
elif(sum > 100):
    print('You have chosen the path of excess')
