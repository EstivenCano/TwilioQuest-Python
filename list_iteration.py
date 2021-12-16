import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

count = 1
for i in order_of_succession:
    print(f'{count}.', i)
    count += 1
